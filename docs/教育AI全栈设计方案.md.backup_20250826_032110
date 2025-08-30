# 教育AI题库与作业系统完整实现方案
## 项目结构总览
```plaintext
edu-ai-question-bank/
├── backend/
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── ai.py              # AI批改相关API
│   │   ├── homework.py        # 作业相关API
│   │   └── question.py       # 题库相关API
│   ├── migrations/
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions/
│   │       └── 20250101_init.py
│   ├── static/
│   │   └── question_import_template.xlsx
│   ├── __init__.py
│   ├── auth.py               # JWT认证
│   ├── celery_worker.py      # Celery异步任务
│   ├── database.py           # 数据库连接
│   ├── main.py               # FastAPI入口
│   ├── models.py             # 数据库模型
│   ├── requirements.txt      # Python依赖
│   └── Dockerfile            # 后端Dockerfile
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── api/
│   │   │   └── index.js      # axios封装
│   │   ├── assets/
│   │   ├── components/
│   │   │   ├── ExcelImport.vue
│   │   │   ├── HomeworkList.vue
│   │   │   ├── HomeworkReview.vue
│   │   │   └── QuestionTable.vue
│   │   ├── router/
│   │   │   └── index.js      # 路由配置
│   │   ├── store/
│   │   │   └── index.js      # Pinia状态管理
│   │   ├── views/
│   │   │   ├── AdminPanel.vue
│   │   │   ├── Home.vue
│   │   │   ├── Login.vue
│   │   │   ├── StudentDashboard.vue
│   │   │   ├── TeacherDashboard.vue
│   │   │   └── Register.vue
│   │   ├── App.vue
│   │   └── main.js
│   ├── package.json
│   ├── vite.config.js
│   └── Dockerfile            # 前端Dockerfile
├── k8s/
│   ├── edu-ai-backend-deployment.yaml
│   ├── edu-ai-backend-service.yaml
│   ├── edu-ai-ingress.yaml
│   └── redis-deployment.yaml
├── docker-compose.yml         # 本地开发环境
└── README.md                 # 项目说明

```
## 技术栈
### 前端技术栈
- 框架: Vue 3
- 组件库: Element Plus
- 状态管理: Pinia
- 路由: Vue Router
- 构建工具: Vite
- HTTP客户端: Axios
- 可视化: ECharts (用于数据分析)
### 后端技术栈
- 框架: FastAPI
- ORM: SQLAlchemy
- 数据库迁移: Alembic
- 异步任务: Celery + Redis
- AI服务: Hugging Face Transformers
- 认证: JWT
- 文档: OpenAPI (Swagger)
### 基础设施
- 数据库: MariaDB
- 缓存: Redis
- 容器化: Docker
- 编排: Kubernetes
- 网关: Nginx Ingress Controller
## 核心文件实现
### 1. 后端核心文件
#### backend/main.py
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.controllers import ai, homework, question
from backend.database import engine
from backend.models import Base

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

# 注册路由
app.include_router(question.router, prefix="/api/questions", tags=["题库管理"])
app.include_router(homework.router, prefix="/api/homework", tags=["作业管理"])
app.include_router(ai.router, prefix="/api/ai", tags=["AI服务"])

@app.get("/")
def read_root():
    return {"message": "教育AI题库系统 API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

```
#### backend/models.py
```python
from sqlalchemy import Column, Integer, String, Text, Enum, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import declarative_base, relationship
import enum

Base = declarative_base()

class Difficulty(enum.Enum):
    easy = '易'
    medium = '中'
    hard = '难'
    olympiad = '奥数'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    password_hash = Column(String(255))
    name = Column(String(100))
    role = Column(Enum('student','teacher','admin','parent'))
    register_time = Column(DateTime)

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(255))

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    type_id = Column(Integer)
    content = Column(Text)
    option_a = Column(String(255))
    option_b = Column(String(255))
    option_c = Column(String(255))
    option_d = Column(String(255))
    answer = Column(String(255))
    explanation = Column(Text)
    knowledge_point = Column(String(255))
    difficulty = Column(Enum(Difficulty))
    tags = Column(String(255))
    image_url = Column(String(255))
    extra_json = Column(Text)
    created_by = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    subject = relationship("Subject")
    creator = relationship("User")

class StudentAnswer(Base):
    __tablename__ = 'student_answers'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    student_id = Column(Integer, ForeignKey('users.id'))
    answer = Column(Text)
    score = Column(DECIMAL(5,2))
    ai_explanation = Column(Text)
    answer_image_url = Column(String(255))
    submit_time = Column(DateTime)

class Homework(Base):
    __tablename__ = 'homework'
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String(255))
    publish_time = Column(DateTime)

