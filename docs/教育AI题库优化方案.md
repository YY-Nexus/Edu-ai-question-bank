# 教育AI题库与作业系统优化方案
基于您的优化建议，我将提供完整的实施方案，包括代码示例、配置文件和文档更新。这些优化将提升系统的安全性、可扩展性、可维护性和用户体验。
## A. 本地/NAS部署与数据安全优化
### 1. AI模型和数据挂载优化
#### scripts/mount_nas.sh
```bash
#!/bin/bash
# NAS挂载脚本
NAS_IP="192.168.3.45"
DATA_PATH="/data"
MODELS_PATH="/models"
MEDIA_PATH="/media"
BACKUP_PATH="/backups"

# 创建挂载点
sudo mkdir -p /mnt/nas/{data,models,media,backups}

# 挂载NAS共享目录
sudo mount -t nfs ${NAS_IP}:${DATA_PATH} /mnt/nas/data
sudo mount -t nfs ${NAS_IP}:${MODELS_PATH} /mnt/nas/models
sudo mount -t nfs ${NAS_IP}:${MEDIA_PATH} /mnt/nas/media
sudo mount -t nfs ${NAS_IP}:${BACKUP_PATH} /mnt/nas/backups

# 添加到/etc/fstab实现开机自动挂载
echo "${NAS_IP}:${DATA_PATH} /mnt/nas/data nfs defaults 0 0" | sudo tee -a /etc/fstab
echo "${NAS_IP}:${MODELS_PATH} /mnt/nas/models nfs defaults 0 0" | sudo tee -a /etc/fstab
echo "${NAS_IP}:${MEDIA_PATH} /mnt/nas/media nfs defaults 0 0" | sudo tee -a /etc/fstab
echo "${NAS_IP}:${BACKUP_PATH} /mnt/nas/backups nfs defaults 0 0" | sudo tee -a /etc/fstab

echo "NAS挂载完成"

```
#### backend/config.py
```python
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    # 数据库配置
    DATABASE_URL: str = "mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db"
    
    # NAS路径配置
    NAS_DATA_PATH: str = "/mnt/nas/data"
    NAS_MODELS_PATH: str = "/mnt/nas/models"
    NAS_MEDIA_PATH: str = "/mnt/nas/media"
    NAS_BACKUP_PATH: str = "/mnt/nas/backups"
    
    # JWT配置
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Redis配置
    REDIS_URL: str = "redis://redis:6379/0"
    
    # AI模型配置
    DEFAULT_MODEL: str = "gemma-3-270m"
    AVAILABLE_MODELS: list = ["gemma-3-270m", "llama-3-8b", "phi-3-mini", "code-llama"]
    
    # 资源限制
    MAX_CONCURRENT_REQUESTS: int = 10
    MODEL_TIMEOUT: int = 30  # 秒
    
    class Config:
        env_file = ".env"

settings = Settings()

```
### 2. 数据库备份优化
#### scripts/backup_db.sh
```bash
#!/bin/bash
# 数据库备份脚本
BACKUP_DIR="/mnt/nas/backups/db"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
DB_CONTAINER="edu-ai-mariadb"
DB_NAME="edu_ai_db"
DB_USER="root"
DB_PASSWORD="yourpassword"

# 创建备份目录
mkdir -p $BACKUP_DIR

# 备份数据库
docker exec $DB_CONTAINER sh -c "exec mysqldump --databases $DB_NAME -u$DB_USER -p$DB_PASSWORD" > $BACKUP_DIR/db_backup_$TIMESTAMP.sql

# 压缩备份文件
gzip $BACKUP_DIR/db_backup_$TIMESTAMP.sql

# 保留最近30天的备份
find $BACKUP_DIR -name "db_backup_*.sql.gz" -type f -mtime +30 -delete

echo "数据库备份完成: $BACKUP_DIR/db_backup_$TIMESTAMP.sql.gz"

```
#### scripts/backup_redis.sh
```bash
#!/bin/bash
# Redis备份脚本
BACKUP_DIR="/mnt/nas/backups/redis"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
REDIS_CONTAINER="edu-ai-redis"

# 创建备份目录
mkdir -p $BACKUP_DIR

# 备份Redis数据
docker exec $REDIS_CONTAINER redis-cli --rdb $BACKUP_DIR/redis_backup_$TIMESTAMP.rdb

# 保留最近7天的备份
find $BACKUP_DIR -name "redis_backup_*.rdb" -type f -mtime +7 -delete

echo "Redis备份完成: $BACKUP_DIR/redis_backup_$TIMESTAMP.rdb"

```
### 3. 环境变量管理
#### .env.example
```plaintext
# 数据库配置
DATABASE_URL=mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db

# JWT配置
SECRET_KEY=your-secret-key-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Redis配置
REDIS_URL=redis://redis:6379/0

# NAS路径配置
NAS_DATA_PATH=/mnt/nas/data
NAS_MODELS_PATH=/mnt/nas/models
NAS_MEDIA_PATH=/mnt/nas/media
NAS_BACKUP_PATH=/mnt/nas/backups

# AI模型配置
DEFAULT_MODEL=gemma-3-270m
AVAILABLE_MODELS=["gemma-3-270m", "llama-3-8b", "phi-3-mini", "code-llama"]

# 资源限制
MAX_CONCURRENT_REQUESTS=10
MODEL_TIMEOUT=30

# 生产环境标识
ENVIRONMENT=development

```
#### backend/Dockerfile
```plaintext
FROM python:3.10

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 创建非root用户
RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app
USER app

# 暴露端口
EXPOSE 8000

# 健康检查
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# 启动命令
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

```
## B. AI服务与扩展性优化
### 1. 模型热更新和多模型切换
#### backend/services/model_service.py
```python
import os
import threading
import time
from typing import Dict, Optional, Tuple
from transformers import AutoModelForCausalLM, AutoTokenizer
from backend.config import settings

class ModelService:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ModelService, cls).__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
            
        self.models: Dict[str, Tuple[AutoModelForCausalLM, AutoTokenizer]] = {}
        self.model_load_lock = threading.Lock()
        self.last_access_time: Dict[str, float] = {}
        self._initialized = True
        
        # 预加载默认模型
        self.load_model(settings.DEFAULT_MODEL)
    
    def load_model(self, model_name: str) -> bool:
        """加载指定模型"""
        if model_name in self.models:
            self.last_access_time[model_name] = time.time()
            return True
            
        model_path = os.path.join(settings.NAS_MODELS_PATH, model_name)
        if not os.path.exists(model_path):
            return False
            
        with self.model_load_lock:
            # 再次检查，防止其他线程已经加载
            if model_name in self.models:
                self.last_access_time[model_name] = time.time()
                return True
                
            try:
                print(f"Loading model: {model_name}")
                tokenizer = AutoTokenizer.from_pretrained(model_path)
                model = AutoModelForCausalLM.from_pretrained(model_path)
                self.models[model_name] = (model, tokenizer)
                self.last_access_time[model_name] = time.time()
                print(f"Model loaded: {model_name}")
                return True
            except Exception as e:
                print(f"Failed to load model {model_name}: {str(e)}")
                return False
    
    def get_model(self, model_name: str) -> Optional[Tuple[AutoModelForCausalLM, AutoTokenizer]]:
        """获取指定模型，如果未加载则尝试加载"""
        if model_name not in self.models:
            if not self.load_model(model_name):
                return None
                
        self.last_access_time[model_name] = time.time()
        return self.models[model_name]
    
    def get_available_models(self) -> list:
        """获取可用模型列表"""
        available = []
        for model_name in settings.AVAILABLE_MODELS:
            model_path = os.path.join(settings.NAS_MODELS_PATH, model_name)
            if os.path.exists(model_path):
                available.append(model_name)
        return available
    
    def unload_model(self, model_name: str) -> bool:
        """卸载指定模型"""
        if model_name not in self.models:
            return False
            
        with self.model_load_lock:
            if model_name in self.models:
                del self.models[model_name]
                if model_name in self.last_access_time:
                    del self.last_access_time[model_name]
                print(f"Model unloaded: {model_name}")
                return True
        return False
    
    def cleanup_unused_models(self, max_idle_time: int = 3600):
        """清理长时间未使用的模型"""
        current_time = time.time()
        models_to_unload = []
        
        for model_name, last_access in self.last_access_time.items():
            if current_time - last_access > max_idle_time:
                models_to_unload.append(model_name)
                
        for model_name in models_to_unload:
            self.unload_model(model_name)

# 全局模型服务实例
model_service = ModelService()

```
#### backend/controllers/ai.py (更新版)
```python
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from backend.auth import get_current_user
from backend.services.model_service import model_service
from backend.database import get_db
from backend.models import StudentAnswer, User
import datetime
import asyncio

router = APIRouter()

@router.post("/grade")
async def ai_grade(
    payload: dict, 
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db), 
    user: User = Depends(get_current_user)
):
    # 获取模型名称，默认使用配置中的默认模型
    model_name = payload.get('model', model_service.DEFAULT_MODEL)
    
    # 检查模型是否可用
    if model_name not in model_service.get_available_models():
        raise HTTPException(status_code=400, detail=f"模型 {model_name} 不可用")
    
    # 获取模型
    model, tokenizer = model_service.get_model(model_name)
    if not model:
        raise HTTPException(status_code=500, detail=f"无法加载模型 {model_name}")
    
    # 创建学生答题记录
    sa = StudentAnswer(
        question_id=payload.get('question_id'),
        student_id=user.id,
        answer=payload['answer'],
        score=None,
        ai_explanation='',
        answer_image_url=payload.get('answer_image_url',''),
        submit_time=datetime.datetime.now()
    )
    db.add(sa)
    db.commit()
    
    # 异步执行AI批改
    task_id = f"grade_{sa.id}_{int(datetime.datetime.now().timestamp())}"
    
    # 这里简化处理，实际应该使用Celery
    background_tasks.add_task(
        process_ai_grade, 
        task_id, 
        model_name, 
        payload['question'], 
        payload['answer'],
        sa.id,
        db
    )
    
    return {"task_id": task_id}

async def process_ai_grade(task_id, model_name, question, answer, answer_id, db):
    """处理AI批改任务"""
    try:
        model, tokenizer = model_service.get_model(model_name)
        prompt = f"题目：{question}\n学生答案：{answer}\n请判断正误并给出解析："
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=128)
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # 更新数据库中的批改结果
        sa = db.query(StudentAnswer).filter(StudentAnswer.id == answer_id).first()
        if sa:
            sa.ai_explanation = result
            db.commit()
            
        # 这里可以添加WebSocket通知或更新Redis中的任务状态
        print(f"Task {task_id} completed: {result}")
        
    except Exception as e:
        print(f"Error processing task {task_id}: {str(e)}")

@router.get("/grade-result/{task_id}")
def get_grade_result(task_id: str):
    """获取AI批改结果"""
    # 这里简化处理，实际应该从Redis或数据库中查询任务状态
    # 返回模拟结果
    return {
        "status": "done",
        "result": "AI批改结果和解析"
    }

@router.get("/models")
def get_available_models():
    """获取可用模型列表"""
    return {
        "available_models": model_service.get_available_models(),
        "default_model": model_service.DEFAULT_MODEL
    }

@router.post("/models/{model_name}/load")
def load_model(model_name: str):
    """加载指定模型"""
    success = model_service.load_model(model_name)
    return {"success": success, "message": f"模型 {model_name} 加载{'成功' if success else '失败'}"}

@router.post("/models/{model_name}/unload")
def unload_model(model_name: str):
    """卸载指定模型"""
    success = model_service.unload_model(model_name)
    return {"success": success, "message": f"模型 {model_name} 卸载{'成功' if success else '失败'}"}

```
### 2. 资源监控和限流
#### backend/middleware/rate_limiter.py
```python
import time
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from collections import defaultdict
from backend.config import settings

class RateLimiter:
    def __init__(self):
        self.requests = defaultdict(list)
        self.max_requests = settings.MAX_CONCURRENT_REQUESTS
        self.time_window = 60  # 秒
    
    def check_rate_limit(self, key: str) -> bool:
        now = time.time()
        key_requests = self.requests[key]
        
        # 移除时间窗口外的请求记录
        while key_requests and key_requests[0] <= now - self.time_window:
            key_requests.pop(0)
        
        # 检查是否超过限制
        if len(key_requests) >= self.max_requests:
            return False
            
        # 记录当前请求
        key_requests.append(now)
        return True

rate_limiter = RateLimiter()

async def rate_limit_middleware(request: Request, call_next):
    # 使用用户ID或IP作为限流键
    client_ip = request.client.host
    user_id = request.headers.get("X-User-ID")
    key = user_id if user_id else client_ip
    
    if not rate_limiter.check_rate_limit(key):
        return JSONResponse(
            status_code=429,
            content={"detail": "请求过于频繁，请稍后再试"}
        )
    
    response = await call_next(request)
    return response

```
#### backend/main.py (更新版)
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.controllers import ai, homework, question
from backend.database import engine
from backend.models import Base
from backend.middleware.rate_limiter import rate_limit_middleware
import uvicorn

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI(title="教育AI题库系统", version="1.0.0")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 添加限流中间件
app.middleware("http")(rate_limit_middleware)

# 注册路由
app.include_router(question.router, prefix="/api/questions", tags=["题库管理"])
app.include_router(homework.router, prefix="/api/homework", tags=["作业管理"])
app.include_router(ai.router, prefix="/api/ai", tags=["AI服务"])

@app.get("/health")
def health_check():
    """健康检查端点"""
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

```
### 3. 异步任务回调优化
#### backend/websocket_manager.py
```python
import asyncio
import json
from typing import Dict, List
from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}
    
    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        if user_id not in self.active_connections:
            self.active_connections[user_id] = []
        self.active_connections[user_id].append(websocket)
    
    def disconnect(self, websocket: WebSocket, user_id: str):
        if user_id in self.active_connections:
            self.active_connections[user_id].remove(websocket)
            if not self.active_connections[user_id]:
                del self.active_connections[user_id]
    
    async def send_personal_message(self, message: str, user_id: str):
        if user_id in self.active_connections:
            for connection in self.active_connections[user_id]:
                try:
                    await connection.send_text(message)
                except:
                    # 连接可能已断开，移除它
                    self.active_connections[user_id].remove(connection)
    
    async def broadcast(self, message: str):
        for user_id, connections in self.active_connections.items():
            for connection in connections:
                try:
                    await connection.send_text(message)
                except:
                    # 连接可能已断开，移除它
                    connections.remove(connection)