class HomeworkAssignment(Base):
    __tablename__ = 'homework_assignments'
    id = Column(Integer, primary_key=True)
    homework_id = Column(Integer, ForeignKey('homework.id'))
    student_id = Column(Integer, ForeignKey('users.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    answer = Column(Text)
    score = Column(DECIMAL(5,2))
    comment = Column(Text)
    ai_explanation = Column(Text)
    submit_time = Column(DateTime)
    review_time = Column(DateTime)

```
#### backend/controllers/question.py
```python
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Response
from sqlalchemy.orm import Session
from backend.models import Question, User
from backend.database import get_db
from backend.auth import get_current_user
import pandas as pd
import datetime
import os

router = APIRouter()

@router.get("/")
def get_questions(subject_id: int = None, db: Session = Depends(get_db)):
    query = db.query(Question)
    if subject_id:
        query = query.filter(Question.subject_id == subject_id)
    return {"items": [q.to_dict() for q in query.limit(100)]}

@router.post("/", dependencies=[Depends(get_current_user)])
def create_question(q: dict, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    nq = Question(**q, created_by=user.id, created_at=datetime.datetime.now())
    db.add(nq)
    db.commit()
    return {"msg": "题目已创建", "id": nq.id}

@router.post("/import-excel", dependencies=[Depends(get_current_user)])
async def import_excel(file: UploadFile = File(...), db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    df = pd.read_excel(file.file)
    for _, row in df.iterrows():
        nq = Question(
            content=row['题干'],
            subject_id=row['学科ID'],
            difficulty=row['难度'],
            tags=row.get('标签',''),
            option_a=row.get('option_a',''),
            option_b=row.get('option_b',''),
            option_c=row.get('option_c',''),
            option_d=row.get('option_d',''),
            answer=row.get('answer',''),
            explanation=row.get('解析',''),
            image_url=row.get('image_url',''),
            extra_json=row.get('extra_json',None),
            created_by=user.id,
            created_at=datetime.datetime.now()
        )
        db.add(nq)
    db.commit()
    return {"msg": "Excel导入成功"}

@router.get("/excel-template")
def download_excel_template():
    template_path = "static/question_import_template.xlsx"
    if not os.path.exists(template_path):
        # 创建模板文件
        import pandas as pd
        df = pd.DataFrame([{
            "题干": "勾股定理是什么",
            "学科ID": 1,
            "难度": "奥数",
            "标签": "数学",
            "option_a": "",
            "option_b": "",
            "option_c": "",
            "option_d": "",
            "answer": "",
            "解析": "a^2+b^2=c^2",
            "image_url": "http://xxx",
            "extra_json": '{"latex":"a^2+b^2=c^2"}'
        }])
        os.makedirs("static", exist_ok=True)
        df.to_excel(template_path, index=False)
    return Response(content=open(template_path, "rb").read(), 
                   media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

```
#### backend/controllers/ai.py
```python
from fastapi import APIRouter, Depends, BackgroundTasks
from backend.auth import get_current_user
from backend.celery_worker import grade_answer
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import StudentAnswer, User
import datetime

router = APIRouter()

@router.post("/grade")
def ai_grade(payload: dict, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    task = grade_answer.apply_async(args=(payload.get('model', 'gemma-3-270m'), payload['question'], payload['answer']))
    # 保存答题记录，状态pending
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
    return {"task_id": task.id}

@router.get("/grade-result/{task_id}")
def get_grade_result(task_id: str):
    from backend.celery_worker import grade_answer
    task = grade_answer.AsyncResult(task_id)
    if not task.ready():
        return {"status": "pending"}
    return {"status": "done", "result": task.result}

```
#### backend/celery_worker.py
```python
from celery import Celery
from transformers import AutoModelForCausalLM, AutoTokenizer

celery_app = Celery('ai_tasks', broker='redis://redis:6379/0')

MODEL_CACHE = {}

def load_model(model_name):
    if model_name not in MODEL_CACHE:
        path = f"/mnt/nas/models/{model_name}"
        tokenizer = AutoTokenizer.from_pretrained(path)
        model = AutoModelForCausalLM.from_pretrained(path)
        MODEL_CACHE[model_name] = (tokenizer, model)
    return MODEL_CACHE[model_name]

@celery_app.task
def grade_answer(model_name, question, answer):
    tokenizer, model = load_model(model_name)
    prompt = f"题目：{question}\n学生答案：{answer}\n请判断正误并给出解析："
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=128)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result

```
#### backend/auth.py
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import User
import datetime

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user

```
### 2. 前端核心文件
#### frontend/src/main.js
```javascript
import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(ElementPlus)
app.use(createPinia())
app.use(router)
app.mount('#app')

```
#### frontend/src/router/index.js
```javascript
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import StudentDashboard from '../views/StudentDashboard.vue'
import TeacherDashboard from '../views/TeacherDashboard.vue'
import AdminPanel from '../views/AdminPanel.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/login', component: Login },
  { 
    path: '/student', 
    component: StudentDashboard, 
    meta: { requiresAuth: true, role: 'student' } 
  },
  { 
    path: '/teacher', 
    component: TeacherDashboard, 
    meta: { requiresAuth: true, role: 'teacher' } 
  },
  { 
    path: '/admin', 
    component: AdminPanel, 
    meta: { requiresAuth: true, role: 'admin' } 
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  const role = localStorage.getItem('role')
  
  if (to.meta.requiresAuth) {
    if (!token) {
      next('/login')
    } else if (to.meta.role && to.meta.role !== role) {
      next('/login')
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router

```
#### frontend/src/views/TeacherDashboard.vue
```plaintext
<template>
  <div class="teacher-dashboard">
    <h1>教师控制台</h1>
    <el-tabs v-model="activeTab">
      <el-tab-pane label="题库管理" name="questions">
        <QuestionTable @importExcel="showImport = true" />
        <ExcelImport v-if="showImport" @close="showImport = false" />
      </el-tab-pane>
      <el-tab-pane label="作业管理" name="homework">
        <HomeworkList />
      </el-tab-pane>
      <el-tab-pane label="作业批改" name="review">
        <HomeworkReview />
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import QuestionTable from '@/components/QuestionTable.vue'
import ExcelImport from '@/components/ExcelImport.vue'
import HomeworkList from '@/components/HomeworkList.vue'
import HomeworkReview from '@/components/HomeworkReview.vue'

const activeTab = ref('questions')
const showImport = ref(false)
</script>

<style scoped>
.teacher-dashboard {
  padding: 20px;
}
</style>

```
#### frontend/src/components/QuestionTable.vue
```plaintext
<template>
  <div class="question-table">
    <div class="actions">
      <el-button type="primary" @click="$emit('importExcel')">Excel导入</el-button>
    </div>
    
    <el-table :data="questions" style="width: 100%">
      <el-table-column prop="content" label="题干" />
      <el-table-column prop="difficulty" label="难度" />
      <el-table-column prop="tags" label="标签" />
      <el-table-column label="操作">
        <template #default="scope">
          <el-button @click="viewQuestion(scope.row)">查看</el-button>
        </template>
      </el-table-column>
    </el-table>
    
    <el-dialog v-model="dialogVisible" title="题目详情" width="50%">
      <div v-if="selectedQuestion">
        <p><strong>题干:</strong> {{ selectedQuestion.content }}</p>
        <p v-if="selectedQuestion.image_url">
          <img :src="selectedQuestion.image_url" style="max-width: 300px;" />
        </p>
        <p><strong>难度:</strong> {{ selectedQuestion.difficulty }}</p>
        <p><strong>标签:</strong> {{ selectedQuestion.tags }}</p>
        <p><strong>解析:</strong> {{ selectedQuestion.explanation }}</p>
      </div>
      <template #footer>
        <el-button @click="dialogVisible = false">关闭</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '@/api'

const questions = ref([])
const dialogVisible = ref(false)
const selectedQuestion = ref(null)

const emit = defineEmits(['importExcel'])

onMounted(async () => {
  try {
    const response = await axios.get('/questions')
    questions.value = response.data.items
  } catch (error) {
    console.error('获取题库失败:', error)
  }
})

const viewQuestion = (question) => {
  selectedQuestion.value = question
  dialogVisible.value = true
}
</script>

<style scoped>
.question-table {
  margin-top: 20px;
}
.actions {
  margin-bottom: 20px;
}
</style>

```
#### frontend/src/components/ExcelImport.vue
```plaintext
<template>
  <div class="excel-import">
    <el-card>
      <h2>题库Excel导入</h2>
      <div class="template-download">
        <el-link :href="templateUrl" target="_blank">下载Excel模板</el-link>
      </div>
      
      <el-upload
        class="upload-demo"
        :action="uploadUrl"
        :headers="{ Authorization: 'Bearer ' + token }"
        :on-success="handleSuccess"
        :on-error="handleError"
        :file-list="fileList"
        accept=".xlsx, .xls"
      >
        <el-button type="primary">点击上传</el-button>
        <template #tip>
          <div class="el-upload__tip">
            只能上传xlsx/xls文件，且不超过10MB
          </div>
        </template>
      </el-upload>
      
      <el-alert
        v-if="message"
        :title="message"
        :type="messageType"
        show-icon
        style="margin-top: 20px;"
      />
      
      <div class="actions">
        <el-button @click="$emit('close')">关闭</el-button>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from '@/api'

const emit = defineEmits(['close'])

const token = localStorage.getItem('token')
const templateUrl = '/api/questions/excel-template'
const uploadUrl = '/api/questions/import-excel'
const fileList = ref([])
const message = ref('')
const messageType = ref('success')

const handleSuccess = (response) => {
  message.value = response.msg || '导入成功'
  messageType.value = 'success'
  fileList.value = []
}

const handleError = (error) => {
  message.value = '导入失败'
  messageType.value = 'error'
  console.error('导入错误:', error)
}
</script>

<style scoped>
.excel-import {
  margin-top: 20px;
}
.template-download {
  margin-bottom: 20px;
}
.actions {
  margin-top: 20px;
  text-align: right;
}
</style>

```
#### frontend/src/components/HomeworkReview.vue
```plaintext
<template>
  <div class="homework-review">
    <h2>作业批改</h2>
    
    <el-table :data="assignments" style="width: 100%">
      <el-table-column prop="studentName" label="学生" />
      <el-table-column prop="question" label="题目" />
      <el-table-column prop="answer" label="学生答案" />
      <el-table-column prop="ai_explanation" label="AI解析" />
      <el-table-column label="评分">
        <template #default="scope">
          <el-input-number 
            v-model="scope.row.score" 
            :min="0" 
            :max="100" 
            :precision="1"
          />
        </template>
      </el-table-column>
      <el-table-column label="批语">
        <template #default="scope">
          <el-input v-model="scope.row.comment" />
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template #default="scope">
          <el-button 
            type="primary" 
            @click="submitReview(scope.row)"
            :disabled="scope.row.submitted"
          >
            {{ scope.row.submitted ? '已提交' : '提交' }}
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '@/api'

const assignments = ref([])

onMounted(async () => {
  try {
    const response = await axios.get('/homework/review-list')
    assignments.value = response.data.items
  } catch (error) {
    console.error('获取作业列表失败:', error)
  }
})

const submitReview = async (assignment) => {
  try {
    await axios.post('/homework/review', {
      id: assignment.id,
      score: assignment.score,
      comment: assignment.comment
    })
    
    assignment.submitted = true
    ElMessage.success('批改成功')
  } catch (error) {
    console.error('提交批改失败:', error)
    ElMessage.error('提交失败')
  }
}
</script>

<style scoped>
.homework-review {
  margin-top: 20px;
}
</style>

```
#### frontend/src/api/index.js
```javascript
import axios from 'axios'
import { ElMessage } from 'element-plus'

const api = axios.create({
  baseURL: '/api', // 配置代理
  timeout: 10000
})

// 请求拦截器
api.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

// 响应拦截器
api.interceptors.response.use(
  response => {
    return response.data
  },
  error => {
    if (error.response && error.response.status === 401) {
      localStorage.removeItem('token')
      localStorage.removeItem('role')
      window.location.href = '/login'
      ElMessage.error('登录已过期，请重新登录')
    }
    return Promise.reject(error)
  }
)

export default api

```
### 3. 部署配置文件
#### docker-compose.yml
```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    container_name: edu-ai-backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db
      - CELERY_BROKER_URL=redis://redis:6379/0
    volumes:
      - /mnt/nas/models:/mnt/nas/models
    depends_on:
      - mariadb
      - redis

  frontend:
    build: ./frontend
    container_name: edu-ai-frontend
    ports:
      - "5173:80"
    depends_on:
      - backend

  mariadb:
    image: mariadb:10.6
    container_name: edu-ai-mariadb
    environment:
      MYSQL_ROOT_PASSWORD: yourpassword
      MYSQL_DATABASE: edu_ai_db
    volumes:
      - /mnt/nas/db:/var/lib/mysql
    ports:
      - "3306:3306"

  redis:
    image: redis:6-alpine
    container_name: edu-ai-redis
    ports:
      - "6379:6379"

  celery:
    build: 
      context: ./backend
      dockerfile: Dockerfile.celery
    container_name: edu-ai-celery
    environment:
      - DATABASE_URL=mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db
      - CELERY_BROKER_URL=redis://redis:6379/0
    volumes:
      - /mnt/nas/models:/mnt/nas/models
    depends_on:
      - mariadb
      - redis

```
#### k8s/edu-ai-ingress.yaml
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: edu-ai-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /$2
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  tls:
  - hosts:
    - ai.yourdomain.com
    secretName: edu-ai-tls
  rules:
  - host: ai.yourdomain.com
    http:
      paths:
      - path: /api(/|$)(.*)
        pathType: Prefix
        backend:
          service:
            name: edu-ai-backend-service
            port:
              number: 8000
      - path: /()(.*)
        pathType: Prefix
        backend:
          service:
            name: edu-ai-frontend-service
            port:
              number: 80

```
#### k8s/edu-ai-backend-deployment.yaml
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
        image: yourrepo/edu-ai-backend:latest
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
      volumes:
      - name: nas-models
        persistentVolumeClaim:
          claimName: nas-models-pvc

```
## API接口文档
### 认证接口
#### POST /api/auth/login
- 描述: 用户登录获取JWT令牌
- 请求体:
    ```json
{
  "username": "string",
  "password": "string"
}

```
- 响应:
    ```json
{
  "token": "jwt_token",
  "role": "student|teacher|admin"
}

```
### 题库管理接口
#### GET /api/questions
- 描述: 获取题库列表
- 查询参数:
    - subject_id (可选): 学科ID
    - keyword (可选): 关键词搜索
- 响应:
    ```json
{
  "items": [
    {
      "id": 1,
      "content": "题干内容",
      "difficulty": "易",
      "tags": "数学,代数",
      "image_url": "http://example.com/image.png"
    }
  ]
}

```
#### POST /api/questions
- 描述: 创建新题目
- 请求体:
    ```json
{
  "content": "题干内容",
  "subject_id": 1,
  "difficulty": "中",
  "tags": "数学",
  "option_a": "选项A",
  "option_b": "选项B",
  "option_c": "选项C",
  "option_d": "选项D",
  "answer": "A",
  "explanation": "解析内容",
  "image_url": "http://example.com/image.png",
  "extra_json": "{\"latex\":\"a^2+b^2=c^2\"}"
}

```
- 响应:
    ```json
{
  "msg": "题目已创建",
  "id": 1
}

```
#### POST /api/questions/import-excel
- 描述: Excel文件导入题库
- 请求体: 文件上传 (multipart/form-data)
- 响应:
    ```json
{
  "msg": "Excel导入成功"
}

```
#### GET /api/questions/excel-template
- 描述: 下载Excel导入模板
- 响应: Excel文件
### 作业管理接口
#### GET /api/homework/list
- 描述: 获取教师作业列表
- 响应:
    ```json
{
  "items": [
    {
      "id": 1,
      "title": "数学作业1",
      "publish_time": "2023-01-01 10:00:00"
    }
  ]
}

```
#### GET /api/homework/review-list
- 描述: 获取待批改作业列表
- 响应:
    ```json
{
  "items": [
    {
      "id": 1,
      "studentName": "张三",
      "question": "题目内容",
      "answer": "学生答案",
      "ai_explanation": "AI解析结果",
      "score": null,
      "comment": ""
    }
  ]
}

```
#### POST /api/homework/review
- 描述: 提交作业批改结果
- 请求体:
    ```json
{
  "id": 1,
  "score": 85.5,
  "comment": "解答正确，但格式不够规范"
}

```
- 响应:
    ```json
{
  "msg": "批改成功"
}

```
### AI服务接口
#### POST /api/ai/grade
- 描述: 提交AI批改任务
- 请求体:
    ```json
{
  "question": "题目内容",
  "answer": "学生答案",
  "model": "gemma-3-270m",
  "question_id": 1
}

```
- 响应:
    ```json
{
  "task_id": "task-uuid"
}

```
#### GET /api/ai/grade-result/{task_id}
- 描述: 获取AI批改结果
- 响应:
    ```json
{
  "status": "done",
  "result": "AI批改结果和解析"
}

```
## 开发者文档
### 系统架构
教育AI题库系统采用前后端分离架构，包含以下核心组件：
1. 前端: Vue3 + Element Plus构建的单页应用，负责用户交互和界面展示
2. 后端: FastAPI提供RESTful API，处理业务逻辑和数据操作
3. 数据库: MariaDB存储题库、用户、作业等数据
4. AI服务: 本地部署的Hugging Face模型，通过Celery异步处理批改任务
5. 缓存: Redis用于Celery消息队列和会话存储
6. 部署: Docker容器化，Kubernetes编排，Nginx作为入口网关
### 开发环境搭建
#### 后端开发环境
1. 安装Python 3.10+
2. 创建虚拟环境: python -m venv venv
3. 激活虚拟环境: source venv/bin/activate
4. 安装依赖: pip install -r backend/requirements.txt
5. 配置数据库: 修改backend/database.py中的连接字符串
6. 运行数据库迁移: alembic upgrade head
7. 启动后端服务: uvicorn backend.main:app --reload
#### 前端开发环境
1. 安装Node.js 16+
2. 进入前端目录: cd frontend
3. 安装依赖: npm install
4. 启动开发服务器: npm run dev
#### 完整环境启动
1. 确保Docker已安装
2. 运行: docker-compose up -d
3. 访问: http://localhost:5173
### 数据库设计
系统包含以下核心表：
1. users: 用户表（学生、教师、管理员）
2. subjects: 学科表
3. questions: 题目表（支持多种题型和难度）
4. student_answers: 学生答题记录
5. homework: 作业表
6. homework_assignments: 作业分配表
详细表结构请参考backend/models.py。
### AI批改流程
1. 学生提交答案后，前端调用/api/ai/grade接口
2. 后端创建Celery任务，将任务放入Redis队列
3. Celery worker从队列获取任务
4. 加载指定的AI模型（如Gemma、Llama）
5. 构造提示词，调用模型生成批改结果
6. 将结果存入数据库，更新任务状态
7. 前端轮询/api/ai/grade-result/{task_id}获取结果
### Excel导入流程
1. 教师下载Excel模板（包含示例数据）
2. 填写题目信息（支持多题型、多学科）
3. 上传Excel文件到/api/questions/import-excel
4. 后端使用pandas解析Excel文件
5. 验证数据格式和完整性
6. 将题目批量插入数据库
7. 返回导入结果
### 权限管理
系统基于角色实现访问控制：
- 学生: 查看题目、提交作业、查看成绩
- 教师: 管理题库、布置作业、批改作业
- 管理员: 用户管理、系统配置
权限控制通过以下机制实现：
1. JWT认证：所有API请求需携带有效令牌
2. 路由守卫：前端根据用户角色控制页面访问
3. 后端权限检查：API接口验证用户权限
### 部署说明
#### 本地部署
1. 克隆项目代码
2. 配置环境变量（数据库连接、模型路径等）
3. 运行docker-compose up -d
4. 访问http://localhost:5173
#### Kubernetes部署
1. 准备Kubernetes集群
2. 配置NAS存储（模型、数据库）
3. 应用K8s配置:
    ```bash
kubectl apply -f k8s/

```
4. 配置DNS解析到Ingress IP
### 性能优化建议
1. 模型加载优化:
    - 使用全局缓存避免重复加载
    - 预加载常用模型到内存
    - 考虑模型量化减少内存占用
2. 数据库优化:
    - 添加适当索引（题目内容、学科ID等）
    - 使用连接池管理数据库连接
    - 考虑读写分离
3. 前端优化:
    - 路由懒加载减少初始包大小
    - 使用虚拟滚动处理大量数据
    - 图片懒加载和压缩
4. 异步处理:
    - 使用Celery处理耗时任务（如AI批改）
    - 实现任务队列优先级
    - 监控任务执行状态
### 故障排查
1. AI模型加载失败:
    - 检查模型文件路径是否正确
    - 确认NAS挂载是否成功
    - 查看Celery worker日志
2. 数据库连接问题:
    - 验证数据库服务状态
    - 检查连接字符串配置
    - 确认网络连通性
3. 前端页面加载缓慢:
    - 检查API响应时间
    - 分析网络请求
    - 查看浏览器控制台错误
4. Excel导入失败:
    - 验证文件格式是否正确
    - 检查字段名称与模板是否一致
    - 查看后端错误日志
### 扩展功能建议
1. 多模态支持:
    - 添加图片题目OCR识别
    - 支持语音答案转录
    - 集成公式识别
2. 高级分析:
    - 学生能力画像
    - 知识点掌握度分析
    - 学习路径推荐
3. 协作功能:
    - 教师共享题库
    - 协同批改
    - 教研组管理
4. 移动端适配:
    - 响应式设计优化
    - 开发移动App
    - 离线功能支持
## 结语
本教育AI题库与作业系统提供了完整的解决方案，涵盖题库管理、作业布置、AI批改等核心功能。系统采用现代化技术栈，支持本地部署和云原生架构，具有良好的可扩展性和维护性。
通过本系统，教师可以高效管理题库、布置作业和批改学生答案；学生可以便捷地完成作业并获得即时反馈；管理员可以灵活配置系统并监控运行状态。AI批改功能显著减轻了教师的工作负担，同时为学生提供个性化的学习指导。
系统设计充分考虑了教育场景的特殊需求，包括数据安全、权限控制、多题型支持等，适合各类教育机构部署使用。
[教育AI题库与作业系统UI设计方案](https://docs.qq.com/aio/DWFh4TFFvU2diYnpv?p=pS6rJzr2QglMQ6SnM46B0d)
    > 前端实现统一的UI设计方案，包括响应交互、视觉效果、动画翻页、弹窗动画、组件导航等。我们将使用Vue3和Element Plus，并添加一些自定义样式和动画效果。
    主要改进点：
    1. 统一的配色方案和主题
    1. 过渡动画和微交互
    1. 弹窗动画效果
    1. 翻页动画
    1. 组件导航的视觉优化
    1. 响应式设计
    下面是具体的实现方案和代码：
    ### 1. 全局样式和主题
    首先，我们定义全局的主题样式，包括颜色、字体、间距等。
    #### frontend/src/styles/theme.css
    ```plaintext
:root {
  /* 主题颜色 */
  --primary-color: #409EFF;
  --primary-light: #ecf5ff;
  --primary-dark: #337ecc;
  
  --success-color: #67C23A;
  --success-light: #f0f9eb;
  --success-dark: #529b2e;
  
  --warning-color: #E6A23C;
  --warning-light: #fdf6ec;
  --warning-dark: #b88230;
  
  --danger-color: #F56C6C;
  --danger-light: #fef0f0;
  --danger-dark: #c45656;
  
  --info-color: #909399;
  --info-light: #f4f4f5;
  --info-dark: #73767a;
  
  /* 文字颜色 */
  --text-primary: #303133;
  --text-regular: #606266;
  --text-secondary: #909399;
  --text-placeholder: #c0c4cc;
  
  /* 边框颜色 */
  --border-light: #e4e7ed;
  --border-base: #dcdfe6;
  --border-dark: #d4d7de;
  
  /* 背景颜色 */
  --background-color: #f5f7fa;
  --background-white: #ffffff;
  
  /* 字体 */
  --font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  
  /* 圆角 */
  --border-radius-small: 2px;
  --border-radius-base: 4px;
  --border-radius-large: 8px;
  --border-radius-circle: 50%;
  
  /* 阴影 */
  --box-shadow-light: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  --box-shadow-base: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  --box-shadow-dark: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .12);
  
  /* 过渡 */
  --transition-all: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-transform: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-opacity: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

body {
  font-family: var(--font-family);
  color: var(--text-primary);
  background-color: var(--background-color);
  margin: 0;
  padding: 0;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* 滚动条样式 */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-thumb {
  background: var(--border-base);
  border-radius: var(--border-radius-base);
}

::-webkit-scrollbar-track {
  background: var(--background-color);
}

/* 通用动画类 */
.fade-enter-active,
.fade-leave-active {
  transition: var(--transition-opacity);
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.3s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(10px);
  opacity: 0;
}

/* 卡片通用样式 */
.custom-card {
  background: var(--background-white);
  border-radius: var(--border-radius-large);
  box-shadow: var(--box-shadow-light);
  padding: 20px;
  margin-bottom: 20px;
  transition: var(--transition-all);
}

.custom-card:hover {
  box-shadow: var(--box-shadow-base);
  transform: translateY(-2px);
}

/* 按钮通用样式 */
.custom-button {
  transition: var(--transition-all);
  border-radius: var(--border-radius-base);
}

.custom-button:hover {
  transform: translateY(-2px);
  box-shadow: var(--box-shadow-base);
}

/* 表格通用样式 */
.custom-table {
  border-radius: var(--border-radius-base);
  overflow: hidden;
}

.custom-table .el-table__header {
  background-color: var(--primary-light);
}

.custom-table .el-table__header th {
  background-color: var(--primary-light);
  color: var(--primary-dark);
  font-weight: 600;
}

/* 弹窗动画 */
.dialog-fade-enter-active {
  animation: dialog-fade-in 0.3s;
}

.dialog-fade-leave-active {
  animation: dialog-fade-out 0.3s;
}

@keyframes dialog-fade-in {
  0% {
    transform: translate3d(0, -20px, 0);
    opacity: 0;
  }
  100% {
    transform: translate3d(0, 0, 0);
    opacity: 1;
  }
}

@keyframes dialog-fade-out {
  0% {
    transform: translate3d(0, 0, 0);
    opacity: 1;
  }
  100% {
    transform: translate3d(0, -20px, 0);
    opacity: 0;
  }
}

/* 翻页动画 */
.page-fade-enter-active,
.page-fade-leave-active {
  transition: var(--transition-opacity);
}

.page-fade-enter-from,
.page-fade-leave-to {
  opacity: 0;
}

/* 组件导航 */
.nav-item {
  position: relative;
  padding: 0 15px;
  height: 100%;
  display: flex;
  align-items: center;
  transition: var(--transition-all);
}

.nav-item::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 3px;
  background-color: var(--primary-color);
  transform: translateX(-50%);
  transition: width 0.3s;
}

.nav-item:hover::after,
.nav-item.active::after {
  width: 80%;
}

.nav-item:hover {
  color: var(--primary-color);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .custom-card {
    padding: 15px;
    margin-bottom: 15px;
  }
  
  .nav-item {
    padding: 0 10px;
  }
}
```
    ### 2. 修改App.vue引入全局样式
    #### frontend/src/App.vue
    ```plaintext
<template>
  <div id="app">
    <router-view v-slot="{ Component }">
      <transition name="page-fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </div>
</template>

<script setup>
// 引入全局样式
import './styles/theme.css'
</script>

<style>
#app {
  font-family: var(--font-family);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--text-primary);
  background-color: var(--background-color);
  min-height: 100vh;
}
</style>
```
    ### 3. 优化组件导航
    #### frontend/src/components/CustomNav.vue
    ```plaintext
<template>
  <nav class="custom-nav">
    <div class="nav-container">
      <div class="nav-logo">
        <img src="@/assets/logo.png" alt="Logo" class="logo" />
        <span class="logo-text">教育AI题库系统</span>
      </div>
      <div class="nav-menu">
        <div 
          v-for="item in menuItems" 
          :key="item.path" 
          class="nav-item" 
          :class="{ active: currentPath === item.path }"
          @click="navigateTo(item.path)"
        >
          {{ item.title }}
        </div>
      </div>
      <div class="nav-user">
        <el-dropdown v-if="user" trigger="click">
          <div class="user-info">
            <el-avatar :size="32" :src="user.avatar || defaultAvatar" />
            <span class="username">{{ user.name || user.username }}</span>
          </div>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="goToProfile">个人中心</el-dropdown-item>
              <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
        <el-button v-else type="primary" @click="goToLogin">登录</el-button>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/store'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()

const currentPath = computed(() => route.path)
const user = computed(() => userStore.user)
const defaultAvatar = 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'

const menuItems = [
  { title: '首页', path: '/' },
  { title: '题库', path: '/questions' },
  { title: '作业', path: '/homework' },
  { title: '关于', path: '/about' }
]

const navigateTo = (path) => {
  router.push(path)
}

const goToLogin = () => {
  router.push('/login')
}

const goToProfile = () => {
  router.push('/profile')
}

const logout = () => {
  userStore.logout()
  router.push('/login')
}
</script>

<style scoped>
.custom-nav {
  background: var(--background-white);
  box-shadow: var(--box-shadow-light);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 60px;
  padding: 0 20px;
}

.nav-logo {
  display: flex;
  align-items: center;
}

.logo {
  height: 32px;
  margin-right: 10px;
}

.logo-text {
  font-size: 18px;
  font-weight: 600;
  color: var(--primary-color);
}

.nav-menu {
  display: flex;
  height: 100%;
}

.nav-user {
  display: flex;
  align-items: center;
}

.user-info {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.username {
  margin-left: 10px;
  font-size: 14px;
  color: var(--text-regular);
}

@media (max-width: 768px) {
  .logo-text {
    display: none;
  }
  
  .nav-menu {
    display: none;
  }
}
</style>
```
    ### 4. 优化弹窗动画
    #### frontend/src/components/CustomDialog.vue
    ```plaintext
<template>
  <el-dialog
    v-model="visible"
    :title="title"
    :width="width"
    :before-close="handleClose"
    class="custom-dialog"
    :close-on-click-modal="false"
    destroy-on-close
  >
    <div class="dialog-content">
      <slot></slot>
    </div>
    <template #footer>
      <div class="dialog-footer">
        <slot name="footer">
          <el-button @click="handleClose">取消</el-button>
          <el-button type="primary" @click="handleConfirm">确定</el-button>
        </slot>
      </div>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  modelValue: {
    type: Boolean,
    default: false
  },
  title: {
    type: String,
    default: '提示'
  },
  width: {
    type: String,
    default: '50%'
  }
})

const emit = defineEmits(['update:modelValue', 'confirm', 'cancel'])

const visible = ref(props.modelValue)

watch(() => props.modelValue, (val) => {
  visible.value = val
})

watch(visible, (val) => {
  emit('update:modelValue', val)
})

const handleClose = () => {
  visible.value = false
  emit('cancel')
}

const handleConfirm = () => {
  emit('confirm')
  visible.value = false
}
</script>

<style scoped>
.custom-dialog {
  border-radius: var(--border-radius-large);
  overflow: hidden;
}

.dialog-content {
  padding: 20px 0;
}

.dialog-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}
</style>
```
    ### 5. 优化表格组件
    #### frontend/src/components/CustomTable.vue
    ```plaintext
<template>
  <div class="custom-table-container">
    <el-table
      :data="data"
      :border="border"
      :stripe="stripe"
      :height="height"
      :max-height="maxHeight"
      :row-key="rowKey"
      :tree-props="treeProps"
      :default-expand-all="defaultExpandAll"
      :show-summary="showSummary"
      :sum-text="sumText"
      :summary-method="summaryMethod"
      :span-method="spanMethod"
      :select-on-indeterminate="selectOnIndeterminate"
      :indent="indent"
      :lazy="lazy"
      :load="load"
      @select="handleSelect"
      @select-all="handleSelectAll"
      @selection-change="handleSelectionChange"
      @cell-mouse-enter="handleCellMouseEnter"
      @cell-mouse-leave="handleCellMouseLeave"
      @cell-click="handleCellClick"
      @cell-dblclick="handleCellDblclick"
      @row-click="handleRowClick"
      @row-contextmenu="handleRowContextmenu"
      @row-dblclick="handleRowDblclick"
      @header-click="handleHeaderClick"
      @header-contextmenu="handleHeaderContextmenu"
      @sort-change="handleSortChange"
      @filter-change="handleFilterChange"
      @current-change="handleCurrentChange"
      @header-dragend="handleHeaderDragend"
      @expand-change="handleExpandChange"
      class="custom-table"
    >
      <slot></slot>
    </el-table>
    
    <div v-if="pagination" class="table-pagination">
      <el-pagination
        v-model:current-page="currentPage"
        v-model:page-size="pageSize"
        :page-sizes="pageSizes"
        :total="total"
        :layout="layout"
        :small="small"
        :background="background"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  data: {
    type: Array,
    default: () => []
  },
  border: {
    type: Boolean,
    default: true
  },
  stripe: {
    type: Boolean,
    default: true
  },
  height: [String, Number],
  maxHeight: [String, Number],
  rowKey: [String, Function],
  treeProps: {
    type: Object,
    default: () => ({})
  },
  defaultExpandAll: {
    type: Boolean,
    default: false
  },
  showSummary: {
    type: Boolean,
    default: false
  },
  sumText: {
    type: String,
    default: '合计'
  },
  summaryMethod: Function,
  spanMethod: Function,
  selectOnIndeterminate: {
    type: Boolean,
    default: true
  },
  indent: {
    type: Number,
    default: 16
  },
  lazy: {
    type: Boolean,
    default: false
  },
  load: Function,
  pagination: {
    type: Boolean,
    default: true
  },
  total: {
    type: Number,
    default: 0
  },
  pageSizes: {
    type: Array,
    default: () => [10, 20, 50, 100]
  },
  layout: {
    type: String,
    default: 'total, sizes, prev, pager, next, jumper'
  },
  small: {
    type: Boolean,
    default: false
  },
  background: {
    type: Boolean,
    default: true
  }
})

const emit = defineEmits([
  'select',
  'select-all',
  'selection-change',
  'cell-mouse-enter',
  'cell-mouse-leave',
  'cell-click',
  'cell-dblclick',
  'row-click',
  'row-contextmenu',
  'row-dblclick',
  'header-click',
  'header-contextmenu',
  'sort-change',
  'filter-change',
  'current-change',
  'header-dragend',
  'expand-change',
  'size-change',
  'update:currentPage',
  'update:pageSize'
])

const currentPage = ref(1)
const pageSize = ref(10)

const handleSelect = (selection, row) => {
  emit('select', selection, row)
}

const handleSelectAll = (selection) => {
  emit('select-all', selection)
}

const handleSelectionChange = (selection) => {
  emit('selection-change', selection)
}

const handleCellMouseEnter = (row, column, cell, event) => {
  emit('cell-mouse-enter', row, column, cell, event)
}

const handleCellMouseLeave = (row, column, cell, event) => {
  emit('cell-mouse-leave', row, column, cell, event)
}

const handleCellClick = (row, column, cell, event) => {
  emit('cell-click', row, column, cell, event)
}

const handleCellDblclick = (row, column, cell, event) => {
  emit('cell-dblclick', row, column, cell, event)
}

const handleRowClick = (row, column, event) => {
  emit('row-click', row, column, event)
}

const handleRowContextmenu = (row, column, event) => {
  emit('row-contextmenu', row, column, event)
}

const handleRowDblclick = (row, column, event) => {
  emit('row-dblclick', row, column, event)
}

const handleHeaderClick = (column, event) => {
  emit('header-click', column, event)
}

const handleHeaderContextmenu = (column, event) => {
  emit('header-contextmenu', column, event)
}

const handleSortChange = (column) => {
  emit('sort-change', column)
}

const handleFilterChange = (filters) => {
  emit('filter-change', filters)
}

const handleCurrentChange = (val) => {
  emit('current-change', val)
  emit('update:currentPage', val)
}

const handleHeaderDragend = (newWidth, oldWidth, column, event) => {
  emit('header-dragend', newWidth, oldWidth, column, event)
}

const handleExpandChange = (row, expanded) => {
  emit('expand-change', row, expanded)
}

const handleSizeChange = (val) => {
  emit('size-change', val)
  emit('update:pageSize', val)
  currentPage.value = 1
  emit('update:currentPage', 1)
}
</script>

<style scoped>
.custom-table-container {
  background: var(--background-white);
  border-radius: var(--border-radius-large);
  overflow: hidden;
  box-shadow: var(--box-shadow-light);
  transition: var(--transition-all);
}

.custom-table-container:hover {
  box-shadow: var(--box-shadow-base);
}

.custom-table {
  width: 100%;
}

.custom-table .el-table__header-wrapper {
  background-color: var(--primary-light);
}

.custom-table .el-table__header th {
  background-color: var(--primary-light);
  color: var(--primary-dark);
  font-weight: 600;
  border-bottom: 2px solid var(--primary-color);
}

.custom-table .el-table__body tr:hover > td {
  background-color: var(--primary-light);
}

.table-pagination {
  padding: 15px;
  display: flex;
  justify-content: flex-end;
}
</style>
```
    ### 6. 优化页面过渡动画
    #### frontend/src/App.vue (更新)
    ```plaintext
<template>
  <div id="app">
    <router-view v-slot="{ Component }">
      <transition name="page-fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </div>
</template>

<script setup>
// 引入全局样式
import './styles/theme.css'
</script>

<style>
#app {
  font-family: var(--font-family);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--text-primary);
  background-color: var(--background-color);
  min-height: 100vh;
}

/* 页面过渡动画 */
.page-fade-enter-active,
.page-fade-leave-active {
  transition: all 0.3s ease;
}

.page-fade-enter-from {
  opacity: 0;
  transform: translateX(30px);
}

.page-fade-leave-to {
  opacity: 0;
  transform: translateX(-30px);
}
</style>
```
    ### 7. 优化按钮组件
    #### frontend/src/components/CustomButton.vue
    ```plaintext
<template>
  <el-button
    :type="type"
    :size="size"
    :plain="plain"
    :round="round"
    :circle="circle"
    :loading="loading"
    :disabled="disabled"
    :icon="icon"
    :autofocus="autofocus"
    :native-type="nativeType"
    :loading-icon="loadingIcon"
    :use-throttle="useThrottle"
    :throttle-duration="throttleDuration"
    @click="handleClick"
    class="custom-button"
  >
    <slot></slot>
  </el-button>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  type: {
    type: String,
    default: 'default'
  },
  size: {
    type: String,
    default: 'default'
  },
  plain: {
    type: Boolean,
    default: false
  },
  round: {
    type: Boolean,
    default: false
  },
  circle: {
    type: Boolean,
    default: false
  },
  loading: {
    type: Boolean,
    default: false
  },
  disabled: {
    type: Boolean,
    default: false
  },
  icon: {
    type: String,
    default: ''
  },
  autofocus: {
    type: Boolean,
    default: false
  },
  nativeType: {
    type: String,
    default: 'button'
  },
  loadingIcon: {
    type: String,
    default: ''
  },
  useThrottle: {
    type: Boolean,
    default: true
  },
  throttleDuration: {
    type: Number,
    default: 300
  }
})

const emit = defineEmits(['click'])

const handleClick = (event) => {
  emit('click', event)
}
</script>

<style scoped>
.custom-button {
  transition: var(--transition-all);
  border-radius: var(--border-radius-base);
  font-weight: 500;
  box-shadow: 0 2px 0 rgba(0, 0, 0, 0.015);
}

.custom-button:hover {
  transform: translateY(-2px);
  box-shadow: var(--box-shadow-base);
}

.custom-button:active {
  transform: translateY(0);
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.015);
}

.custom-button--primary {
  background-color: var(--primary-color);
  border-color: var(--primary-color);
}

.custom-button--primary:hover {
  background-color: var(--primary-dark);
  border-color: var(--primary-dark);
}

.custom-button--success {
  background-color: var(--success-color);
  border-color: var(--success-color);
}

.custom-button--success:hover {
  background-color: var(--success-dark);
  border-color: var(--success-dark);
}

.custom-button--warning {
  background-color: var(--warning-color);
  border-color: var(--warning-color);
}

.custom-button--warning:hover {
  background-color: var(--warning-dark);
  border-color: var(--warning-dark);
}

.custom-button--danger {
  background-color: var(--danger-color);
  border-color: var(--danger-color);
}

.custom-button--danger:hover {
  background-color: var(--danger-dark);
  border-color: var(--danger-dark);
}

.custom-button--info {
  background-color: var(--info-color);
  border-color: var(--info-color);
}

.custom-button--info:hover {
  background-color: var(--info-dark);
  border-color: var(--info-dark);
}
</style>
```
    ### 8. 优化卡片组件
    #### frontend/src/components/CustomCard.vue
    ```plaintext
<template>
  <div class="custom-card" :class="`custom-card-${variant}`">
    <div v-if="$slots.header" class="card-header">
      <slot name="header"></slot>
    </div>
    <div class="card-content">
      <slot></slot>
    </div>
    <div v-if="$slots.footer" class="card-footer">
      <slot name="footer"></slot>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  variant: {
    type: String,
    default: 'default',
    validator: (value) => ['default', 'primary', 'success', 'warning', 'danger', 'info'].includes(value)
  }
})
</script>

<style scoped>
.custom-card {
  background: var(--background-white);
  border-radius: var(--border-radius-large);
  box-shadow: var(--box-shadow-light);
  padding: 20px;
  margin-bottom: 20px;
  transition: var(--transition-all);
  border: 1px solid var(--border-light);
}

.custom-card:hover {
  box-shadow: var(--box-shadow-base);
  transform: translateY(-2px);
}

.custom-card-primary {
  border-left: 4px solid var(--primary-color);
}

.custom-card-success {
  border-left: 4px solid var(--success-color);
}

.custom-card-warning {
  border-left: 4px solid var(--warning-color);
}

.custom-card-danger {
  border-left: 4px solid var(--danger-color);
}

.custom-card-info {
  border-left: 4px solid var(--info-color);
}

.card-header {
  padding-bottom: 15px;
  border-bottom: 1px solid var(--border-light);
  margin-bottom: 15px;
}

.card-footer {
  padding-top: 15px;
  border-top: 1px solid var(--border-light);
  margin-top: 15px;
}
</style>
```
    ### 9. 更新现有组件使用自定义组件
    #### 更新 QuestionTable.vue
    ```plaintext
<template>
  <div class="question-table">
    <CustomCard>
      <template #header>
        <div class="card-header-content">
          <h2>题库管理</h2>
          <CustomButton type="primary" @click="$emit('importExcel')">
            <el-icon><Upload /></el-icon>
            Excel导入
          </CustomButton>
        </div>
      </template>
      
      <CustomTable
        :data="questions"
        border
        stripe
        @row-click="viewQuestion"
      >
        <el-table-column prop="content" label="题干" min-width="200" />
        <el-table-column prop="difficulty" label="难度" width="100" />
        <el-table-column prop="tags" label="标签" width="150" />
        <el-table-column label="操作" width="100">
          <template #default="scope">
            <CustomButton type="primary" size="small" @click.stop="viewQuestion(scope.row)">
              查看
            </CustomButton>
          </template>
        </el-table-column>
      </CustomTable>
    </CustomCard>
    
    <CustomDialog
      v-model="dialogVisible"
      title="题目详情"
      width="60%"
    >
      <div v-if="selectedQuestion" class="question-detail">
        <h3>题干</h3>
        <p>{{ selectedQuestion.content }}</p>
        
        <div v-if="selectedQuestion.image_url" class="question-image">
          <h3>图片</h3>
          <el-image 
            :src="selectedQuestion.image_url" 
            fit="contain"
            style="max-width: 100%; max-height: 300px;"
          />
        </div>
        
        <div class="question-meta">
          <div class="meta-item">
            <span class="label">难度:</span>
            <span class="value">{{ selectedQuestion.difficulty }}</span>
          </div>
          <div class="meta-item">
            <span class="label">标签:</span>
            <span class="value">{{ selectedQuestion.tags }}</span>
          </div>
        </div>
        
        <div class="question-explanation">
          <h3>解析</h3>
          <p>{{ selectedQuestion.explanation }}</p>
        </div>
      </div>
      
      <template #footer>
        <CustomButton @click="dialogVisible = false">关闭</CustomButton>
      </template>
    </CustomDialog>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '@/api'
import CustomCard from './CustomCard.vue'
import CustomTable from './CustomTable.vue'
import CustomButton from './CustomButton.vue'
import CustomDialog from './CustomDialog.vue'
import { Upload } from '@element-plus/icons-vue'

const questions = ref([])
const dialogVisible = ref(false)
const selectedQuestion = ref(null)

const emit = defineEmits(['importExcel'])

onMounted(async () => {
  try {
    const response = await axios.get('/questions')
    questions.value = response.data.items
  } catch (error) {
    console.error('获取题库失败:', error)
  }
})

const viewQuestion = (question) => {
  selectedQuestion.value = question
  dialogVisible.value = true
}
</script>

<style scoped>
.question-table {
  margin-top: 20px;
}

.card-header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-header-content h2 {
  margin: 0;
  color: var(--text-primary);
}

.question-detail h3 {
  margin-top: 20px;
  margin-bottom: 10px;
  color: var(--text-primary);
  font-size: 16px;
  font-weight: 600;
}

.question-detail h3:first-child {
  margin-top: 0;
}

.question-image {
  margin-top: 20px;
}

.question-meta {
  display: flex;
  flex-wrap: wrap;
  margin-top: 20px;
}

.meta-item {
  margin-right: 30px;
  margin-bottom: 10px;
}

.meta-item .label {
  font-weight: 600;
  margin-right: 5px;
  color: var(--text-regular);
}

.meta-item .value {
  color: var(--text-primary);
}

.question-explanation {
  margin-top: 20px;
}
</style>
```
    ### 10. 更新 HomeworkReview.vue
    ```plaintext
<template>
  <div class="homework-review">
    <CustomCard>
      <template #header>
        <h2>作业批改</h2>
      </template>
      
      <CustomTable
        :data="assignments"
        border
        stripe
      >
        <el-table-column prop="studentName" label="学生" width="120" />
        <el-table-column prop="question" label="题目" min-width="200" />
        <el-table-column prop="answer" label="学生答案" min-width="200" />
        <el-table-column prop="ai_explanation" label="AI解析" min-width="200" />
        <el-table-column label="评分" width="150">
          <template #default="scope">
            <el-input-number 
              v-model="scope.row.score" 
              :min="0" 
              :max="100" 
              :precision="1"
              size="small"
            />
          </template>
        </el-table-column>
        <el-table-column label="批语" width="200">
          <template #default="scope">
            <el-input v-model="scope.row.comment" size="small" />
          </template>
        </el-table-column>
        <el-table-column label="操作" width="120">
          <template #default="scope">
            <CustomButton 
              type="primary" 
              size="small" 
              @click="submitReview(scope.row)"
              :disabled="scope.row.submitted"
            >
              {{ scope.row.submitted ? '已提交' : '提交' }}
            </CustomButton>
          </template>
        </el-table-column>
      </CustomTable>
    </CustomCard>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '@/api'
import { ElMessage } from 'element-plus'
import CustomCard from './CustomCard.vue'
import CustomTable from './CustomTable.vue'
import CustomButton from './CustomButton.vue'

const assignments = ref([])

onMounted(async () => {
  try {
    const response = await axios.get('/homework/review-list')
    assignments.value = response.data.items
  } catch (error) {
    console.error('获取作业列表失败:', error)
  }
})

const submitReview = async (assignment) => {
  try {
    await axios.post('/homework/review', {
      id: assignment.id,
      score: assignment.score,
      comment: assignment.comment
    })
    
    assignment.submitted = true
    ElMessage.success('批改成功')
  } catch (error) {
    console.error('提交批改失败:', error)
    ElMessage.error('提交失败')
  }
}
</script>

<style scoped>
.homework-review {
  margin-top: 20px;
}
</style>
```
    ### 11. 更新 ExcelImport.vue
    ```plaintext
<template>
  <CustomDialog
    v-model="visible"
    title="题库Excel导入"
    width="50%"
    @close="$emit('close')"
  >
    <div class="excel-import-content">
      <div class="template-download">
        <CustomButton type="primary" @click="downloadTemplate">
          <el-icon><Download /></el-icon>
          下载Excel模板
        </CustomButton>
      </div>
      
      <div class="upload-section">
        <el-upload
          class="upload-demo"
          :action="uploadUrl"
          :headers="{ Authorization: 'Bearer ' + token }"
          :on-success="handleSuccess"
          :on-error="handleError"
          :on-progress="handleProgress"
          :file-list="fileList"
          :limit="1"
          accept=".xlsx, .xls"
          :auto-upload="false"
          ref="uploadRef"
        >
          <template #trigger>
            <CustomButton type="primary">选择文件</CustomButton>
          </template>
          <CustomButton 
            type="success" 
            class="upload-btn"
            @click="submitUpload"
            :disabled="fileList.length === 0"
          >
            上传
          </CustomButton>
          <template #tip>
            <div class="el-upload__tip">
              只能上传xlsx/xls文件，且不超过10MB
            </div>
          </template>
        </el-upload>
      </div>
      
      <div v-if="uploading" class="upload-progress">
        <el-progress :percentage="uploadPercentage" :status="uploadStatus" />
      </div>
      
      <el-alert
        v-if="message"
        :title="message"
        :type="messageType"
        show-icon
        :closable="false"
        style="margin-top: 20px;"
      />
    </div>
    
    <template #footer>
      <CustomButton @click="$emit('close')">关闭</CustomButton>
    </template>
  </CustomDialog>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from '@/api'
import { Download } from '@element-plus/icons-vue'
import CustomButton from './CustomButton.vue'
import CustomDialog from './CustomDialog.vue'

const props = defineProps({
  modelValue: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:modelValue', 'close'])

const visible = computed({
  get: () => props.modelValue,
  set: (val) => emit('update:modelValue', val)
})

const token = localStorage.getItem('token')
const templateUrl = '/api/questions/excel-template'
const uploadUrl = '/api/questions/import-excel'
const uploadRef = ref()
const fileList = ref([])
const uploading = ref(false)
const uploadPercentage = ref(0)
const uploadStatus = ref('')
const message = ref('')
const messageType = ref('success')

const downloadTemplate = () => {
  window.open(templateUrl)
}

const submitUpload = () => {
  uploadRef.value.submit()
}

const handleSuccess = (response) => {
  uploading.value = false
  message.value = response.msg || '导入成功'
  messageType.value = 'success'
  fileList.value = []
  uploadPercentage.value = 100
  uploadStatus.value = 'success'
}

const handleError = (error) => {
  uploading.value = false
  message.value = '导入失败'
  messageType.value = 'error'
  uploadPercentage.value = 0
  uploadStatus.value = 'exception'
  console.error('导入错误:', error)
}

const handleProgress = (event) => {
  uploading.value = true
  uploadPercentage.value = Math.floor(event.percent)
  uploadStatus.value = ''
}
</script>

<style scoped>
.excel-import-content {
  padding: 10px 0;
}

.template-download {
  margin-bottom: 20px;
}

.upload-section {
  margin-bottom: 20px;
}

.upload-btn {
  margin-left: 10px;
}

.upload-progress {
  margin-top: 20px;
}
</style>
```
    ### 12. 更新 TeacherDashboard.vue
    ```plaintext
<template>
  <div class="teacher-dashboard">
    <CustomNav />
    
    <div class="dashboard-container">
      <CustomCard>
        <template #header>
          <h2>教师控制台</h2>
        </template>
        
        <el-tabs v-model="activeTab" class="dashboard-tabs">
          <el-tab-pane label="题库管理" name="questions">
            <QuestionTable @importExcel="showImport = true" />
            <ExcelImport v-if="showImport" v-model="showImport" @close="showImport = false" />
          </el-tab-pane>
          <el-tab-pane label="作业管理" name="homework">
            <HomeworkList />
          </el-tab-pane>
          <el-tab-pane label="作业批改" name="review">
            <HomeworkReview />
          </el-tab-pane>
        </el-tabs>
      </CustomCard>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import CustomNav from '@/components/CustomNav.vue'
import CustomCard from '@/components/CustomCard.vue'
import QuestionTable from '@/components/QuestionTable.vue'
import ExcelImport from '@/components/ExcelImport.vue'
import HomeworkList from '@/components/HomeworkList.vue'
import HomeworkReview from '@/components/HomeworkReview.vue'

const activeTab = ref('questions')
const showImport = ref(false)
</script>

<style scoped>
.teacher-dashboard {
  min-height: 100vh;
  background-color: var(--background-color);
}

.dashboard-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.dashboard-tabs {
  margin-top: 20px;
}
</style>
```
    ### 13. 更新路由配置
    #### frontend/src/router/index.js
    ```plaintext
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import StudentDashboard from '../views/StudentDashboard.vue'
import TeacherDashboard from '../views/TeacherDashboard.vue'
import AdminPanel from '../views/AdminPanel.vue'
import { useUserStore } from '@/store'

const routes = [
  { 
    path: '/', 
    component: Home,
    meta: { title: '首页' }
  },
  { 
    path: '/login', 
    component: Login,
    meta: { title: '登录' }
  },
  { 
    path: '/student', 
    component: StudentDashboard, 
    meta: { 
      requiresAuth: true, 
      role: 'student',
      title: '学生控制台'
    } 
  },
  { 
    path: '/teacher', 
    component: TeacherDashboard, 
    meta: { 
      requiresAuth: true, 
      role: 'teacher',
      title: '教师控制台'
    } 
  },
  { 
    path: '/admin', 
    component: AdminPanel, 
    meta: { 
      requiresAuth: true, 
      role: 'admin',
      title: '管理员控制台'
    } 
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

// 路由守卫
router.beforeEach((to, from, next) => {
  const userStore = useUserStore()
  const token = localStorage.getItem('token')
  const role = localStorage.getItem('role')
  
  // 设置页面标题
  document.title = to.meta.title ? `${to.meta.title} - 教育AI题库系统` : '教育AI题库系统'
  
  if (to.meta.requiresAuth) {
    if (!token) {
      next('/login')
    } else if (to.meta.role && to.meta.role !== role) {
      next('/login')
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
```
    ### 14. 创建状态管理
    #### frontend/src/store/index.js
    ```plaintext
import { createPinia, defineStore } from 'pinia'
import axios from '@/api'

const pinia = createPinia()

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || '',
    role: localStorage.getItem('role') || ''
  }),
  
  getters: {
    isLoggedIn: (state) => !!state.token,
    isAdmin: (state) => state.role === 'admin',
    isTeacher: (state) => state.role === 'teacher',
    isStudent: (state) => state.role === 'student'
  },
  
  actions: {
    async login(username, password) {
      try {
        const response = await axios.post('/auth/login', { username, password })
        const { token, role } = response
        
        this.token = token
        this.role = role
        
        localStorage.setItem('token', token)
        localStorage.setItem('role', role)
        
        // 获取用户信息
        await this.fetchUserInfo()
        
        return true
      } catch (error) {
        console.error('登录失败:', error)
        return false
      }
    },
    
    async fetchUserInfo() {
      try {
        const response = await axios.get('/users/me')
        this.user = response
      } catch (error) {
        console.error('获取用户信息失败:', error)
      }
    },
    
    logout() {
      this.user = null
      this.token = ''
      this.role = ''
      
      localStorage.removeItem('token')
      localStorage.removeItem('role')
    }
  }
})

export default pinia
```
    ### 15. 更新 main.js
    #### frontend/src/main.js
    ```plaintext
import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import { createPinia } from 'pinia'
import pinia from './store'
import App from './App.vue'
import router from './router'

const app = createApp(App)

// 注册所有图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app.use(ElementPlus)
app.use(createPinia())
app.use(pinia)
app.use(router)

app.mount('#app')
```
    ### 16. 更新 vite.config.js
    #### frontend/vite.config.js
    ```plaintext
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src')
    }
  },
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  },
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    sourcemap: false,
    chunkSizeWarningLimit: 1500,
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes('node_modules')) {
            return 'vendor'
          }
        }
      }
    }
  }
})
```
    ### 17. 更新 package.json
    #### frontend/package.json
    ```plaintext
{
  "name": "edu-ai-frontend",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "lint": "eslint . --ext vue,js,jsx,cjs,mjs,ts,tsx,cts,mts --fix --ignore-path .gitignore"
  },
  "dependencies": {
    "@element-plus/icons-vue": "^2.1.0",
    "axios": "^1.4.0",
    "element-plus": "^2.3.8",
    "pinia": "^2.1.4",
    "vue": "^3.3.4",
    "vue-router": "^4.2.4"
  },
  "devDependencies": {
    "@rushstack/eslint-patch": "^1.3.2",
    "@vitejs/plugin-vue": "^4.2.3",
    "@vue/eslint-config-prettier": "^8.0.0",
    "eslint": "^8.45.0",
    "eslint-plugin-vue": "^9.15.1",
    "prettier": "^3.0.0",
    "vite": "^4.4.5"
  }
}
```
    ## 总结
    我们实现了以下UI设计改进：
    1. 统一的主题系统：通过CSS变量定义了完整的主题色、文字颜色、边框、背景等，便于全局维护和主题切换。
    1. 响应交互：
        - 按钮悬停效果（上移+阴影）
        - 卡片悬停效果（上移+阴影增强）
        - 表格行悬停高亮
        - 导航项悬停下划线动画
    1. 视觉效果：
        - 统一的圆角和阴影
        - 精心设计的颜色系统
        - 清晰的视觉层次
    1. 动画翻页：
        - 页面切换淡入淡出+滑动效果
        - 弹窗进入/退出动画
        - 列表项过渡动画
    1. 弹窗动画：
        - 自定义弹窗组件，支持淡入淡出+位移动画
        - 可自定义标题、宽度和内容
    1. 组件导航：
        - 自定义导航组件，支持悬停效果和活动状态指示
        - 响应式设计，移动端自动隐藏菜单项
    1. 自定义组件：
        - CustomButton：统一按钮样式和交互
        - CustomCard：统一卡片样式，支持多种变体
        - CustomTable：统一表格样式，优化表头和行悬停
        - CustomDialog：统一弹窗样式和动画
        - CustomNav：统一导航样式和交互
    1. 状态管理：
        - 使用Pinia管理用户状态
        - 实现登录/登出逻辑
        - 路由守卫保护需要认证的页面
    1. 其他优化：
        - 全局过渡动画
        - 自定义滚动条样式
        - 响应式设计适配移动端
        - 统一的间距和排版
    这些改进使整个应用具有一致的外观和感觉，增强了用户体验，并使界面更加现代和专业。所有组件都遵循相同的设计语言，确保了视觉上的连贯性。。
[教育AI题库与作业系统文档](https://docs.qq.com/aio/DWFh4TFFvU2diYnpv?p=kGHkvqfjWqL8dYQmO36lnY)
    ## 1. 产品需求文档（PRD）
    ```plaintext
# 教育AI题库与作业系统产品需求文档

## 1. 文档概述
本文档描述教育AI题库与作业系统的产品需求，包括用户故事、核心功能流程和优先级，面向产品经理和开发团队。

## 2. 用户故事

### 2.1 教师用户故事
- **作为教师**，我希望能管理题库，包括创建、编辑和删除题目，以便高效组织教学资源。
- **作为教师**，我希望能批量导入题目（Excel格式），以便快速建立题库。
- **作为教师**，我希望能布置作业并指定学生，以便分配学习任务。
- **作为教师**，我希望能查看学生提交的作业，以便评估学习效果。
- **作为教师**，我希望能使用AI辅助批改作业，以便减轻工作负担。
- **作为教师**，我希望能查看学生答题统计数据，以便调整教学策略。

### 2.2 学生用户故事
- **作为学生**，我希望能查看教师布置的作业，以便了解学习任务。
- **作为学生**，我希望能在线提交作业答案，以便完成学习任务。
- **作为学生**，我希望能查看作业批改结果和反馈，以便了解学习情况。
- **作为学生**，我希望能查看历史作业和成绩，以便跟踪学习进度。

### 2.3 管理员用户故事
- **作为管理员**，我希望能管理系统用户（教师、学生），以便维护系统安全。
- **作为管理员**，我希望能管理系统学科和题型，以便支持多样化教学。
- **作为管理员**，我希望能监控系统运行状态，以便保障系统稳定。

## 3. 核心功能流程图

### 3.1 题库管理流程
```mermaid
graph TD
    A[教师登录] --> B[进入题库管理]
    B --> C{操作选择}
    C -->|创建题目| D[填写题目信息]
    C -->|编辑题目| E[修改题目信息]
    C -->|删除题目| F[确认删除]
    C -->|导入Excel| G[上传Excel文件]
    D --> H[保存题目]
    E --> H
    G --> I[解析Excel数据]
    I --> H
    H --> J[更新题库]
    F --> J
```
    ### 3.2 作业批改流程
    是
    否
    学生提交作业
    系统记录答案
    触发AI批改任务
    Celery队列处理
    AI模型批改
    生成批改结果
    更新作业状态
    教师查看批改结果
    是否需要人工调整
    教师修改评分/批语
    批改完成
    ## 4. 功能优先级
    ### 4.1 高优先级（核心功能）
    1. 用户认证与权限管理
        - 用户注册、登录、角色分配
        - 基于角色的访问控制
    1. 题库管理
        - 题目的增删改查
        - 题目分类（学科、难度、标签）
        - Excel批量导入
    1. 作业管理
        - 作业创建与发布
        - 学生作业提交
        - 作业状态跟踪
    1. AI批改服务
        - 客观题自动批改
        - 主观题AI辅助批改
        - 批改结果生成
    ### 4.2 中优先级（增强功能）
    1. 作业统计分析
        - 学生答题正确率统计
        - 知识点掌握度分析
        - 班级成绩分布
    1. 通知系统
        - 作业发布通知
        - 批改完成通知
        - 系统消息推送
    1. 题库共享
        - 教师间题库共享
        - 公共题库管理
    ### 4.3 低优先级（扩展功能）
    1. 多模态支持
        - 图片题目OCR识别
        - 语音答案转录
        - 公式识别与解析
    1. 学习路径推荐
        - 基于答题情况推荐学习资源
        - 个性化学习计划生成
    1. 移动端适配
        - 响应式设计优化
        - 移动App开发
    ## 5. 非功能性需求
    ### 5.1 性能需求
    - 系统响应时间：普通操作<2秒，AI批改<30秒
    - 支持并发用户：100+教师同时在线
    - 题库容量：支持10万+题目
    ### 5.2 安全需求
    - 用户密码加密存储
    - API接口JWT认证
    - 敏感数据传输加密
    - 定期数据备份
    ### 5.3 可用性需求
    - 系统可用性≥99.5%
    - 支持浏览器：Chrome、Firefox、Edge最新版本
    - 移动设备兼容性：响应式设计
    ## 6. 验收标准
    ### 6.1 题库管理验收
    - 教师可以成功创建、编辑、删除题目
    - Excel导入功能支持正确解析和验证数据
    - 题目可以按学科、难度、标签分类筛选
    ### 6.2 作业管理验收
    - 教师可以成功创建和发布作业
    - 学生可以查看并提交作业
    - 作业状态正确跟踪（未提交、已提交、已批改）
    ### 6.3 AI批改验收
    - 客观题批改准确率≥98%
    - 主观题批改结果合理，提供有效反馈
    - AI批改任务在30秒内完成
    ## 7. 修订历史
|版本|日期|修改内容|修改人|
|-|-|-|-|
|1.0|2023-10-01|初稿|产品经理|
|1.1|2023-10-15|增加用户故事和流程图|产品经理|
|1.2|2023-10-20|调整功能优先级|产品经理|

                版本
                日期
                修改内容
                修改人
                1.0
                2023-10-01
                初稿
                产品经理
                1.1
                2023-10-15
                增加用户故事和流程图
                产品经理
                1.2
                2023-10-20
                调整功能优先级
                产品经理
    ```plaintext
## 2. 系统设计文档（SDD）

```markdown
# 教育AI题库与作业系统系统设计文档

## 1. 文档概述
本文档描述教育AI题库与作业系统的系统设计，包括整体架构、核心模块职责、数据库设计和关键接口交互逻辑，面向架构师和开发团队。

## 2. 整体架构

### 2.1 架构图
系统采用前后端分离的微服务架构，主要包含以下组件：
```
    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   前端应用       │    │   API网关        │    │   认证服务       │
│  (Vue3 + Element │◄──►│ (Nginx + JWT)   │◄──►│  (OAuth2)       │
│   Plus)         │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
│                       │                       │
│                       │                       │
▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   题库服务       │    │   作业服务       │    │   AI服务         │
│  (FastAPI)       │    │  (FastAPI)       │    │ (FastAPI +       │
│                 │    │                 │    │  Transformers)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
│                       │                       │
│                       │                       │
▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   数据库         │    │   消息队列       │    │   模型存储       │
│  (MariaDB)       │    │   (Redis)        │    │   (NAS)         │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
    ```plaintext
### 2.2 模块间关系
1. **前端应用**：通过HTTP请求与API网关交互，负责用户界面展示和交互
2. **API网关**：统一入口，处理请求路由、认证和负载均衡
3. **认证服务**：管理用户身份验证和授权
4. **题库服务**：提供题库管理相关API，与数据库交互
5. **作业服务**：处理作业相关业务逻辑，与数据库和消息队列交互
6. **AI服务**：提供AI批改功能，与模型存储和消息队列交互
7. **数据库**：持久化存储系统数据
8. **消息队列**：处理异步任务（如AI批改）
9. **模型存储**：存储AI模型文件，供AI服务加载

## 3. 核心模块职责

### 3.1 前端模块
- **职责**：提供用户界面，处理用户交互，展示数据
- **技术栈**：Vue3、Element Plus、Pinia、Axios
- **主要组件**：
  - 登录/注册组件
  - 题库管理组件
  - 作业管理组件
  - AI批改结果展示组件

### 3.2 API网关模块
- **职责**：统一入口，处理请求路由、认证、限流和负载均衡
- **技术栈**：Nginx、JWT
- **主要功能**：
  - 请求路由到对应服务
  - JWT令牌验证
  - 请求限流和熔断
  - 静态资源服务

### 3.3 题库服务模块
- **职责**：提供题库管理相关API，处理题目CRUD操作
- **技术栈**：FastAPI、SQLAlchemy
- **主要功能**：
  - 题目增删改查
  - 题目分类和筛选
  - Excel导入导出
  - 题目版本管理

### 3.4 作业服务模块
- **职责**：处理作业相关业务逻辑，管理作业生命周期
- **技术栈**：FastAPI、SQLAlchemy
- **主要功能**：
  - 作业创建和发布
  - 学生作业提交
  - 作业状态跟踪
  - 作业统计分析

### 3.5 AI服务模块
- **职责**：提供AI批改功能，处理模型推理任务
- **技术栈**：FastAPI、Transformers、Celery
- **主要功能**：
  - 模型加载和管理
  - AI批改任务处理
  - 批改结果生成
  - 模型性能监控

### 3.6 认证服务模块
- **职责**：管理用户身份验证和授权
- **技术栈**：FastAPI、OAuth2
- **主要功能**：
  - 用户注册和登录
  - JWT令牌生成和验证
  - 权限管理
  - 会话管理

## 4. 数据库设计

### 4.1 核心表结构

#### 4.1.1 用户表（users）
| 字段名 | 类型 | 约束 | 描述 |
|--------|------|------|------|
| id | INT | PK, AUTO_INCREMENT | 用户ID |
| username | VARCHAR(100) | UNIQUE, NOT NULL | 用户名 |
| password_hash | VARCHAR(255) | NOT NULL | 密码哈希 |
| name | VARCHAR(100) | | 真实姓名 |
| role | ENUM('student','teacher','admin') | NOT NULL | 用户角色 |
| email | VARCHAR(255) | UNIQUE | 电子邮箱 |
| phone | VARCHAR(20) | | 手机号码 |
| register_time | DATETIME | NOT NULL | 注册时间 |
| last_login | DATETIME | | 最后登录时间 |
| status | TINYINT | DEFAULT 1 | 状态(1:正常,0:禁用) |

#### 4.1.2 学科表（subjects）
| 字段名 | 类型 | 约束 | 描述 |
|--------|------|------|------|
| id | INT | PK, AUTO_INCREMENT | 学科ID |
| name | VARCHAR(50) | NOT NULL | 学科名称 |
| code | VARCHAR(20) | UNIQUE | 学科代码 |
| description | TEXT | | 学科描述 |
| created_by | INT | FK(users.id) | 创建人ID |
| created_at | DATETIME | NOT NULL | 创建时间 |

#### 4.1.3 题目表（questions）
| 字段名 | 类型 | 约束 | 描述 |
|--------|------|------|------|
| id | INT | PK, AUTO_INCREMENT | 题目ID |
| subject_id | INT | FK(subjects.id) | 学科ID |
| type_id | INT | NOT NULL | 题型ID |
| content | TEXT | NOT NULL | 题干内容 |
| option_a | VARCHAR(500) | | 选项A |
| option_b | VARCHAR(500) | | 选项B |
| option_c | VARCHAR(500) | | 选项C |
| option_d | VARCHAR(500) | | 选项D |
| answer | TEXT | | 标准答案 |
| explanation | TEXT | | 解析 |
| difficulty | ENUM('易','中','难','奥数') | NOT NULL | 难度 |
| tags | VARCHAR(255) | | 标签(逗号分隔) |
| image_url | VARCHAR(500) | | 题目图片URL |
| extra_json | TEXT | | 扩展字段(JSON) |
| created_by | INT | FK(users.id) | 创建人ID |
| created_at | DATETIME | NOT NULL | 创建时间 |
| updated_at | DATETIME | NOT NULL | 更新时间 |

#### 4.1.4 作业表（homework）
| 字段名 | 类型 | 约束 | 描述 |
|--------|------|------|------|
| id | INT | PK, AUTO_INCREMENT | 作业ID |
| title | VARCHAR(255) | NOT NULL | 作业标题 |
| description | TEXT | | 作业描述 |
| teacher_id | INT | FK(users.id) | 教师ID |
| start_time | DATETIME | NOT NULL | 开始时间 |
| end_time | DATETIME | NOT NULL | 截止时间 |
| status | ENUM('draft','published','closed') | NOT NULL | 状态 |
| created_at | DATETIME | NOT NULL | 创建时间 |

#### 4.1.5 作业分配表（homework_assignments）
| 字段名 | 类型 | 约束 | 描述 |
|--------|------|------|------|
| id | INT | PK, AUTO_INCREMENT | 分配ID |
| homework_id | INT | FK(homework.id) | 作业ID |
| student_id | INT | FK(users.id) | 学生ID |
| question_id | INT | FK(questions.id) | 题目ID |
| answer | TEXT | | 学生答案 |
| answer_image_url | VARCHAR(500) | | 答案图片URL |
| score | DECIMAL(5,2) | | 得分 |
| ai_explanation | TEXT | | AI解析 |
| comment | TEXT | | 教师批语 |
| submit_time | DATETIME | | 提交时间 |
| review_time | DATETIME | | 批改时间 |
| status | ENUM('pending','submitted','reviewed') | NOT NULL | 状态 |

### 4.2 数据库关系图
```
    users
├── 1:N homework (teacher_id)
├── 1:N questions (created_by)
└── 1:N homework_assignments (student_id)
    subjects
└── 1:N questions (subject_id)
    homework
├── 1:N homework_assignments (homework_id)
└── N:1 users (teacher_id)
    questions
└── 1:N homework_assignments (question_id)
    ```plaintext
## 5. 关键接口交互逻辑

### 5.1 用户登录与认证流程
1. **用户登录接口**：
   - 请求：`POST /api/auth/login`
   - 请求体：`{"username": "string", "password": "string"}`
   - 响应：`{"token": "jwt_token", "role": "student|teacher|admin"}`

2. **认证流程**：
   - 用户提交用户名和密码
   - 认证服务验证凭据
   - 生成JWT令牌并返回
   - 前端存储令牌并在后续请求中携带
   - API网关验证令牌有效性

### 5.2 题目创建流程
1. **创建题目接口**：
   - 请求：`POST /api/questions`
   - 请求体：题目信息JSON
   - 响应：`{"msg": "题目已创建", "id": 123}`

2. **数据流转**：
   - 前端提交题目信息
   - API网关验证JWT令牌
   - 题库服务接收请求
   - 验证数据有效性
   - 写入数据库
   - 返回结果

### 5.3 AI批改流程
1. **提交批改任务接口**：
   - 请求：`POST /api/ai/grade`
   - 请求体：`{"question_id": 123, "answer": "学生答案", "model": "gemma-3-270m"}`
   - 响应：`{"task_id": "task-uuid"}`

2. **数据流转**：
   - 前端提交批改请求
   - AI服务创建Celery任务
   - 任务ID返回前端
   - Celery worker从队列获取任务
   - 加载指定AI模型
   - 构造提示词并推理
   - 生成批改结果
   - 更新数据库
   - 前端轮询获取结果

### 5.4 作业批改流程
1. **提交批改接口**：
   - 请求：`POST /api/homework/review`
   - 请求体：`{"assignment_id": 456, "score": 85.5, "comment": "批语内容"}`
   - 响应：`{"msg": "批改成功"}`

2. **数据流转**：
   - 教师提交批改结果
   - 作业服务接收请求
   - 更新作业分配表
   - 记录批改时间
   - 发送通知给学生
   - 返回成功结果

## 6. 安全设计

### 6.1 认证与授权
- JWT令牌认证，有效期30分钟
- 基于角色的访问控制（RBAC）
- 敏感操作二次验证

### 6.2 数据安全
- 密码使用bcrypt哈希存储
- API通信使用HTTPS加密
- 数据库连接使用SSL/TLS

### 6.3 防护措施
- API请求频率限制
- SQL注入防护
- XSS攻击防护
- CSRF防护

## 7. 性能设计

### 7.1 缓存策略
- Redis缓存用户会话
- 题目列表缓存
- AI模型缓存（内存）

### 7.2 数据库优化
- 适当索引（用户名、题目ID、作业ID等）
- 查询优化（避免全表扫描）
- 连接池管理

### 7.3 异步处理
- AI批改任务异步处理
- 通知消息异步发送
- 大文件上传异步处理

## 8. 扩展性设计

### 8.1 水平扩展
- 微服务架构支持独立扩展
- 无状态服务设计
- 数据库读写分离

### 8.2 插件化设计
- AI模型可插拔替换
- 题目类型可扩展
- 通知渠道可配置

## 9. 监控与日志

### 9.1 监控指标
- 服务响应时间
- 错误率统计
- 资源使用情况
- AI批改任务队列长度

### 9.2 日志管理
- 结构化日志记录
- 日志分级存储
- 敏感信息脱敏
- 日志审计追踪

## 10. 修订历史

| 版本 | 日期       | 修改内容         | 修改人 |
|------|------------|------------------|--------|
| 1.0  | 2023-10-01 | 初稿             | 架构师 |
| 1.1  | 2023-10-15 | 完善架构图和模块职责 | 架构师 |
| 1.2  | 2023-10-20 | 补充接口交互逻辑 | 架构师 |
```
    ## 3. 用户手册
    ```plaintext
# 教育AI题库与作业系统用户手册

## 1. 欢迎使用教育AI题库与作业系统

欢迎使用教育AI题库与作业系统！本系统为教师和学生提供全面的题库管理、作业布置与批改功能。通过AI智能批改技术，帮助教师减轻工作负担，为学生提供即时反馈。

本手册将指导您完成系统的基本操作，包括注册登录、浏览题目、提交作业和查看成绩等。

## 2. 注册登录

### 2.1 注册账户
1. 打开系统登录页面，点击"注册"按钮。
2. 在注册页面，填写以下信息：
   - 用户名：设置一个唯一的用户名，用于登录系统。
   - 密码：设置一个安全的密码，建议包含字母、数字和特殊字符。
   - 确认密码：再次输入密码进行确认。
   - 姓名：输入您的真实姓名。
   - 电子邮箱：输入有效的电子邮箱，用于找回密码。
   - 用户角色：选择您的身份（教师或学生）。
3. 阅读并同意用户协议和隐私政策。
4. 点击"注册"按钮完成注册。
5. 系统会自动登录并跳转到主页面。

### 2.2 登录系统
1. 打开系统登录页面。
2. 输入您的用户名和密码。
3. 点击"登录"按钮。
4. 如果用户名和密码正确，系统将跳转到对应的主页面（教师控制台或学生控制台）。
5. 如果忘记密码，点击"忘记密码"链接，通过注册的邮箱重置密码。

### 2.3 修改密码
1. 登录系统后，点击右上角的用户头像，选择"个人设置"。
2. 在个人设置页面，找到"修改密码"部分。
3. 输入当前密码。
4. 输入新密码并确认。
5. 点击"保存"按钮完成密码修改。

## 3. 浏览题目

### 3.1 教师浏览题目
1. 登录教师控制台，点击"题库管理"标签页。
2. 系统显示所有题目列表，包含题干、难度和标签等信息。
3. 使用筛选功能查找特定题目：
   - 按学科筛选：从下拉菜单选择特定学科。
   - 按难度筛选：选择"易"、"中"、"难"或"奥数"。
   - 按关键词搜索：在搜索框输入关键词，系统会搜索题干和标签。
4. 点击题目行操作列的"查看"按钮，可以查看题目详情，包括题干、选项、答案和解析。
5. 使用分页控件浏览更多题目。

### 3.2 学生浏览题目
1. 登录学生控制台，点击"题库练习"标签页。
2. 系统显示所有可练习的题目列表。
3. 使用筛选和搜索功能查找感兴趣的题目。
4. 点击题目行操作列的"练习"按钮，可以尝试解答该题目。
5. 提交答案后，系统会显示正确答案和解析，帮助学生理解。

## 4. 下单支付（作业提交）

### 4.1 教师布置作业
1. 登录教师控制台，点击"作业管理"标签页。
2. 点击"创建新作业"按钮。
3. 在作业创建页面，填写以下信息：
   - 作业标题：输入作业的名称。
   - 作业描述：详细说明作业要求和注意事项。
   - 开始时间：设置作业的开始时间。
   - 截止时间：设置作业的截止时间。
   - 选择学生：从学生列表中选择要布置作业的学生。
   - 选择题目：从题库中选择要包含在作业中的题目。
4. 点击"保存"按钮创建作业。
5. 系统会自动向选定的学生发送作业通知。

### 4.2 学生提交作业
1. 登录学生控制台，点击"我的作业"标签页。
2. 系统显示所有分配给您的作业列表，包含作业标题、截止时间和状态等信息。
3. 点击"未提交"状态的作业行操作列的"作答"按钮。
4. 系统显示作业包含的所有题目。
5. 依次完成每道题目：
   - 对于选择题：从选项中选择正确答案。
   - 对于主观题：在文本框中输入您的答案。
   - 对于需要上传图片的题目：点击"上传图片"按钮，选择相应的图片文件。
6. 完成所有题目后，点击"提交作业"按钮。
7. 系统会提示"作业提交成功"，作业状态更新为"已提交"。

### 4.3 教师批改作业
1. 登录教师控制台，点击"作业批改"标签页。
2. 系统显示所有需要批改的作业列表。
3. 点击作业行操作列的"批改"按钮。
4. 系统显示该作业的所有学生提交情况。
5. 对于每份提交：
   - 系统会显示学生的答案和AI给出的初步批改结果。
   - 查看AI批改结果，如有需要，可以调整评分和添加批语。
   - 在"评分"字段中输入分数（0-100分）。
   - 在"批语"字段中输入评语或建议。
   - 点击"保存批改"按钮。
6. 批改完成后，系统会自动通知学生批改结果。

## 5. 查看订单（作业成绩）

### 5.1 学生查看作业成绩
1. 登录学生控制台，点击"我的成绩"标签页。
2. 系统显示您所有已批改的作业成绩列表，包含作业标题、提交时间、得分和批语等信息。
3. 点击作业行操作列的"查看详情"按钮，可以查看该作业的详细批改情况，包括每道题目的得分和批语。
4. 系统会统计您的历史成绩，以图表形式展示成绩趋势。
5. 您可以按时间、学科等条件筛选查看成绩。

### 5.2 教师查看作业统计
1. 登录教师控制台，点击"作业统计"标签页。
2. 系统显示所有已发布作业的统计信息，包括：
   - 作业提交率：已提交作业的学生比例。
   - 平均得分：所有学生作业的平均分数。
   - 题目正确率：每道题目的正确率统计。
   - 学生分布：不同分数段的学生人数分布。
3. 点击"导出报表"按钮，可以将统计数据导出为Excel文件。
4. 点击"查看详情"按钮，可以查看特定作业的详细批改情况。

## 6. 常见问题

### 6.1 忘记密码如何找回？
如果您忘记了登录密码，可以通过以下步骤找回：
1. 在登录页面点击"忘记密码"链接。
2. 输入您注册时使用的电子邮箱。
3. 系统会发送一封包含密码重置链接的邮件到您的邮箱。
4. 点击邮件中的链接，进入密码重置页面。
5. 输入新密码并确认。
6. 点击"重置密码"按钮完成密码重置。
7. 使用新密码登录系统。

### 6.2 如何导入题目到题库？
教师可以通过Excel批量导入题目：
1. 登录教师控制台，进入"题库管理"页面。
2. 点击"Excel导入"按钮。
3. 下载Excel模板文件。
4. 按照模板格式填写题目信息。
5. 点击"上传Excel"按钮，选择填写好的Excel文件。
6. 系统会自动解析Excel文件并导入题目到题库。
7. 导入完成后，系统会显示导入结果，包括成功数量和失败原因。

### 6.3 AI批改结果不准确怎么办？
如果AI批改结果不准确，教师可以进行以下操作：
1. 在作业批改页面，查看AI给出的批改结果。
2. 如果认为评分不合理，可以手动调整分数。
3. 在批语字段中添加详细的评语或解释。
4. 点击"保存批改"按钮提交修改。
5. 系统会记录教师的批改结果，并优化AI模型的学习。

### 6.4 如何联系技术支持？
如果您在使用系统过程中遇到技术问题，可以通过以下方式获取帮助：
1. 在系统页面右下角点击"帮助"按钮，查看常见问题解答。
2. 发送邮件至技术支持邮箱：support@example.com。
3. 工作时间（周一至周五，9:00-18:00）拨打技术支持热线：400-123-4567。
4. 在教师/学生群组中提出问题，其他用户或管理员会提供帮助。

### 6.5 系统支持哪些浏览器？
教育AI题库与作业系统支持以下浏览器的最新版本：
1. Google Chrome
2. Mozilla Firefox
3. Microsoft Edge
4. Safari
为了获得最佳使用体验，建议使用Google Chrome或Mozilla Firefox浏览器，并确保浏览器已启用JavaScript和Cookie。

## 7. 版本更新信息

当前系统版本：v2.1.0

最新更新内容：
- 优化AI批改算法，提高主观题批改准确率
- 新增作业统计分析功能
- 改进移动端适配
- 修复已知问题

如需查看完整更新日志，请访问系统"关于"页面。
```
    ## 4. 部署文档
    ```plaintext
# 教育AI题库与作业系统部署文档

## 1. 部署概述

本文档描述教育AI题库与作业系统的部署流程，包括环境要求、部署步骤和配置说明，适用于系统管理员和运维人员。

系统采用微服务架构，支持本地部署和云原生部署，提供Docker Compose和Kubernetes两种部署方式。

## 2. 环境要求

### 2.1 开发环境要求
- **操作系统**: Linux (Ubuntu 20.04+), macOS 10.15+, Windows 10+ (WSL2)
- **Python**: 3.10+
- **Node.js**: 16+
- **Docker**: 20.10+
- **Docker Compose**: 1.29+
- **数据库**: MariaDB 10.6+ 或 MySQL 8.0+
- **缓存**: Redis 6.0+
- **存储**: 至少50GB可用空间（用于模型和数据库）

### 2.2 生产环境要求
- **操作系统**: Linux (Ubuntu 20.04+ LTS, CentOS 8+)
- **容器运行时**: Docker 20.10+ 或 containerd
- **编排工具**: Kubernetes 1.20+ 或 Docker Compose 2.0+
- **数据库**: MariaDB 10.6+ 集群 (主从复制)
- **缓存**: Redis 6.0+ 集群 (哨兵或集群模式)
- **存储**: NAS或分布式存储，至少100GB可用空间
- **负载均衡**: Nginx 1.20+ 或云负载均衡
- **监控**: Prometheus + Grafana (可选)
- **日志**: ELK Stack (可选)

### 2.3 网络要求
- **端口开放**: 
  - 80 (HTTP)
  - 443 (HTTPS)
  - 3306 (数据库)
  - 6379 (Redis)
  - 8000 (后端API)
  - 5173 (前端)
- **带宽**: 建议100Mbps+，特别是在模型下载和更新时

## 3. 部署架构

### 3.1 开发环境架构
```
    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   开发机         │    │   Docker主机     │    │   NAS存储       │
│                 │    │                 │    │                 │
│ ┌─────────────┐ │    │ ┌─────────────┐ │    │ ┌─────────────┐ │
│ │  前端开发   │ │    │ │  前端容器   │ │    │ │  模型文件   │ │
│ │ (Vue3)      │ │    │ │ (Nginx)     │ │    │ │             │ │
│ └─────────────┘ │    │ └─────────────┘ │    │ └─────────────┘ │
│ ┌─────────────┐ │    │ ┌─────────────┐ │    │ ┌─────────────┐ │
│ │  后端开发   │ │◄──►│ │  后端容器   │ │◄──►│ │  数据备份   │ │
│ │ (FastAPI)   │ │    │ │ (Uvicorn)   │ │    │ │             │ │
│ └─────────────┘ │    │ └─────────────┘ │    │ └─────────────┘ │
│ ┌─────────────┐ │    │ ┌─────────────┐ │    │ ┌─────────────┐ │
│ │  数据库     │ │    │ │  数据库容器 │ │    │ │  日志文件   │ │
│ │ (MariaDB)   │ │    │ │ (MariaDB)   │ │    │ │             │ │
│ └─────────────┘ │    │ └─────────────┘ │    │ └─────────────┘ │
└─────────────────┘    └─────────────────┘    └─────────────────┘
    ```plaintext
### 3.2 生产环境架构
```
    ```plaintext
                      ┌─────────────────┐
                      │   负载均衡器     │
                      │   (Nginx/ALB)   │
                      └─────────┬───────┘
                                │
                ┌───────────────┴───────────────┐
                │                                │
    ┌───────────▼──────────┐              ┌────▼─────┐
    │   Web服务器集群       │              │  CDN/    │
    │   (Nginx)             │              │  静态资源 │
    └───────────┬──────────┘              └──────────┘
                │
    ┌───────────┴──────────┐
    │   API网关集群         │
    │   (Kong/Nginx)        │
    └───────────┬──────────┘
                │
┌───────────────┼───────────────┐
│               │               │

```
    ┌───▼───┐     ┌─────▼─────┐   ┌─────▼─────┐
│前端服务│     │  认证服务  │   │  监控服务  │
│集群   │     │  集群     │   │  (Prometheus)│
└───┬───┘     └─────┬─────┘   └───────────┘
│               │
┌───▼───────────────▼───┐
│   微服务集群           │
│                        │
│ ┌───────┐ ┌─────────┐ │
│ │题库服务│ │ 作业服务│ │
│ └───────┘ └─────────┘ │
│ ┌───────┐ ┌─────────┐ │
│ │AI服务 │ │通知服务│ │
│ └───────┘ └─────────┘ │
└─────────┬──────────────┘
│
┌─────▼─────┐
│  消息队列  │
│  (Redis)  │
└─────┬─────┘
│
┌─────▼─────┐     ┌─────────────┐
│  数据库    │     │   NAS存储   │
│  (MariaDB) │     │  (模型文件) │
└───────────┘     └─────────────┘
    ```plaintext
## 4. 部署步骤

### 4.1 开发环境部署 (Docker Compose)

#### 4.1.1 准备工作
1. 克隆项目代码
   ```bash
   git clone https://github.com/your-org/edu-ai-system.git
   cd edu-ai-system
```
    1. 创建环境变量文件
        ```plaintext
cp .env.example .env

```
        编辑.env文件，配置以下变量：
        ```plaintext
DATABASE_URL=mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db
CELERY_BROKER_URL=redis://redis:6379/0
SECRET_KEY=your-secret-key-here
NAS_MODEL_PATH=/mnt/nas/models
```
    1. 创建必要的目录
        ```plaintext
mkdir -p ./data/mysql
mkdir -p ./data/redis
mkdir -p ./models

```
    1. 下载AI模型到./models目录
        ```plaintext
# 示例：下载Gemma模型
git lfs install
git clone https://huggingface.co/google/gemma-2b-it ./models/gemma-2b-it
```
    #### 4.1.2 启动服务
    1. 构建并启动所有服务
        ```plaintext
docker-compose up -d --build

```
    1. 查看服务状态
        ```plaintext
docker-compose ps

```
    1. 查看日志
        ```plaintext
docker-compose logs -f backend
docker-compose logs -f frontend

```
    1. 初始化数据库
        ```plaintext
# 进入后端容器
docker-compose exec backend bash

# 运行数据库迁移
alembic upgrade head

# 创建初始管理员用户（可选）
python -c "from backend.database import SessionLocal; from backend.models import User; from backend.auth import get_password_hash; db = SessionLocal(); admin = User(username='admin', password_hash=get_password_hash('admin'), name='管理员', role='admin'); db.add(admin); db.commit(); print('管理员用户已创建')"
```
    #### 4.1.3 访问系统
    - 前端界面: http://localhost:5173
    - 后端API: http://localhost:8000
    - API文档: http://localhost:8000/docs
    #### 4.1.4 停止服务
    ```plaintext
docker-compose down

```
    ### 4.2 生产环境部署 (Kubernetes)
    #### 4.2.1 准备工作
    1. 安装和配置Kubernetes集群
        - 可以使用云服务商提供的Kubernetes服务（如EKS、GKE、ACK）
        - 或使用kubeadm自建集群
    1. 安装kubectl并配置kubeconfig
        ```plaintext
kubectl cluster-info

```
    1. 安装Helm 3（可选，用于管理复杂应用）
        ```plaintext
# 下载Helm
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```
    1. 准备NAS存储
        - 确保Kubernetes节点可以访问NAS
        - 创建PersistentVolume和PersistentVolumeClaim
    #### 4.2.2 创建命名空间
    ```plaintext
kubectl create namespace edu-ai-system

```
    #### 4.2.3 部署数据库
    1. 创建MariaDB配置文件
        ```plaintext
# mariadb-configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: mariadb-config
  namespace: edu-ai-system
data:
  my.cnf: |
    [mysqld]
    character-set-server=utf8mb4
    collation-server=utf8mb4_unicode_ci
    max_allowed_packet=256M
```
    1. 创建MariaDB部署
        ```plaintext
# mariadb-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mariadb
  namespace: edu-ai-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mariadb
  template:
    metadata:
      labels:
        app: mariadb
    spec:
      containers:
      - name: mariadb
        image: mariadb:10.6
        ports:
        - containerPort: 3306
        env:
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mariadb-secret
              key: root-password
        - name: MYSQL_DATABASE
          value: edu_ai_db
        volumeMounts:
        - name: mariadb-data
          mountPath: /var/lib/mysql
        - name: config
          mountPath: /etc/mysql/conf.d
      volumes:
      - name: mariadb-data
        persistentVolumeClaim:
          claimName: mariadb-pvc
      - name: config
        configMap:
          name: mariadb-config
```
    1. 创建MariaDB服务
        ```plaintext
# mariadb-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: mariadb
  namespace: edu-ai-system
spec:
  selector:
    app: mariadb
  ports:
  - port: 3306
  clusterIP: None
```
    1. 创建数据库密码Secret
        ```plaintext
kubectl create secret generic mariadb-secret --from-literal=root-password=yourpassword -n edu-ai-system

```
    1. 应用配置
        ```plaintext
kubectl apply -f mariadb-configmap.yaml
kubectl apply -f mariadb-deployment.yaml
kubectl apply -f mariadb-service.yaml

```
    #### 4.2.4 部署Redis
    ```plaintext
# redis-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
  namespace: edu-ai-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis:6-alpine
        ports:
        - containerPort: 6379
        volumeMounts:
        - name: redis-data
          mountPath: /data
      volumes:
      - name: redis-data
        persistentVolumeClaim:
          claimName: redis-pvc
---
apiVersion: v1
kind: Service
metadata:
  name: redis
  namespace: edu-ai-system
spec:
  selector:
    app: redis
  ports:
  - port: 6379
```
    应用配置:
    ```plaintext
kubectl apply -f redis-deployment.yaml

```
    #### 4.2.5 部署后端服务
    1. 构建后端镜像并推送到镜像仓库
        ```plaintext
# backend/Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend /app/backend

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
```
        ```plaintext
# 构建镜像
docker build -t your-registry/edu-ai-backend:latest ./backend

# 推送到镜像仓库
docker push your-registry/edu-ai-backend:latest
```
    1. 创建后端部署配置
        ```plaintext
# backend-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
  namespace: edu-ai-system
spec:
  replicas: 2
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
      - name: backend
        image: your-registry/edu-ai-backend:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          value: "mysql+pymysql://root:$(DB_ROOT_PASSWORD)@mariadb:3306/edu_ai_db"
        - name: CELERY_BROKER_URL
          value: "redis://redis:6379/0"
        - name: SECRET_KEY
          valueFrom:
            secretKeyRef:
              name: backend-secret
              key: secret-key
        volumeMounts:
        - name: nas-models
          mountPath: /mnt/nas/models
      volumes:
      - name: nas-models
        persistentVolumeClaim:
          claimName: nas-models-pvc
---
apiVersion: v1
kind: Service
metadata:
  name: backend-service
  namespace: edu-ai-system
spec:
  selector:
    app: backend
  ports:
  - port: 8000
```
    1. 创建后端Secret
        ```plaintext
kubectl create secret generic backend-secret --from-literal=secret-key=your-secret-key -n edu-ai-system
kubectl create secret generic backend-secret --from-literal=DB_ROOT_PASSWORD=yourpassword -n edu-ai-system

```
    1. 应用配置
        ```plaintext
kubectl apply -f backend-deployment.yaml

```
    #### 4.2.6 部署前端服务
    1. 构建前端镜像并推送到镜像仓库
        ```plaintext
# frontend/Dockerfile
FROM node:16-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```
        ```plaintext
# 构建镜像
docker build -t your-registry/edu-ai-frontend:latest ./frontend

# 推送到镜像仓库
docker push your-registry/edu-ai-frontend:latest
```
    1. 创建前端部署配置
        ```plaintext
# frontend-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  namespace: edu-ai-system
spec:
  replicas: 2
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: frontend
        image: your-registry/edu-ai-frontend:latest
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
  namespace: edu-ai-system
spec:
  selector:
    app: frontend
  ports:
  - port: 80
```
    1. 应用配置
        ```plaintext
kubectl apply -f frontend-deployment.yaml

```
    #### 4.2.7 部署Ingress
    ```plaintext
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: edu-ai-ingress
  namespace: edu-ai-system
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /$2
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  tls:
  - hosts:
    - ai.yourdomain.com
    secretName: edu-ai-tls
  rules:
  - host: ai.yourdomain.com
    http:
      paths:
      - path: /api(/|$)(.*)
        pathType: Prefix
        backend:
          service:
            name: backend-service
            port:
              number: 8000
      - path: /()(.*)
        pathType: Prefix
        backend:
          service:
            name: frontend-service
            port:
              number: 80
```
    应用配置:
    ```plaintext
kubectl apply -f ingress.yaml

```
    #### 4.2.8 部署Celery Worker
    ```plaintext
# celery-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: celery-worker
  namespace: edu-ai-system
spec:
  replicas: 2
  selector:
    matchLabels:
      app: celery-worker
  template:
    metadata:
      labels:
        app: celery-worker
    spec:
      containers:
      - name: celery-worker
        image: your-registry/edu-ai-backend:latest
        command: ["celery", "-A", "backend.celery_worker", "worker", "--loglevel=info"]
        env:
        - name: DATABASE_URL
          value: "mysql+pymysql://root:$(DB_ROOT_PASSWORD)@mariadb:3306/edu_ai_db"
        - name: CELERY_BROKER_URL
          value: "redis://redis:6379/0"
        - name: SECRET_KEY
          valueFrom:
            secretKeyRef:
              name: backend-secret
              key: secret-key
        volumeMounts:
        - name: nas-models
          mountPath: /mnt/nas/models
      volumes:
      - name: nas-models
        persistentVolumeClaim:
          claimName: nas-models-pvc
```
    应用配置:
    ```plaintext
kubectl apply -f celery-deployment.yaml

```
    #### 4.2.9 初始化数据库
    ```plaintext
# 在后端Pod中运行数据库迁移
kubectl exec -it deployment/backend -n edu-ai-system -- alembic upgrade head

# 创建初始管理员用户
kubectl exec -it deployment/backend -n edu-ai-system -- python -c "
from backend.database import SessionLocal
from backend.models import User
from backend.auth import get_password_hash
db = SessionLocal()
admin = User(username='admin', password_hash=get_password_hash('admin'), name='管理员', role='admin')
db.add(admin)
db.commit()
print('管理员用户已创建')
"
```
    #### 4.2.10 验证部署
    1. 检查Pod状态
        ```plaintext
kubectl get pods -n edu-ai-system

```
    1. 检查服务状态
        ```plaintext
kubectl get svc -n edu-ai-system

```
    1. 检查Ingress状态
        ```plaintext
kubectl get ingress -n edu-ai-system

```
    1. 访问系统
        - 前端界面: https://ai.yourdomain.com
        - 后端API: https://ai.yourdomain.com/api
        - API文档: https://ai.yourdomain.com/api/docs
    ## 5. 配置说明
    ### 5.1 环境变量配置
    #### 5.1.1 后端服务环境变量
|变量名|描述|默认值|示例|
|-|-|-|-|
|DATABASE_URL|数据库连接字符串|无|mysql+pymysql://root:password@mariadb:3306/edu_ai_db|
|CELERY_BROKER_URL|Celery消息代理URL|无|redis://redis:6379/0|
|SECRET_KEY|JWT密钥|无|your-secret-key-here|
|NAS_MODEL_PATH|NAS模型路径|/mnt/nas/models|/mnt/nas/models|
|LOG_LEVEL|日志级别|INFO|DEBUG|
|MAX_CONTENT_LENGTH|最大请求内容长度|10485760|20971520|

                变量名
                描述
                默认值
                示例
                DATABASE_URL
                数据库连接字符串
                无
                mysql+pymysql://root:password@mariadb:3306/edu_ai_db
                CELERY_BROKER_URL
                Celery消息代理URL
                无
                redis://redis:6379/0
                SECRET_KEY
                JWT密钥
                无
                your-secret-key-here
                NAS_MODEL_PATH
                NAS模型路径
                /mnt/nas/models
                /mnt/nas/models
                LOG_LEVEL
                日志级别
                INFO
                DEBUG
                MAX_CONTENT_LENGTH
                最大请求内容长度
                10485760
                20971520
    #### 5.1.2 前端服务环境变量
|变量名|描述|默认值|示例|
|-|-|-|-|
|VITE_API_BASE_URL|API基础URL|/api|https://api.example.com|
|VITE_APP_TITLE|应用标题|教育AI题库系统|我的题库系统|
|VITE_APP_VERSION|应用版本|2.1.0|2.1.0|

                变量名
                描述
                默认值
                示例
                VITE_API_BASE_URL
                API基础URL
                /api
                https://api.example.com
                VITE_APP_TITLE
                应用标题
                教育AI题库系统
                我的题库系统
                VITE_APP_VERSION
                应用版本
                2.1.0
                2.1.0
    ### 5.2 数据库配置
    #### 5.2.1 连接池配置
    ```plaintext
# 后端/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:password@mariadb:3306/edu_ai_db"
# 连接池配置
engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    pool_recycle=300
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
```
    #### 5.2.2 索引优化
    ```plaintext
-- 用户表索引
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_role ON users(role);

-- 题目表索引
CREATE INDEX idx_questions_subject_id ON questions(subject_id);
CREATE INDEX idx_questions_difficulty ON questions(difficulty);
CREATE INDEX idx_questions_created_at ON questions(created_at);

-- 作业分配表索引
CREATE INDEX idx_homework_assignments_homework_id ON homework_assignments(homework_id);
CREATE INDEX idx_homework_assignments_student_id ON homework_assignments(student_id);
CREATE INDEX idx_homework_assignments_status ON homework_assignments(status);
```
    ### 5.3 Redis配置
    #### 5.3.1 连接配置
    ```plaintext
# backend/celery_worker.py
from celery import Celery

# Celery配置
app = Celery(
    'edu-ai',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0',
    broker_connection_retry_on_startup=True
)

# 任务配置
app.conf.task_serializer = 'json'
app.conf.accept_content = ['json']
app.conf.result_serializer = 'json'
app.conf.timezone = 'Asia/Shanghai'
```
    #### 5.3.2 持久化配置
    ```plaintext
# redis-persistent.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: redis-config
  namespace: edu-ai-system
data:
  redis.conf: |
    appendonly yes
    appendfsync everysec
    save 900 1
    save 300 10
    save 60 10000
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: redis-pvc
  namespace: edu-ai-system
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
```
    ### 5.4 AI模型配置
    #### 5.4.1 模型路径配置
    ```plaintext
# backend/celery_worker.py
import os

# 模型路径配置
MODEL_PATH = os.getenv('NAS_MODEL_PATH', '/mnt/nas/models')
SUPPORTED_MODELS = {
    'gemma-2b-it': f'{MODEL_PATH}/gemma-2b-it',
    'llama-3-8b': f'{MODEL_PATH}/llama-3-8b',
    'phi-3-mini': f'{MODEL_PATH}/phi-3-mini',
    'code-llama': f'{MODEL_PATH}/code-llama'
}
```
    #### 5.4.2 模型加载配置
    ```plaintext
# backend/celery_worker.py
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 模型加载配置
def load_model(model_name):
    if model_name not in MODEL_CACHE:
        model_path = SUPPORTED_MODELS.get(model_name)
        if not model_path:
            raise ValueError(f"Unsupported model: {model_name}")
        
        # 设备配置
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # 加载模型和tokenizer
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map='auto'
        )
        
        MODEL_CACHE[model_name] = (tokenizer, model, device)
    
    return MODEL_CACHE[model_name]
```
    ## 6. 监控与日志
    ### 6.1 服务监控
    1. 部署Prometheus和Grafana
        ```plaintext
# 创建监控命名空间
kubectl create namespace monitoring

# 部署Prometheus
helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring
```
    1. 配置服务监控
        ```plaintext
# backend-monitor.yaml
apiVersion: v1
kind: ServiceMonitor
metadata:
  name: backend-monitor
  namespace: monitoring
  labels:
    app: backend
spec:
  selector:
    matchLabels:
      app: backend
  endpoints:
  - port: metrics
    interval: 15s
```
    ### 6.2 日志收集
    1. 部署EFK Stack
        ```plaintext
# 创建日志命名空间
kubectl create namespace logging

# 部署Elasticsearch
helm install elasticsearch elastic/elasticsearch -n logging

# 部署Kibana
helm install kibana elastic/kibana -n logging

# 部署Fluentd
helm install fluentd fluent/fluentd -n logging
```
    1. 配置日志格式
        ```plaintext
# backend/main.py
import logging
import sys
from pydantic import BaseModel

# 日志配置
logging.basicConfig(
    level=logging.INFO,
    format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

# 记录请求日志
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(
        f"method={request.method} path={request.url.path} "
        f"status_code={response.status_code} process_time={process_time:.4f}"
    )
    return response
```
    ## 7. 备份与恢复
    ### 7.1 数据库备份
    1. 创建备份脚本
        ```plaintext
# backup-db.sh
#!/bin/bash

# 配置变量
DB_HOST="mariadb"
DB_USER="root"
DB_PASS="yourpassword"
DB_NAME="edu_ai_db"
BACKUP_DIR="/mnt/nas/backups"
DATE=$(date +%Y%m%d_%H%M%S)

# 创建备份目录
mkdir -p $BACKUP_DIR

# 执行备份
mysqldump -h $DB_HOST -u $DB_USER -p$DB_PASS $DB_NAME | gzip > $BACKUP_DIR/edu_ai_db_$DATE.sql.gz

# 保留最近7天的备份
find $BACKUP_DIR -name "edu_ai_db_*.sql.gz" -mtime +7 -delete

echo "数据库备份完成: $BACKUP_DIR/edu_ai_db_$DATE.sql.gz"
```
    1. 创建定时任务
        ```plaintext
# 编辑crontab
crontab -e

# 添加定时任务，每天凌晨2点执行备份
0 2 * * * /path/to/backup-db.sh >> /var/log/db-backup.log 2>&1
```
    ### 7.2 数据库恢复
    1. 创建恢复脚本
        ```plaintext
# restore-db.sh
#!/bin/bash

# 配置变量
DB_HOST="mariadb"
DB_USER="root"
DB_PASS="yourpassword"
DB_NAME="edu_ai_db"
BACKUP_FILE=$1

# 检查备份文件
if [ -z "$BACKUP_FILE" ]; then
    echo "请指定备份文件路径"
    exit 1
fi

if [ ! -f "$BACKUP_FILE" ]; then
    echo "备份文件不存在: $BACKUP_FILE"
    exit 1
fi

# 执行恢复
gunzip < $BACKUP_FILE | mysql -h $DB_HOST -u $DB_USER -p$DB_PASS $DB_NAME

echo "数据库恢复完成: $BACKUP_FILE"
```
    1. 执行恢复
        ```plaintext
# 恢复最新备份
./restore-db.sh /mnt/nas/backups/edu_ai_db_20231001_020000.sql.gz

# 恢复指定备份
./restore-db.sh /mnt/nas/backups/edu_ai_db_20231001_020000.sql.gz
```
    ### 7.3 模型文件备份
    1. 使用rsync同步模型文件
        ```plaintext
# backup-models.sh
#!/bin/bash

# 配置变量
MODEL_DIR="/mnt/nas/models"
BACKUP_DIR="/mnt/nas/backups/models"

# 创建备份目录
mkdir -p $BACKUP_DIR

# 同步模型文件
rsync -av --delete $MODEL_DIR/ $BACKUP_DIR/

echo "模型文件备份完成: $BACKUP_DIR"
```
    1. 创建定时任务
        ```plaintext
# 编辑crontab
crontab -e

# 添加定时任务，每周日凌晨1点执行备份
0 1 * * 0 /path/to/backup-models.sh >> /var/log/models-backup.log 2>&1
```
    ## 8. 故障排查
    ### 8.1 常见问题及解决方案
    #### 8.1.1 服务无法启动
    问题: 后端服务启动失败，报错"数据库连接失败"解决方案:
    1. 检查数据库服务状态
        ```plaintext
kubectl get pods -n edu-ai-system | grep mariadb

```
    1. 检查数据库服务日志
        ```plaintext
kubectl logs -f deployment/mariadb -n edu-ai-system

```
    1. 检查数据库连接配置
        ```plaintext
kubectl get secret backend-secret -n edu-ai-system -o yaml

```
    1. 重新部署后端服务
        ```plaintext
kubectl rollout restart deployment/backend -n edu-ai-system

```
    #### 8.1.2 AI批改任务失败
    问题: AI批改任务一直处于"pending"状态解决方案:
    1. 检查Celery Worker状态
        ```plaintext
kubectl get pods -n edu-ai-system | grep celery

```
    1. 检查Celery Worker日志
        ```plaintext
kubectl logs -f deployment/celery-worker -n edu-ai-system

```
    1. 检查Redis服务状态
        ```plaintext
kubectl get pods -n edu-ai-system | grep redis

```
    1. 检查Redis连接配置
        ```plaintext
kubectl exec -it deployment/backend -n edu-ai-system -- env | grep CELERY
```
    1. 重启Celery Worker
        ```plaintext
kubectl rollout restart deployment/celery-worker -n edu-ai-system

```
    #### 8.1.3 前端无法访问后端API
    问题: 前端页面报错"Network Error"解决方案:
    1. 检查后端服务状态
        ```plaintext
kubectl get pods -n edu-ai-system | grep backend

```
    1. 检查后端服务日志
        ```plaintext
kubectl logs -f deployment/backend -n edu-ai-system

```
    1. 检查服务配置
        ```plaintext
kubectl get svc -n edu-ai-system

```
    1. 检查Ingress配置
        ```plaintext
kubectl get ingress -n edu-ai-system

```
    1. 检查CORS配置
        ```plaintext
kubectl exec -it deployment/backend -n edu-ai-system -- cat /app/backend/main.py | grep -A 10 CORSMiddleware
```
    ### 8.2 日志分析
    1. 收集所有服务日志
        ```plaintext
mkdir -p /tmp/edu-ai-logs

# 收集后端日志
kubectl logs deployment/backend -n edu-ai-system > /tmp/edu-ai-logs/backend.log

# 收集前端日志
kubectl logs deployment/frontend -n edu-ai-system > /tmp/edu-ai-logs/frontend.log

# 收集Celery日志
kubectl logs deployment/celery-worker -n edu-ai-system > /tmp/edu-ai-logs/celery.log

# 收集数据库日志
kubectl logs deployment/mariadb -n edu-ai-system > /tmp/edu-ai-logs/mariadb.log

# 收集Redis日志
kubectl logs deployment/redis -n edu-ai-system > /tmp/edu-ai-logs/redis.log
```
    1. 分析错误日志
        ```plaintext
# 查看后端错误日志
grep -i "error\|exception\|failed" /tmp/edu-ai-logs/backend.log

# 查看前端错误日志
grep -i "error\|failed" /tmp/edu-ai-logs/frontend.log

# 查看Celery错误日志
grep -i "error\|exception\|failed" /tmp/edu-ai-logs/celery.log
```
    ## 9. 性能优化
    ### 9.1 数据库优化
    1. 增加连接池大小
        ```plaintext
# backend/database.py
engine = create_engine(
    DATABASE_URL,
    pool_size=20,         # 连接池大小
    max_overflow=30,      # 最大溢出连接数
    pool_recycle=3600,    # 连接回收时间(秒)
    pool_pre_ping=True    # 每次连接前ping一下
)
```
    1. 添加读写分离
        ```plaintext
# backend/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 主库(写)
master_engine = create_engine("mysql+pymysql://root:password@master-db:3306/edu_ai_db")

# 从库(读)
slave_engine = create_engine("mysql+pymysql://root:password@slave-db:3306/edu_ai_db")

# 会话工厂
MasterSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=master_engine)
SlaveSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=slave_engine)

# 获取数据库会话
def get_db():
    db = SlaveSessionLocal()  # 默认使用从库
    try:
        yield db
    finally:
        db.close()

def get_write_db():
    db = MasterSessionLocal()  # 写操作使用主库
    try:
        yield db
    finally:
        db.close()
```
    ### 9.2 缓存优化
    1. 使用Redis缓存常用数据
        ```plaintext
# backend/utils/cache.py
import redis
import json
import pickle
from functools import wraps

# Redis连接
redis_client = redis.Redis(host='redis', port=6379, db=0)

# 缓存装饰器
def cache(expire=3600):
    def decorator(func):
@wraps(func)
        def wrapper(*args, **kwargs):
            # 生成缓存键
            key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            
            # 尝试从缓存获取
            cached = redis_client.get(key)
            if cached:
                try:
                    return pickle.loads(cached)
                except:
                    pass
            
            # 执行函数
            result = func(*args, **kwargs)
            
            # 存入缓存
            redis_client.setex(key, expire, pickle.dumps(result))
            
            return result
        return wrapper
    return decorator

# 使用示例
@cache(expire=1800)# 缓存30分钟
def get_questions(subject_id=None):
    # 查询数据库
    # ...
    return questions
```
    1. 缓存AI模型
        ```plaintext
# backend/celery_worker.py
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 全局模型缓存
MODEL_CACHE = {}

def load_model(model_name):
    if model_name not in MODEL_CACHE:
        model_path = SUPPORTED_MODELS.get(model_name)
        if not model_path:
            raise ValueError(f"Unsupported model: {model_name}")
        
        # 设备配置
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # 加载模型和tokenizer
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map='auto'
        )
        
        # 存入缓存
        MODEL_CACHE[model_name] = {
            'tokenizer': tokenizer,
            'model': model,
            'device': device
        }
    
    return MODEL_CACHE[model_name]
```
    ### 9.3 前端优化
    1. 启用Gzip压缩
        ```plaintext
# nginx.conf
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_proxied any;
gzip_comp_level 6;
gzip_types
    text/plain
    text/css
    text/xml
    text/javascript
    application/javascript
    application/xml+rss
    application/json;
```
    1. 启用浏览器缓存
        ```plaintext
# nginx.conf
location ~* \.(jpg|jpeg|png|gif|ico|css|js|pdf|txt)$ {
    expires 7d;
    add_header Cache-Control "public, no-transform";
}
```
    1. 使用CDN加速静态资源
        ```plaintext
<!-- index.html -->
<link rel="stylesheet" href="https://cdn.example.com/css/app.css">
<script src="https://cdn.example.com/js/app.js"></script>
```
    ## 10. 安全加固
    ### 10.1 网络安全
    1. 配置网络策略
        ```plaintext
# network-policy.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: edu-ai-network-policy
  namespace: edu-ai-system
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: edu-ai-system
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          name: edu-ai-system
    - to:
      - ipBlock:
          cidr: 0.0.0.0/0
        ports:
        - protocol: TCP
          port: 443
        - protocol: TCP
          port: 80
```
    1. 启用TLS加密
        ```plaintext
# tls-secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: edu-ai-tls
  namespace: edu-ai-system
type: kubernetes.io/tls
data:
  tls.crt: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0t...
  tls.key: LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0t...
```
    ### 10.2 应用安全
    1. 配置安全头
        ```plaintext
# nginx.conf
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'" always;
```
    1. 限制API请求频率
        ```plaintext
# rate-limit.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: edu-ai-ingress
  namespace: edu-ai-system
  annotations:
    nginx.ingress.kubernetes.io/limit-rps: "10"
    nginx.ingress.kubernetes.io/limit-connections: "5"
spec:
  # ... 其他配置
```
    1. 审计日志
        ```plaintext
# backend/main.py
import logging
import time

logger = logging.getLogger(__name__)

@app.middleware("http")
async def audit_log(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    # 记录审计日志
    logger.info(
        f"audit: method={request.method} path={request.url.path} "
        f"status_code={response.status_code} process_time={process_time:.4f} "
        f"user_agent={request.headers.get('user-agent')} "
        f"remote_addr={request.client.host}"
    )
    
    return response
```
    ### 10.3 数据安全
    1. 数据库加密
        ```plaintext
-- 创建加密表
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    -- 敏感字段加密
    id_card VARBINARY(255) ENCRYPTED USING AES_256_CBC,
    phone VARBINARY(20) ENCRYPTED USING AES_256_CBC,
    -- 其他字段...
);
```
    1. 敏感数据脱敏
        ```plaintext
# backend/utils/sanitizer.py
import re

def sanitize_phone(phone):
    if not phone:
        return phone
    return re.sub(r'(\d{3})\d{4}(\d{4})', r'\1****\2', phone)

def sanitize_id_card(id_card):
    if not id_card:
        return id_card
    return re.sub(r'(\d{6})\d{8}(\d{4})', r'\1********\2', id_card)

def sanitize_email(email):
    if not email:
        return email
    username, domain = email.split('@')
    username = username[:2] + '*' * (len(username) - 2)
    return f"{username}@{domain}"
```
    ## 11. 版本升级
    ### 11.1 升级流程
    1. 备份数据
        ```plaintext
# 备份数据库
./backup-db.sh

# 备份模型文件
./backup-models.sh
```
    1. 更新代码
        ```plaintext
# 拉取最新代码
git pull origin main

# 更新子模块
git submodule update --init --recursive
```
    1. 更新依赖
        ```plaintext
# 更新后端依赖
cd backend
pip install -r requirements.txt --upgrade

# 更新前端依赖
cd ../frontend
npm update
```
    1. 重新构建镜像
        ```plaintext
# 构建后端镜像
docker build -t your-registry/edu-ai-backend:latest ./backend
docker push your-registry/edu-ai-backend:latest

# 构建前端镜像
docker build -t your-registry/edu-ai-frontend:latest ./frontend
docker push your-registry/edu-ai-frontend:latest
```
    1. 应用更新
        ```plaintext
# 更新Kubernetes部署
kubectl set image deployment/backend backend=your-registry/edu-ai-backend:latest -n edu-ai-system
kubectl set image deployment/frontend frontend=your-registry/edu-ai-frontend:latest -n edu-ai-system
kubectl set image deployment/celery-worker backend=your-registry/edu-ai-backend:latest -n edu-ai-system

# 检查更新状态
kubectl rollout status deployment/backend -n edu-ai-system
kubectl rollout status deployment/frontend -n edu-ai-system
kubectl rollout status deployment/celery-worker -n edu-ai-system
```
    1. 数据库迁移
        ```plaintext
# 在后端Pod中运行迁移
kubectl exec -it deployment/backend -n edu-ai-system -- alembic upgrade head
```
    1. 验证更新
        ```plaintext
# 检查Pod状态
kubectl get pods -n edu-ai-system

# 检查服务日志
kubectl logs -f deployment/backend -n edu-ai-system
kubectl logs -f deployment/frontend -n edu-ai-system
kubectl logs -f deployment/celery-worker -n edu-ai-system

# 访问系统验证功能
curl https://ai.yourdomain.com/api/health
```
    ### 11.2 回滚策略
    1. 准备回滚脚本
        ```plaintext
# rollback.sh
#!/bin/bash

# 回滚到指定版本
VERSION=$1

if [ -z "$VERSION" ]; then
    echo "请指定回滚版本"
    exit 1
fi

# 回滚Kubernetes部署
kubectl set image deployment/backend backend=your-registry/edu-ai-backend:$VERSION -n edu-ai-system
kubectl set image deployment/frontend frontend=your-registry/edu-ai-frontend:$VERSION -n edu-ai-system
kubectl set image deployment/celery-worker backend=your-registry/edu-ai-backend:$VERSION -n edu-ai-system

# 检查回滚状态
kubectl rollout status deployment/backend -n edu-ai-system
kubectl rollout status deployment/frontend -n edu-ai-system
kubectl rollout status deployment/celery-worker -n edu-ai-system

echo "回滚完成: $VERSION"
```
    1. 执行回滚
        ```plaintext
# 回滚到上一个版本
./rollback.sh v2.0.5

# 回滚到指定版本
./rollback.sh v2.0.4
```
    ## 12. 总结
    本文档详细介绍了教育AI题库与作业系统的部署流程，包括环境要求、部署步骤、配置说明、监控日志、备份恢复、故障排查、性能优化、安全加固和版本升级等内容。
    系统采用微服务架构，支持Docker Compose和Kubernetes两种部署方式，可以根据实际需求选择合适的部署方案。在部署过程中，需要注意网络配置、存储规划、安全加固等方面的问题，确保系统稳定可靠地运行。
    对于生产环境，建议使用Kubernetes进行部署，并结合CI/CD流水线实现自动化部署。同时，需要配置完善的监控、日志和备份机制，确保系统的可观测性和可靠性。
    如在部署过程中遇到问题，可以参考本文档的故障排查部分，或联系技术支持获取帮助。
[教育AI题库与作业系统优化方案](https://docs.qq.com/aio/DWFh4TFFvU2diYnpv?p=m3JyHL65bsnBk2cV1cslra)