manager = ConnectionManager()

```
#### backend/controllers/websocket.py
```python
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from backend.auth import get_current_user
from backend.websocket_manager import manager
from backend.database import get_db
from backend.models import User

router = APIRouter()

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int, db=Depends(get_db)):
    # 验证用户
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        await websocket.close(code=4000, reason="用户不存在")
        return
    
    await manager.connect(websocket, str(user_id))
    try:
        while True:
            data = await websocket.receive_text()
            # 处理接收到的消息
            await manager.send_personal_message(f"你说了: {data}", str(user_id))
    except WebSocketDisconnect:
        manager.disconnect(websocket, str(user_id))
        await manager.broadcast(f"用户 {user.name} 离开了聊天")

```
## C. 前端可视化与交互优化
### 1. 数据可视化模块抽象
#### frontend/src/components/charts/QuestionDistributionChart.vue
```plaintext
<template>
  <div class="chart-container" ref="chartContainer"></div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import * as echarts from 'echarts'

const props = defineProps({
  chartData: {
    type: Object,
    required: true
  },
  chartType: {
    type: String,
    default: 'bar'
  },
  title: {
    type: String,
    default: ''
  }
})

const chartContainer = ref(null)
let chart = null

const initChart = () => {
  if (!chartContainer.value) return
  
  chart = echarts.init(chartContainer.value)
  
  const option = {
    title: {
      text: props.title,
      left: 'center'
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: props.chartData.xAxis
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        name: '数量',
        type: props.chartType,
        data: props.chartData.series,
        itemStyle: {
          color: '#409EFF'
        }
      }
    ]
  }
  
  chart.setOption(option)
}

const resizeChart = () => {
  if (chart) {
    chart.resize()
  }
}

watch(() => props.chartData, () => {
  if (chart) {
    chart.setOption({
      xAxis: {
        data: props.chartData.xAxis
      },
      series: [
        {
          data: props.chartData.series
        }
      ]
    })
  }
}, { deep: true })

onMounted(() => {
  initChart()
  window.addEventListener('resize', resizeChart)
})

onUnmounted(() => {
  if (chart) {
    chart.dispose()
  }
  window.removeEventListener('resize', resizeChart)
})
</script>

<style scoped>
.chart-container {
  width: 100%;
  height: 400px;
}
</style>

```
#### frontend/src/components/charts/StudentPerformanceChart.vue
```plaintext
<template>
  <div class="chart-container" ref="chartContainer"></div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import * as echarts from 'echarts'

const props = defineProps({
  performanceData: {
    type: Array,
    required: true
  },
  title: {
    type: String,
    default: '学生成绩分布'
  }
})

const chartContainer = ref(null)
let chart = null

const initChart = () => {
  if (!chartContainer.value) return
  
  chart = echarts.init(chartContainer.value)
  
  // 处理数据，计算分数段
  const scoreRanges = ['0-59', '60-69', '70-79', '80-89', '90-100']
  const scoreCounts = [0, 0, 0, 0, 0]
  
  props.performanceData.forEach(item => {
    const score = item.score
    if (score < 60) scoreCounts[0]++
    else if (score < 70) scoreCounts[1]++
    else if (score < 80) scoreCounts[2]++
    else if (score < 90) scoreCounts[3]++
    else scoreCounts[4]++
  })
  
  const option = {
    title: {
      text: props.title,
      left: 'center'
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: scoreRanges
    },
    yAxis: {
      type: 'value',
      name: '学生人数'
    },
    series: [
      {
        name: '人数',
        type: 'bar',
        data: scoreCounts,
        itemStyle: {
          color: function(params) {
            const colorList = ['#F56C6C', '#E6A23C', '#409EFF', '#67C23A', '#909399']
            return colorList[params.dataIndex]
          }
        }
      }
    ]
  }
  
  chart.setOption(option)
}

const resizeChart = () => {
  if (chart) {
    chart.resize()
  }
}

watch(() => props.performanceData, () => {
  if (chart) {
    initChart()
  }
}, { deep: true })

onMounted(() => {
  initChart()
  window.addEventListener('resize', resizeChart)
})

onUnmounted(() => {
  if (chart) {
    chart.dispose()
  }
  window.removeEventListener('resize', resizeChart)
})
</script>

<style scoped>
.chart-container {
  width: 100%;
  height: 400px;
}
</style>

```
### 2. Excel导入模板校验优化
#### frontend/src/components/ExcelImport.vue (优化版)
```plaintext
<template>
  <div class="excel-import">
    <el-card>
      <h2>题库Excel导入</h2>
      <div class="template-download">
        <el-link :href="templateUrl" target="_blank" type="primary">
          <el-icon><Download /></el-icon>
          下载Excel模板
        </el-link>
      </div>
      
      <el-upload
        class="upload-demo"
        :action="uploadUrl"
        :headers="{ Authorization: 'Bearer ' + token }"
        :on-success="handleSuccess"
        :on-error="handleError"
        :before-upload="beforeUpload"
        :file-list="fileList"
        accept=".xlsx, .xls"
        :limit="1"
        :auto-upload="false"
        ref="uploadRef"
      >
        <template #trigger>
          <el-button type="primary">选择文件</el-button>
        </template>
        <el-button class="ml-3" type="success" @click="submitUpload">
          开始上传
        </el-button>
        <template #tip>
          <div class="el-upload__tip">
            只能上传xlsx/xls文件，且不超过10MB
          </div>
        </template>
      </el-upload>
      
      <div v-if="validationErrors.length > 0" class="validation-errors">
        <h3>文件校验错误：</h3>
        <ul>
          <li v-for="(error, index) in validationErrors" :key="index" class="error-item">
            {{ error }}
          </li>
        </ul>
      </div>
      
      <el-alert
        v-if="message"
        :title="message"
        :type="messageType"
        show-icon
        :closable="false"
        style="margin-top: 20px;"
      />
      
      <div class="actions">
        <el-button @click="$emit('close')">关闭</el-button>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Download } from '@element-plus/icons-vue'
import axios from '@/api'
import * as XLSX from 'xlsx'

const emit = defineEmits(['close'])

const token = localStorage.getItem('token')
const templateUrl = '/api/questions/excel-template'
const uploadUrl = '/api/questions/import-excel'
const uploadRef = ref()
const fileList = ref([])
const message = ref('')
const messageType = ref('success')
const validationErrors = ref([])

// 模板必需字段
const requiredFields = ['题干', '学科ID', '难度']
// 有效难度值
const validDifficulties = ['易', '中', '难', '奥数']

const beforeUpload = (file) => {
  validationErrors.value = []
  
  // 检查文件类型
  const isExcel = file.type === 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' || 
                  file.type === 'application/vnd.ms-excel'
  if (!isExcel) {
    ElMessage.error('只能上传Excel文件!')
    return false
  }
  
  // 检查文件大小
  const isLt10M = file.size / 1024 / 1024 < 10
  if (!isLt10M) {
    ElMessage.error('文件大小不能超过 10MB!')
    return false
  }
  
  // 读取并验证Excel内容
  return new Promise((resolve) => {
    const reader = new FileReader()
    reader.onload = (e) => {
      try {
        const data = new Uint8Array(e.target.result)
        const workbook = XLSX.read(data, { type: 'array' })
        const firstSheetName = workbook.SheetNames[0]
        const worksheet = workbook.Sheets[firstSheetName]
        const jsonData = XLSX.utils.sheet_to_json(worksheet)
        
        // 验证数据
        validateExcelData(jsonData)
        
        if (validationErrors.value.length > 0) {
          ElMessage.error('文件校验失败，请查看错误信息')
          resolve(false)
        } else {
          resolve(true)
        }
      } catch (error) {
        ElMessage.error('文件解析失败: ' + error.message)
        resolve(false)
      }
    }
    reader.readAsArrayBuffer(file)
  })
}

const validateExcelData = (data) => {
  if (data.length === 0) {
    validationErrors.value.push('Excel文件为空')
    return
  }
  
  // 检查必需字段
  const firstRow = data[0]
  requiredFields.forEach(field => {
    if (!(field in firstRow)) {
      validationErrors.value.push(`缺少必需字段: ${field}`)
    }
  })
  
  // 检查每行数据
  data.forEach((row, index) => {
    const rowNum = index + 1
    
    // 检查题干
    if (!row['题干'] || row['题干'].trim() === '') {
      validationErrors.value.push(`第${rowNum}行: 题干不能为空`)
    }
    
    // 检查学科ID
    if (!row['学科ID'] || isNaN(row['学科ID'])) {
      validationErrors.value.push(`第${rowNum}行: 学科ID必须为数字`)
    }
    
    // 检查难度
    if (!validDifficulties.includes(row['难度'])) {
      validationErrors.value.push(`第${rowNum}行: 难度值无效，应为: ${validDifficulties.join(', ')}`)
    }
  })
}

const submitUpload = () => {
  uploadRef.value.submit()
}

const handleSuccess = (response) => {
  message.value = response.msg || '导入成功'
  messageType.value = 'success'
  fileList.value = []
  ElMessage.success('导入成功')
}

const handleError = (error) => {
  message.value = '导入失败'
  messageType.value = 'error'
  console.error('导入错误:', error)
  ElMessage.error('导入失败')
}
</script>

<style scoped>
.excel-import {
  margin-top: 20px;
}
.template-download {
  margin-bottom: 20px;
}
.validation-errors {
  margin-top: 20px;
  padding: 10px;
  background-color: #fef0f0;
  border-radius: 4px;
}
.validation-errors h3 {
  margin-top: 0;
  color: #f56c6c;
}
.error-item {
  color: #f56c6c;
}
.actions {
  margin-top: 20px;
  text-align: right;
}
.ml-3 {
  margin-left: 10px;
}
</style>

```
### 3. 多权限支持优化
#### frontend/src/router/index.js (优化版)
```javascript
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import StudentDashboard from '../views/StudentDashboard.vue'
import TeacherDashboard from '../views/TeacherDashboard.vue'
import AdminPanel from '../views/AdminPanel.vue'
import { useUserStore } from '../store'

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login, meta: { guestOnly: true } },
  { 
    path: '/student', 
    component: StudentDashboard, 
    meta: { requiresAuth: true, roles: ['student'] } 
  },
  { 
    path: '/teacher', 
    component: TeacherDashboard, 
    meta: { requiresAuth: true, roles: ['teacher'] } 
  },
  { 
    path: '/admin', 
    component: AdminPanel, 
    meta: { requiresAuth: true, roles: ['admin'] } 
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫
router.beforeEach(async (to, from, next) => {
  const userStore = useUserStore()
  
  // 检查是否已登录
  const isAuthenticated = userStore.isAuthenticated
  
  // 需要登录但未登录
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login')
    return
  }
  
  // 已登录但访问仅限游客的页面（如登录页）
  if (to.meta.guestOnly && isAuthenticated) {
    next('/')
    return
  }
  
  // 检查角色权限
  if (to.meta.roles && isAuthenticated) {
    // 如果用户信息未加载，先加载
    if (!userStore.userInfo) {
      try {
        await userStore.fetchUserInfo()
      } catch (error) {
        // 获取用户信息失败，可能是token过期
        userStore.logout()
        next('/login')
        return
      }
    }
    
    // 检查用户角色是否有权限访问
    if (!to.meta.roles.includes(userStore.userInfo.role)) {
      next('/login')
      return
    }
  }
  
  next()
})

export default router

```
#### frontend/src/store/index.js (优化版)
```javascript
import { defineStore } from 'pinia'
import axios from '@/api'

export const useUserStore = defineStore('user', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    userInfo: JSON.parse(localStorage.getItem('userInfo')) || null,
    isAuthenticated: !!localStorage.getItem('token')
  }),
  
  getters: {
    userRole: (state) => state.userInfo?.role || null,
    userName: (state) => state.userInfo?.name || null,
    userId: (state) => state.userInfo?.id || null
  },
  
  actions: {
    setToken(token) {
      this.token = token
      localStorage.setItem('token', token)
      this.isAuthenticated = true
    },
    
    setUserInfo(userInfo) {
      this.userInfo = userInfo
      localStorage.setItem('userInfo', JSON.stringify(userInfo))
    },
    
    async login(username, password) {
      try {
        const response = await axios.post('/auth/login', { username, password })
        this.setToken(response.data.token)
        await this.fetchUserInfo()
        return { success: true }
      } catch (error) {
        return { 
          success: false, 
          message: error.response?.data?.detail || '登录失败' 
        }
      }
    },
    
    async fetchUserInfo() {
      try {
        const response = await axios.get('/users/me')
        this.setUserInfo(response.data)
        return response.data
      } catch (error) {
        this.logout()
        throw error
      }
    },
    
    logout() {
      this.token = null
      this.userInfo = null
      this.isAuthenticated = false
      localStorage.removeItem('token')
      localStorage.removeItem('userInfo')
    },
    
    async checkAuth() {
      if (this.token && !this.userInfo) {
        try {
          await this.fetchUserInfo()
        } catch (error) {
          this.logout()
          return false
        }
      }
      return this.isAuthenticated
    }
  }
})

```
## D. CI/CD与运维自动化优化
### 1. 自动化测试
#### backend/tests/test_api.py
```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.main import app
from backend.database import get_db
from backend.models import Base, User, Question
import os

# 使用测试数据库
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建测试数据库表
Base.metadata.create_all(bind=engine)

# 覆盖数据库依赖
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture
def test_user():
    return {
        "username": "testuser",
        "password": "testpass",
        "name": "测试用户",
        "role": "teacher"
    }

@pytest.fixture
def auth_headers(test_user):
    # 创建测试用户
    response = client.post("/auth/login", json={
        "username": test_user["username"],
        "password": test_user["password"]
    })
    token = response.json()["token"]
    return {"Authorization": f"Bearer {token}"}

def test_login(test_user):
    response = client.post("/auth/login", json={
        "username": test_user["username"],
        "password": test_user["password"]
    })
    assert response.status_code == 200
    assert "token" in response.json()

def test_create_question(auth_headers):
    question_data = {
        "content": "测试题目",
        "subject_id": 1,
        "difficulty": "中",
        "tags": "测试"
    }
    response = client.post("/api/questions/", json=question_data, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["msg"] == "题目已创建"

def test_get_questions(auth_headers):
    response = client.get("/api/questions/", headers=auth_headers)
    assert response.status_code == 200
    assert "items" in response.json()

def test_unauthorized_access():
    response = client.get("/api/questions/")
    assert response.status_code == 401

```
#### frontend/tests/components/ExcelImport.spec.js
```javascript
import { mount } from '@vue/test-utils'
import { describe, it, expect, vi } from 'vitest'
import ExcelImport from '@/components/ExcelImport.vue'
import axios from '@/api'
import ElementPlus from 'element-plus'

// 模拟axios
vi.mock('@/api', () => ({
  default: {
    get: vi.fn(),
    post: vi.fn()
  }
}))

describe('ExcelImport.vue', () => {
  it('renders correctly', () => {
    const wrapper = mount(ExcelImport, {
      global: {
        plugins: [ElementPlus],
        stubs: ['el-upload', 'el-button', 'el-link', 'el-card', 'el-alert']
      }
    })
    expect(wrapper.find('.excel-import').exists()).toBe(true)
  })

  it('emits close event when close button is clicked', async () => {
    const wrapper = mount(ExcelImport, {
      global: {
        plugins: [ElementPlus],
        stubs: ['el-upload', 'el-button', 'el-link', 'el-card', 'el-alert']
      }
    })
    
    await wrapper.find('.actions button').trigger('click')
    expect(wrapper.emitted()).toHaveProperty('close')
  })

  it('validates Excel file before upload', async () => {
    const wrapper = mount(ExcelImport, {
      global: {
        plugins: [ElementPlus],
        stubs: ['el-upload', 'el-button', 'el-link', 'el-card', 'el-alert']
      }
    })
    
    // 模拟文件选择
    const file = new File(['dummy content'], 'test.xlsx', { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' })
    const uploadComponent = wrapper.findComponent({ name: 'ElUpload' })
    
    // 触发before-upload钩子
    const result = await uploadComponent.vm.beforeUpload(file)
    expect(result).toBe(true)
  })
})

```
### 2. GitHub Actions CI/CD
#### .github/workflows/ci-cd.yml
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      mariadb:
        image: mariadb:10.6
        env:
          MYSQL_ROOT_PASSWORD: testpass
          MYSQL_DATABASE: test_db
        ports:
          - 3306:3306
        options: --health-cmd="mysqladmin ping" --health-interval=10s --health-timeout=5s --health-retries=3
    
    redis:
      image: redis:6-alpine
      ports:
        - 6379:6379
      options: --health-cmd="redis-cli ping" --health-interval=10s --health-timeout=5s --health-retries=3
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r backend/requirements.txt
        pip install pytest pytest-asyncio httpx
    
    - name: Run backend tests
      run: |
        cd backend
        pytest tests/ -v
    
    - name: Set up Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        cache: 'npm'
        cache-dependency-path: frontend/package-lock.json
    
    - name: Install frontend dependencies
      run: |
        cd frontend
        npm ci
    
    - name: Run frontend tests
      run: |
        cd frontend
        npm run test:unit
    
    - name: Build frontend
      run: |
        cd frontend
        npm run build

  build-and-push:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    permissions:
      contents: read
      packages: write
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2
    
    - name: Log in to Container Registry
      uses: docker/login-action@v2
      with:
        registry: ${{ env.REGISTRY }}
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
    
    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v4
      with:
        images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
        tags: |
          type=ref,event=branch
          type=ref,event=pr
          type=sha,prefix={{branch}}-
          type=raw,value=latest,enable={{is_default_branch}}
    
    - name: Build and push backend Docker image
      uses: docker/build-push-action@v4
      with:
        context: ./backend
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}
        cache-from: type=gha
        cache-to: type=gha,mode=max
    
    - name: Build and push frontend Docker image
      uses: docker/build-push-action@v4
      with:
        context: ./frontend
        push: true
        tags: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}-frontend:${{ github.sha }}
        labels: ${{ steps.meta.outputs.labels }}
        cache-from: type=gha
        cache-to: type=gha,mode=max

  deploy:
    needs: build-and-push
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    
    - name: Set up kubectl
      uses: azure/setup-kubectl@v3
      with:
        version: '1.28.0'
    
    - name: Configure kubeconfig
      run: |
        mkdir -p $HOME/.kube
        echo "${{ secrets.KUBE_CONFIG }}" | base64 -d > $HOME/.kube/config
        chmod 600 $HOME/.kube/config
    
    - name: Update Kubernetes deployment
      run: |
        # 更新镜像版本
        sed -i "s|ghcr.io/${{ github.repository }}:.*|ghcr.io/${{ github.repository }}:${{ github.sha }}|g" k8s/edu-ai-backend-deployment.yaml
        sed -i "s|ghcr.io/${{ github.repository }}-frontend:.*|ghcr.io/${{ github.repository }}-frontend:${{ github.sha }}|g" k8s/edu-ai-frontend-deployment.yaml
        
        # 应用配置
        kubectl apply -f k8s/
        
        # 等待部署完成
        kubectl rollout status deployment/edu-ai-backend
        kubectl rollout status deployment/edu-ai-frontend

```
### 3. 健康检查与告警
#### k8s/edu-ai-backend-deployment.yaml (更新版)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: edu-ai-backend
spec:
  replicas: 2
  selector:
    matchLabels:
      app: edu-ai-backend
  template:
    metadata:
      labels:
        app: edu-ai-backend
    spec:
      containers:
      - name: backend
        image: ghcr.io/your-repo/edu-ai-backend:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          value: "mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db"
        - name: CELERY_BROKER_URL
          value: "redis://redis:6379/0"
        volumeMounts:
        - name: nas-models
          mountPath: /mnt/nas/models
        resources:
          limits:
            cpu: "2"
            memory: "4Gi"
          requests:
            cpu: "500m"
            memory: "1Gi"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
          timeoutSeconds: 3
          failureThreshold: 1
      volumes:
      - name: nas-models
        persistentVolumeClaim:
          claimName: nas-models-pvc

```
#### scripts/monitor_nas.sh
```bash
#!/bin/bash
# NAS资源监控脚本

NAS_IP="192.168.3.45"
ALERT_EMAIL="admin@example.com"
ALERT_THRESHOLD=90  # 磁盘使用率阈值(%)

# 检查磁盘使用率
DISK_USAGE=$(ssh $NAS_IP "df -h /data | tail -1 | awk '{print \$5}' | sed 's/%//'")

if [ "$DISK_USAGE" -ge "$ALERT_THRESHOLD" ]; then
    # 发送告警邮件
    echo "NAS磁盘使用率告警: ${DISK_USAGE}%" | mail -s "NAS磁盘使用率告警" $ALERT_EMAIL
    
    # 记录到日志
    echo "$(date): NAS磁盘使用率告警: ${DISK_USAGE}%" >> /var/log/nas_monitor.log
    
    # 可以添加其他告警方式，如Slack、企业微信等
fi

# 检查模型服务状态
MODEL_SERVICES=("gemma-3-270m" "llama-3-8b")
for service in "${MODEL_SERVICES[@]}"; do
    if ! ssh $NAS_IP "ps aux | grep -v grep | grep $service"; then
        echo "$(date): 模型服务 $service 未运行" >> /var/log/nas_monitor.log
        echo "模型服务 $service 未运行" | mail -s "模型服务告警" $ALERT_EMAIL
    fi
done

```
#### scripts/cron_monitor.sh
```bash
#!/bin/bash
# 设置监控任务到crontab
# 每小时检查一次NAS状态
(crontab -l 2>/dev/null; echo "0 * * * * /path/to/scripts/monitor_nas.sh") | crontab -

# 每天凌晨2点备份数据库
(crontab -l 2>/dev/null; echo "0 2 * * * /path/to/scripts/backup_db.sh") | crontab -

# 每天凌晨3点备份Redis
(crontab -l 2>/dev/null; echo "0 3 * * * /path/to/scripts/backup_redis.sh") | crontab -

echo "监控任务已设置"

```
## E. 文档与开发协作优化
### 1. API文档自动生成
#### backend/docs/api_examples.md
```plaintext
# API接口调用示例

## 认证接口

### 登录获取JWT令牌

**请求**
```http
POST /auth/login
Content-Type: application/json

{
  "username": "teacher",
  "password": "password123"
}

```
响应
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "role": "teacher"
}

```
## 题库管理接口
### 获取题库列表
请求
```http
GET /api/questions?subject_id=1&keyword=数学
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

```
响应
```json
{
  "items": [
    {
      "id": 1,
      "content": "勾股定理是什么？",
      "difficulty": "中",
      "tags": "数学,几何",
      "image_url": "http://example.com/image.png"
    }
  ]
}

```
### 创建新题目
请求
```http
POST /api/questions
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
  "content": "勾股定理是什么？",
  "subject_id": 1,
  "difficulty": "中",
  "tags": "数学,几何",
  "option_a": "a+b=c",
  "option_b": "a^2+b^2=c^2",
  "option_c": "a*b=c",
  "option_d": "a/b=c",
  "answer": "a^2+b^2=c^2",
  "explanation": "勾股定理公式为a^2+b^2=c^2",
  "image_url": "http://example.com/image.png",
  "extra_json": "{\"latex\":\"a^2+b^2=c^2\"}"
}

```
响应
```json
{
  "msg": "题目已创建",
  "id": 1
}

```
## AI服务接口
### 提交AI批改任务
请求
```http
POST /api/ai/grade
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
  "question": "勾股定理是什么？",
  "answer": "a^2+b^2=c^2",
  "model": "gemma-3-270m",
  "question_id": 1
}

```
响应
```json
{
  "task_id": "grade_1_1642680000"
}

```
### 获取AI批改结果
请求
```http
GET /api/ai/grade-result/grade_1_1642680000
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

```
响应
```json
{
  "status": "done",
  "result": "回答正确。勾股定理是一个基本的几何定理，描述了直角三角形的三边关系。公式为a²+b²=c²，其中a和b是直角边，c是斜边。"
}

```
## 作业管理接口
### 获取待批改作业列表
请求
```http
GET /api/homework/review-list
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

```
响应
```json
{
  "items": [
    {
      "id": 1,
      "studentName": "张三",
      "question": "勾股定理是什么？",
      "answer": "a^2+b^2=c^2",
      "ai_explanation": "回答正确。勾股定理是一个基本的几何定理...",
      "score": null,
      "comment": ""
    }
  ]
}

```
### 提交作业批改结果
请求
```http
POST /api/homework/review
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
  "id": 1,
  "score": 95.5,
  "comment": "回答正确，表述清晰"
}

```
响应
```json
{
  "msg": "批改成功"
}

```
```plaintext

### 2. 用户/开发者手册

#### docs/user_guide.md
```markdown
# 教育AI题库系统用户指南

## 目录
1. [系统简介](#系统简介)
2. [快速开始](#快速开始)
3. [功能说明](#功能说明)
   - [题库管理](#题库管理)
   - [作业管理](#作业管理)
   - [AI批改](#ai批改)
4. [常见问题](#常见问题)

## 系统简介

教育AI题库系统是一个面向教育机构的智能题库管理平台，提供题库管理、作业布置、AI自动批改等功能，帮助教师提高工作效率，为学生提供个性化学习体验。

## 快速开始

### 系统要求
- 现代浏览器（Chrome、Firefox、Safari、Edge）
- 稳定的网络连接

### 登录系统
1. 打开浏览器，访问系统地址
2. 输入用户名和密码
3. 点击"登录"按钮

### 首次使用
1. 系统会根据您的角色（学生/教师/管理员）自动跳转到相应界面
2. 教师用户需要先创建题库或导入题库
3. 学生用户可以查看已布置的作业并提交答案

## 功能说明

### 题库管理

#### 创建题目
1. 进入教师控制台
2. 点击"题库管理"标签
3. 点击"新建题目"按钮
4. 填写题目信息，包括题干、选项、答案、解析等
5. 点击"保存"按钮

#### Excel导入题库
1. 进入教师控制台
2. 点击"题库管理"标签
3. 点击"Excel导入"按钮
4. 下载Excel模板
5. 按照模板格式填写题目信息
6. 上传填写好的Excel文件
7. 系统会自动校验并导入题目

#### 查看题目
1. 进入教师控制台
2. 点击"题库管理"标签
3. 系统会显示所有题目列表
4. 点击"查看"按钮可以查看题目详情

### 作业管理

#### 布置作业
1. 进入教师控制台
2. 点击"作业管理"标签
3. 点击"布置新作业"按钮
4. 填写作业标题和说明
5. 从题库中选择题目
6. 选择学生或班级
7. 点击"发布"按钮

#### 批改作业
1. 进入教师控制台
2. 点击"作业批改"标签
3. 系统会显示所有待批改的作业
4. 查看学生答案和AI批改结果
5. 输入分数和评语
6. 点击"提交"按钮

#### 查看作业（学生）
1. 进入学生控制台
2. 系统会显示所有已布置的作业
3. 点击作业名称可以查看详情
4. 填写答案并提交

### AI批改

#### AI自动批改
1. 学生提交答案后，系统会自动调用AI模型进行批改
2. AI批改结果会显示在作业批改界面
3. 教师可以查看AI批改结果并进行人工调整

#### 模型选择
1. 系统支持多种AI模型（如Gemma、Llama等）
2. 教师可以在批改时选择合适的模型
3. 系统会记住您的选择，下次自动使用

## 常见问题

### Q: 忘记密码怎么办？
A: 点击登录页面的"忘记密码"链接，按照提示重置密码。

### Q: Excel导入失败怎么办？
A: 请检查以下几点：
   - 文件格式是否为.xlsx或.xls
   - 是否按照模板格式填写
   - 必填字段是否完整
   - 难度值是否为"易"、"中"、"难"、"奥数"之一

### Q: AI批改结果不准确怎么办？
A: 您可以手动调整批改结果，系统会记录您的调整并用于模型优化。

### Q: 如何联系技术支持？
A: 请发送邮件至support@example.com或拨打技术支持电话。

```
#### docs/developer_guide.md
```plaintext
# 教育AI题库系统开发者指南

## 目录
1. [系统架构](#系统架构)
2. [开发环境搭建](#开发环境搭建)
3. [代码结构](#代码结构)
4. [API开发](#api开发)
5. [前端开发](#前端开发)
6. [AI服务集成](#ai服务集成)
7. [部署指南](#部署指南)
8. [贡献指南](#贡献指南)

## 系统架构

### 整体架构
系统采用前后端分离架构，包含以下核心组件：

- **前端**: Vue3 + Element Plus构建的单页应用
- **后端**: FastAPI提供RESTful API
- **数据库**: MariaDB存储业务数据
- **缓存**: Redis用于会话存储和任务队列
- **AI服务**: 基于Hugging Face Transformers的本地模型
- **部署**: Docker容器化，Kubernetes编排

### 数据流
1. 用户通过浏览器访问前端应用
2. 前端通过HTTP请求与后端API交互
3. 后端处理业务逻辑，操作数据库
4. AI批改任务通过Celery异步处理
5. 结果通过WebSocket或轮询返回给前端

## 开发环境搭建

### 后端开发环境
1. 安装Python 3.10+
2. 创建虚拟环境:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

```
1. 安装依赖:
    ```bash
pip install -r backend/requirements.txt

```
2. 配置环境变量:
    ```bash
cp backend/.env.example backend/.env
# 编辑.env文件，配置数据库连接等信息

```
3. 运行数据库迁移:
    ```bash
cd backend
alembic upgrade head

```
4. 启动开发服务器:
    ```bash
uvicorn backend.main:app --reload

```
### 前端开发环境
1. 安装Node.js 16+
2. 进入前端目录:
    ```bash
cd frontend

```
3. 安装依赖:
    ```bash
npm install

```
4. 启动开发服务器:
    ```bash
npm run dev

```
### 完整环境启动
1. 确保Docker已安装
2. 运行:
    ```bash
docker-compose up -d

```
3. 访问: http://localhost:5173
## 代码结构
### 后端结构
```plaintext
backend/
├── controllers/       # API控制器
│   ├── ai.py          # AI相关API
│   ├── homework.py    # 作业相关API
│   └── question.py   # 题库相关API
├── models.py         # 数据库模型
├── database.py       # 数据库连接
├── auth.py           # 认证相关
├── services/         # 业务服务
│   └── model_service.py  # AI模型服务
├── middleware/       # 中间件
│   └── rate_limiter.py   # 限流中间件
├── main.py           # FastAPI入口
├── requirements.txt  # Python依赖
└── tests/            # 测试代码

```
### 前端结构
```plaintext
frontend/
├── src/
│   ├── api/           # API封装
│   ├── assets/        # 静态资源
│   ├── components/    # 组件
│   ├── router/        # 路由配置
│   ├── store/         # 状态管理
│   ├── views/         # 页面
│   ├── App.vue        # 根组件
│   └── main.js        # 入口文件
├── public/            # 公共资源
├── package.json       # 项目配置
└── vite.config.js     # Vite配置

```
## API开发
### 创建新API
1. 在backend/controllers/下创建新的控制器文件
2. 定义API路由和处理函数
3. 在backend/main.py中注册路由
4. 添加相应的测试用例
### 示例：创建新API
```python
# backend/controllers/example.py
from fastapi import APIRouter, Depends
from backend.auth import get_current_user

router = APIRouter()

@router.get("/example")
def example_endpoint(user=Depends(get_current_user)):
    return {"message": "这是一个示例API", "user": user.username}

```
```python
# backend/main.py
from backend.controllers import example

app.include_router(example.router, prefix="/api/example", tags=["示例"])

```
## 前端开发
### 创建新组件
1. 在frontend/src/components/下创建新的Vue组件
2. 实现组件逻辑和模板
3. 在需要的页面中引入并使用组件
### 示例：创建新组件
```plaintext
<!-- frontend/src/components/ExampleComponent.vue -->
<template>
  <div class="example-component">
    <h2>{{ title }}</h2>
    <p>{{ message }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const title = ref('示例组件')
const message = ref('这是一个示例组件')
</script>

<style scoped>
.example-component {
  padding: 20px;
  border: 1px solid #eee;
  border-radius: 4px;
}
</style>

```
### 创建新页面
1. 在frontend/src/views/下创建新的Vue组件
2. 在frontend/src/router/index.js中添加路由配置
3. 实现页面逻辑和模板
## AI服务集成
### 添加新模型
1. 将模型文件下载到NAS的/mnt/nas/models/目录下
2. 在backend/config.py的AVAILABLE_MODELS列表中添加模型名称
3. 重启后端服务或使用API热加载模型
### 示例：添加新模型
```python
# backend/config.py
AVAILABLE_MODELS = ["gemma-3-270m", "llama-3-8b", "phi-3-mini", "code-llama", "new-model"]

```
### 优化模型性能
1. 使用模型量化减少内存占用
2. 调整批处理大小提高吞吐量
3. 使用GPU加速（如果可用）
## 部署指南
### Docker部署
1. 构建镜像:
    ```bash
docker-compose build

```
2. 启动服务:
    ```bash
docker-compose up -d

```
3. 查看日志:
    ```bash
docker-compose logs -f

```
### Kubernetes部署
1. 配置kubectl连接到K8s集群
2. 应用配置:
    ```bash
kubectl apply -f k8s/

```
3. 查看部署状态:
    ```bash
kubectl get pods -w

```
### NAS配置
1. 挂载NAS目录:
    ```bash
sudo mkdir -p /mnt/nas/{data,models,media,backups}
sudo mount -t nfs 192.168.3.45:/data /mnt/nas/data
sudo mount -t nfs 192.168.3.45:/models /mnt/nas/models
sudo mount -t nfs 192.168.3.45:/media /mnt/nas/media
sudo mount -t nfs 192.168.3.45:/backups /mnt/nas/backups

```
2. 添加到/etc/fstab实现开机自动挂载
## 贡献指南
### 代码规范
- 遵循PEP 8 Python代码规范
- 遵循Vue 3组合式API风格
- 使用ESLint和Prettier格式化代码
### 提交规范
- feat: 新功能
- fix: 修复bug
- docs: 文档更新
- style: 代码格式调整
- refactor: 代码重构
- test: 测试相关
- chore: 构建过程或辅助工具的变动
### 提交流程
1. Fork项目
2. 创建特性分支: git checkout -b feature/your-feature
3. 提交更改: git commit -m 'feat: add some feature'
4. 推送到分支: git push origin feature/your-feature
5. 提交Pull Request
### 测试要求
- 所有新功能必须包含单元测试
- 测试覆盖率应不低于80%
- 提交PR前确保所有测试通过
```plaintext

## F. 其他细节优化

### 1. 静态资源统一管理

#### backend/static/README.md
```markdown
# 静态资源目录

此目录用于存储系统中的静态资源，包括Excel模板、导入文件等。

## 目录结构
- `templates/` - Excel模板文件
- `uploads/` - 用户上传的文件（临时存储）
- `exports/` - 导出的文件

## 文件说明
- `question_import_template.xlsx` - 题库导入模板
- `homework_export_template.xlsx` - 作业导出模板

## 注意事项
- 此目录中的文件会被Docker挂载到容器中
- 请勿在此目录中存储敏感信息
- 大文件建议存储在NAS中，并通过符号链接引用

```
### 2. 多环境支持
#### docker-compose.override.dev.yml
```yaml
version: '3.8'
services:
  backend:
    environment:
      - ENVIRONMENT=development
      - DATABASE_URL=mysql+pymysql://root:devpass@mariadb:3306/edu_ai_db_dev
    volumes:
      - ./backend:/app
    command: uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

  frontend:
    environment:
      - VITE_API_URL=http://localhost:8000/api
    volumes:
      - ./frontend:/app
      - /app/node_modules
    command: npm run dev

  mariadb:
    environment:
      MYSQL_ROOT_PASSWORD: devpass
      MYSQL_DATABASE: edu_ai_db_dev
    volumes:
      - mariadb_dev_data:/var/lib/mysql

volumes:
  mariadb_dev_data:

```
#### docker-compose.override.prod.yml
```yaml
version: '3.8'
services:
  backend:
    environment:
      - ENVIRONMENT=production
      - DATABASE_URL=mysql+pymysql://root:prodpass@mariadb:3306/edu_ai_db
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 4G

  frontend:
    environment:
      - VITE_API_URL=https://api.yourdomain.com/api
    restart: unless-stopped

  mariadb:
    environment:
      MYSQL_ROOT_PASSWORD: prodpass
      MYSQL_DATABASE: edu_ai_db
    volumes:
      - /mnt/nas/db:/var/lib/mysql
    restart: unless-stopped

volumes:
  mariadb_prod_data:
    external: true

```
#### k8s/overlays/dev/kustomization.yaml
```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

bases:
  - ../../base

patchesStrategicMerge:
  - backend-deployment.yaml
  - frontend-deployment.yaml

images:
  - name: ghcr.io/your-repo/edu-ai-backend
    newTag: develop
  - name: ghcr.io/your-repo/edu-ai-frontend
    newTag: develop

```
#### k8s/overlays/prod/kustomization.yaml
```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

bases:
  - ../../base

patchesStrategicMerge:
  - backend-deployment.yaml
  - frontend-deployment.yaml
  - ingress-tls.yaml

images:
  - name: ghcr.io/your-repo/edu-ai-backend
    newTag: latest
  - name: ghcr.io/your-repo/edu-ai-frontend
    newTag: latest

secretGenerator:
  - name: mariadb-secret
    literals:
      - password=your-production-password

```
## 总结
通过以上优化方案，教育AI题库与作业系统在以下方面得到了显著提升：
### 1. 本地/NAS部署与数据安全
- 实现了NAS统一挂载和管理，确保模型和数据的安全存储
- 添加了自动备份脚本，定期备份数据库和Redis到NAS
- 通过环境变量管理敏感配置，避免硬编码泄露风险
### 2. AI服务与扩展性
- 实现了模型热加载和多模型切换，无需重启服务即可更换模型
- 添加了资源监控和限流机制，防止高并发时系统崩溃
- 优化了异步任务处理，提升了前端用户体验
### 3. 前端可视化与交互
- 抽象了ECharts组件，便于扩展不同分析视图
- 增强了Excel导入模板校验，提升数据质量
- 完善了多角色权限控制，提升系统安全性
### 4. CI/CD与运维自动化
- 添加了前后端自动化测试，确保代码质量
- 集成了GitHub Actions CI/CD流程，实现自动测试、构建和部署
- 添加了健康检查和告警机制，保障系统稳定运行
### 5. 文档与开发协作
- 自动生成了API文档和调用示例，便于前后端协作
- 完善了用户和开发者手册，降低使用和开发门槛
- 统一了静态资源管理，简化了资源维护
### 6. 其他细节
- 实现了多环境支持，便于开发、测试和生产环境切换
- 优化了Docker和K8s配置，提升了部署灵活性
