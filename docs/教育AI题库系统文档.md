# 教育AI题库与作业系统文档

## 1. 产品需求文档（PRD）

```markdown
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

```mermaid
graph TD
    A[学生提交作业] --> B[系统记录答案]
    B --> C[触发AI批改任务]
    C --> D[Celery队列处理]
    D --> E[AI模型批改]
    E --> F[生成批改结果]
    F --> G[更新作业状态]
    G --> H[教师查看批改结果]
    H --> I{是否需要人工调整}
    I -->|是| J[教师修改评分/批语]
    I -->|否| K[批改完成]
    J --> K
```

## 4. 功能优先级

### 4.1 高优先级（核心功能）

1. 用户认证与权限管理
   - 用户注册、登录、角色分配
   - 基于角色的访问控制
2. 题库管理
   - 题目的增删改查
   - 题目分类（学科、难度、标签）
   - Excel批量导入
3. 作业管理
   - 作业创建与发布
   - 学生作业提交
   - 作业状态跟踪
4. AI批改服务
   - 客观题自动批改
   - 主观题AI辅助批改
   - 批改结果生成

### 4.2 中优先级（增强功能）

1. 作业统计分析
   - 学生答题正确率统计
   - 知识点掌握度分析
   - 班级成绩分布
2. 通知系统
   - 作业发布通知
   - 批改完成通知
   - 系统消息推送
3. 题库共享
   - 教师间题库共享
   - 公共题库管理

### 4.3 低优先级（扩展功能）

1. 多模态支持
   - 图片题目OCR识别
   - 语音答案转录
   - 公式识别与解析
2. 学习路径推荐
   - 基于答题情况推荐学习资源
   - 个性化学习计划生成
3. 移动端适配
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

| 版本 | 日期       | 修改内容         | 修改人   |
|------|------------|------------------|----------|
| 1.0  | 2023-10-01 | 初稿             | 产品经理 |
| 1.1  | 2023-10-15 | 增加用户故事和流程图 | 产品经理 |
| 1.2  | 2023-10-20 | 调整功能优先级   | 产品经理 |

```


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
```

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
| 字段名        | 类型             | 约束                     | 描述             |
|---------------|------------------|--------------------------|------------------|
| id            | INT              | PK, AUTO_INCREMENT       | 用户ID           |
| username      | VARCHAR(100)     | UNIQUE, NOT NULL         | 用户名           |
| password_hash | VARCHAR(255)     | NOT NULL                 | 密码哈希         |
| name          | VARCHAR(100)     |                          | 真实姓名         |
| role          | ENUM('student','teacher','admin') | NOT NULL | 用户角色         |
| email         | VARCHAR(255)     | UNIQUE                   | 电子邮箱         |
| phone         | VARCHAR(20)      |                          | 手机号码         |
| register_time | DATETIME         | NOT NULL                 | 注册时间         |
| last_login    | DATETIME         |                          | 最后登录时间     |
| status        | TINYINT          | DEFAULT 1                | 状态(1:正常,0:禁用) |

#### 4.1.2 学科表（subjects）
| 字段名      | 类型         | 约束               | 描述       |
|-------------|--------------|--------------------|------------|
| id          | INT          | PK, AUTO_INCREMENT | 学科ID     |
| name        | VARCHAR(50)  | NOT NULL           | 学科名称   |
| code        | VARCHAR(20)  | UNIQUE             | 学科代码   |
| description | TEXT         |                    | 学科描述   |
| created_by  | INT          | FK(users.id)       | 创建人ID   |
| created_at  | DATETIME     | NOT NULL           | 创建时间   |

#### 4.1.3 题目表（questions）
| 字段名         | 类型                          | 约束               | 描述               |
|----------------|-------------------------------|--------------------|--------------------|
| id             | INT                           | PK, AUTO_INCREMENT | 题目ID             |
| subject_id     | INT                           | FK(subjects.id)    | 学科ID             |
| type_id        | INT                           | NOT NULL           | 题型ID             |
| content        | TEXT                          | NOT NULL           | 题干内容           |
| option_a       | VARCHAR(500)                  |                    | 选项A              |
| option_b       | VARCHAR(500)                  |                    | 选项B              |
| option_c       | VARCHAR(500)                  |                    | 选项C              |
| option_d       | VARCHAR(500)                  |                    | 选项D              |
| answer         | TEXT                          |                    | 标准答案           |
| explanation    | TEXT                          |                    | 解析               |
| difficulty     | ENUM('易','中','难','奥数')   | NOT NULL           | 难度               |
| tags           | VARCHAR(255)                  |                    | 标签(逗号分隔)     |
| image_url      | VARCHAR(500)                  |                    | 题目图片URL        |
| extra_json     | TEXT                          |                    | 扩展字段(JSON)     |
| created_by     | INT                           | FK(users.id)       | 创建人ID           |
| created_at     | DATETIME                      | NOT NULL           | 创建时间           |
| updated_at     | DATETIME                      | NOT NULL           | 更新时间           |

#### 4.1.4 作业表（homework）
| 字段名      | 类型                            | 约束               | 描述         |
|-------------|---------------------------------|--------------------|--------------|
| id          | INT                             | PK, AUTO_INCREMENT | 作业ID       |
| title       | VARCHAR(255)                    | NOT NULL           | 作业标题     |
| description | TEXT                            |                    | 作业描述     |
| teacher_id  | INT                             | FK(users.id)       | 教师ID       |
| start_time  | DATETIME                        | NOT NULL           | 开始时间     |
| end_time    | DATETIME                        | NOT NULL           | 截止时间     |
| status      | ENUM('draft','published','closed') | NOT NULL        | 状态         |
| created_at  | DATETIME                        | NOT NULL           | 创建时间     |

#### 4.1.5 作业分配表（homework_assignments）
| 字段名            | 类型                          | 约束                    | 描述               |
|-------------------|-------------------------------|-------------------------|--------------------|
| id                | INT                           | PK, AUTO_INCREMENT      | 分配ID             |
| homework_id       | INT                           | FK(homework.id)         | 作业ID             |
| student_id        | INT                           | FK(users.id)            | 学生ID             |
| question_id       | INT                           | FK(questions.id)        | 题目ID             |
| answer            | TEXT                          |                         | 学生答案           |
| answer_image_url  | VARCHAR(500)                  |                         | 答案图片URL        |
| score             | DECIMAL(5,2)                  |                         | 得分               |
| ai_explanation    | TEXT                          |                         | AI解析             |
| comment           | TEXT                          |                         | 教师批语           |
| submit_time       | DATETIME                      |                         | 提交时间           |
| review_time       | DATETIME                      |                         | 批改时间           |
| status            | ENUM('pending','submitted','reviewed') | NOT NULL      | 状态               |

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
```

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

```markdown
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

## 4. 作业管理

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

## 5. 查看成绩

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

```markdown
# 教育AI题库与作业系统部署文档



#### infra/k8s/rename_yaml_by_content.py

YAML文件重命名工具，根据文件内容自动分类和重命名

```python
import os
import re

src_dir = './generated_yaml_sections'
dst_dir = '../infra/k8s'
os.makedirs(dst_dir, exist_ok=True)

# 关键字与目标文件名映射
patterns = [
    (r'mariadb-config', 'mariadb-configmap.yaml'),
    (r'(kind:\s*Deployment[\s\S]*name:\s*mariadb|app:\s*mariadb)', 'mariadb-deployment.yaml'),
    (r'(kind:\s*Deployment[\s\S]*name:\s*redis|app:\s*redis)', 'redis-deployment.yaml'),
    (r'(kind:\s*Deployment[\s\S]*name:\s*backend|app:\s*backend)', 'backend-deployment.yaml'),
    (r'(kind:\s*Deployment[\s\S]*name:\s*frontend|app:\s*frontend)', 'frontend-deployment.yaml'),
    (r'kind:\s*Ingress', 'ingress.yaml'),
    (r'(kind:\s*Deployment[\s\S]*name:\s*celery-worker|app:\s*celery-worker)', 'celery-deployment.yaml'),
    (r'redis.conf', 'redis-persistent.yaml'),
    (r'ServiceMonitor', 'backend-monitor.yaml'),
    (r'NetworkPolicy', 'network-policy.yaml'),
    (r'kubernetes.io/tls', 'tls-secret.yaml'),
    (r'limit-rps', 'rate-limit.yaml'),
]

for fname in os.listdir(src_dir):
    if not fname.endswith('.yaml'):
        continue
    fpath = os.path.join(src_dir, fname)
    with open(fpath, encoding='utf-8') as f:
        content = f.read()
    new_name = None
    for pat, target in patterns:
        if re.search(pat, content, re.IGNORECASE):
            new_name = target
            break
    if not new_name:
        new_name = f'unknown_{fname}'
    dst_path = os.path.join(dst_dir, new_name)
    # 如果已存在则加编号
    base, ext = os.path.splitext(new_name)
    i = 2
    while os.path.exists(dst_path):
        dst_path = os.path.join(dst_dir, f'{base}_{i}{ext}')
        i += 1
    os.rename(fpath, dst_path)
    print(f'{fname} → {dst_path}')

print('批量重命名完成。')
```


#### infra/k8s/ingress_2.yaml

Kubernetes基础设施配置文件，用于部署和管理容器化应用的基础组件

```yaml
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


#### infra/k8s/tls-secret.yaml

Kubernetes基础设施配置文件，用于部署和管理容器化应用的基础组件

```yaml
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


#### infra/k8s/redis-persistent.yaml

Kubernetes基础设施配置文件，用于部署和管理容器化应用的基础组件

```yaml
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


#### infra/k8s/network-policy.yaml

Kubernetes基础设施配置文件，用于部署和管理容器化应用的基础组件

```yaml
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


#### infra/k8s/ingress.yaml

Kubernetes Ingress配置，定义了外部访问路由和SSL终止

```yaml
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


#### infra/k8s/mariadb-configmap_2.yaml

Kubernetes基础设施配置文件，用于部署和管理容器化应用的基础组件

```yaml
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


#### infra/k8s/mariadb-configmap.yaml

MariaDB数据库配置映射，包含数据库初始化和配置参数

```yaml
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
   ---
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


#### infra/k8s/redis-deployment.yaml

Redis缓存服务部署配置，用于会话存储和任务队列

```yaml
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

## 基础设施配置文件

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
```


### 3.2 生产环境架构

```

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

```

## 4. 部署步骤

### 4.1 开发环境部署 (Docker Compose)

#### 4.1.1 准备工作
1. 克隆项目代码
   ```bash
   git clone https://github.com/your-org/edu-ai-system.git
   cd edu-ai-system
   ```

2. 创建环境变量文件

   ```bash
   cp .env.example .env
   ```

   编辑.env文件，配置以下变量：

   ```bash
   DATABASE_URL=mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db
   CELERY_BROKER_URL=redis://redis:6379/0
   SECRET_KEY=your-secret-key-here
   NAS_MODEL_PATH=/mnt/nas/models
   ```

3. 创建必要的目录

   ```bash
   mkdir -p ./data/mysql
   mkdir -p ./data/redis
   mkdir -p ./models
   ```

4. 下载AI模型到./models目录

   ```bash
   # 示例：下载Gemma模型
   git lfs install
   git clone https://huggingface.co/google/gemma-2b-it ./models/gemma-2b-it
   ```

#### 4.1.2 启动服务

1. 构建并启动所有服务

   ```bash
   docker-compose up -d --build
   ```

2. 查看服务状态

   ```bash
   docker-compose ps
   ```

3. 查看日志

   ```bash
   docker-compose logs -f backend
   docker-compose logs -f frontend
   ```

4. 初始化数据库

   ```bash
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

```bash
docker-compose down
```

### 4.2 生产环境部署 (Kubernetes)

#### 4.2.1 准备工作

1. 安装和配置Kubernetes集群
   - 可以使用云服务商提供的Kubernetes服务（如EKS、GKE、ACK）
   - 或使用kubeadm自建集群

2. 安装kubectl并配置kubeconfig

   ```bash
   kubectl cluster-info
   ```

3. 安装Helm 3（可选，用于管理复杂应用）

   ```bash
   # 下载Helm
   curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
   sudo apt-get update
   sudo apt-get install helm
   ```

4. 准备NAS存储
   - 确保Kubernetes节点可以访问NAS
   - 创建PersistentVolume和PersistentVolumeClaim

#### 4.2.2 创建命名空间

```bash
kubectl create namespace edu-ai-system
```

#### 4.2.3 部署数据库

1. 创建MariaDB配置文件

   ```yaml
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

2. 创建MariaDB部署

   ```yaml
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
   ---
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

3. 创建数据库密码Secret

   ```bash
   kubectl create secret generic mariadb-secret --from-literal=root-password=yourpassword -n edu-ai-system
   ```

4. 应用配置

   ```bash
   kubectl apply -f mariadb-configmap.yaml
   kubectl apply -f mariadb-deployment.yaml
   ```

#### 4.2.4 部署Redis

```yaml
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

```bash
kubectl apply -f redis-deployment.yaml
```

#### 4.2.5 部署后端服务

1. 构建后端镜像并推送到镜像仓库

   ```Dockerfile
   # backend/Dockerfile
   FROM python:3.10-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   COPY backend /app/backend

   EXPOSE 8000

   CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

   ```bash
   # 构建镜像
   docker build -t your-registry/edu-ai-backend:latest ./backend

   # 推送到镜像仓库
   docker push your-registry/edu-ai-backend:latest
   ```

2. 创建后端部署配置

   ```yaml
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

3. 创建后端Secret

   ```bash
   kubectl create secret generic backend-secret --from-literal=secret-key=your-secret-key -n edu-ai-system
   kubectl create secret generic backend-secret --from-literal=DB_ROOT_PASSWORD=yourpassword -n edu-ai-system
   ```

4. 应用配置

   ```bash
   kubectl apply -f backend-deployment.yaml
   ```

#### 4.2.6 部署前端服务

1. 构建前端镜像并推送到镜像仓库

   ```Dockerfile
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

   ```bash
   # 构建镜像
   docker build -t your-registry/edu-ai-frontend:latest ./frontend

   # 推送到镜像仓库
   docker push your-registry/edu-ai-frontend:latest
   ```

2. 创建前端部署配置

   ```yaml
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

3. 应用配置

   ```bash
   kubectl apply -f frontend-deployment.yaml
   ```

#### 4.2.7 部署Ingress

```yaml
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

```bash
kubectl apply -f ingress.yaml
```

#### 4.2.8 部署Celery Worker

```yaml
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

```bash
kubectl apply -f celery-deployment.yaml
```

#### 4.2.9 初始化数据库

```bash
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

   ```bash
   kubectl get pods -n edu-ai-system
   ```

2. 检查服务状态

   ```bash
   kubectl get svc -n edu-ai-system
   ```

3. 检查Ingress状态

   ```bash
   kubectl get ingress -n edu-ai-system
   ```

4. 访问系统
   - 前端界面: https://ai.yourdomain.com
   - 后端API: https://ai.yourdomain.com/api
   - API文档: https://ai.yourdomain.com/api/docs

## 5. 配置说明

### 5.1 环境变量配置

#### 5.1.1 后端服务环境变量

| 变量名 | 描述 | 默认值 | 示例 |
|--------|------|--------|------|
| DATABASE_URL | 数据库连接字符串 | 无 | mysql+pymysql://root:password@mariadb:3306/edu_ai_db |
| CELERY_BROKER_URL | Celery消息代理URL | 无 | redis://redis:6379/0 |
| SECRET_KEY | JWT密钥 | 无 | your-secret-key-here |
| NAS_MODEL_PATH | NAS模型路径 | /mnt/nas/models | /mnt/nas/models |
| LOG_LEVEL | 日志级别 | INFO | DEBUG |
| MAX_CONTENT_LENGTH | 最大请求内容长度 | 10485760 | 20971520 |

#### 5.1.2 前端服务环境变量

| 变量名 | 描述 | 默认值 | 示例 |
|--------|------|--------|------|
| VITE_API_BASE_URL | API基础URL | /api | https://api.example.com |
| VITE_APP_TITLE | 应用标题 | 教育AI题库系统 | 我的题库系统 |
| VITE_APP_VERSION | 应用版本 | 2.1.0 | 2.1.0 |

### 5.2 数据库配置

#### 5.2.1 连接池配置

```python
# backend/database.py
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

```sql
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

```python
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

```yaml
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

```python
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

```python
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

   ```bash
   # 创建监控命名空间
   kubectl create namespace monitoring

   # 部署Prometheus
   helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring
   ```

2. 配置服务监控

   ```yaml
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

   ```bash
   # 创建日志命名空间
   kubectl create namespace logging

   # 部署Elasticsearch
   helm install elasticsearch elastic/elasticsearch -n logging

   # 部署Kibana
   helm install kibana elastic/kibana -n logging

   # 部署Fluentd
   helm install fluentd fluent/fluentd -n logging
   ```

2. 配置日志格式

   ```python
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

   ```bash
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

2. 创建定时任务

   ```bash
   # 编辑crontab
   crontab -e

   # 添加定时任务，每天凌晨2点执行备份
   0 2 * * * /path/to/backup-db.sh >> /var/log/db-backup.log 2>&1
   ```

### 7.2 数据库恢复

1. 创建恢复脚本

   ```bash
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

2. 执行恢复

   ```bash
   # 恢复最新备份
   ./restore-db.sh /mnt/nas/backups/edu_ai_db_20231001_020000.sql.gz

   # 恢复指定备份
   ./restore-db.sh /mnt/nas/backups/edu_ai_db_20231001_020000.sql.gz
   ```

### 7.3 模型文件备份

1. 使用rsync同步模型文件

   ```bash
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

2. 创建定时任务

   ```bash
   # 编辑crontab
   crontab -e

   # 添加定时任务，每周日凌晨1点执行备份
   0 1 * * 0 /path/to/backup-models.sh >> /var/log/models-backup.log 2>&1
   ```

## 8. 故障排查

### 8.1 常见问题及解决方案

#### 8.1.1 服务无法启动

问题: 后端服务启动失败，报错"数据库连接失败"

解决方案:

1. 检查数据库服务状态

   ```bash
   kubectl get pods -n edu-ai-system | grep mariadb
   ```

2. 检查数据库服务日志

   ```bash
   kubectl logs -f deployment/mariadb -n edu-ai-system
   ```

3. 检查数据库连接配置

   ```bash
   kubectl get secret backend-secret -n edu-ai-system -o yaml
   ```

4. 重新部署后端服务

   ```bash
   kubectl rollout restart deployment/backend -n edu-ai-system
   ```

#### 8.1.2 AI批改任务失败

问题: AI批改任务一直处于"pending"状态

解决方案:

1. 检查Celery Worker状态

   ```bash
   kubectl get pods -n edu-ai-system | grep celery
   ```

2. 检查Celery Worker日志

   ```bash
   kubectl logs -f deployment/celery-worker -n edu-ai-system
   ```

3. 检查Redis服务状态

   ```bash
   kubectl get pods -n edu-ai-system | grep redis
   ```

4. 检查Redis连接配置

   ```bash
   kubectl exec -it deployment/backend -n edu-ai-system -- env | grep CELERY
   ```

5. 重启Celery Worker

   ```bash
   kubectl rollout restart deployment/celery-worker -n edu-ai-system
   ```

#### 8.1.3 前端无法访问后端API

问题: 前端页面报错"Network Error"

解决方案:

1. 检查后端服务状态

   ```bash
   kubectl get pods -n edu-ai-system | grep backend
   ```

2. 检查后端服务日志

   ```bash
   kubectl logs -f deployment/backend -n edu-ai-system
   ```

3. 检查服务配置

   ```bash
   kubectl get svc -n edu-ai-system
   ```

4. 检查Ingress配置

   ```bash
   kubectl get ingress -n edu-ai-system
   ```

5. 检查CORS配置

   ```bash
   kubectl exec -it deployment/backend -n edu-ai-system -- cat /app/backend/main.py | grep -A 10 CORSMiddleware
   ```

### 8.2 日志分析

1. 收集所有服务日志

   ```bash
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

2. 分析错误日志

   ```bash
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

   ```python
   # backend/database.py
   engine = create_engine(
       DATABASE_URL,
       pool_size=20,         # 连接池大小
       max_overflow=30,      # 最大溢出连接数
       pool_recycle=3600,    # 连接回收时间(秒)
       pool_pre_ping=True    # 每次连接前ping一下
   )
   ```

2. 添加读写分离

   ```python
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

   ```python
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
   @cache(expire=1800)  # 缓存30分钟
   def get_questions(subject_id=None):
       # 查询数据库
       # ...
       return questions
   ```

2. 缓存AI模型

   ```python
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

   ```nginx
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

2. 启用浏览器缓存

   ```nginx
   # nginx.conf
   location ~* \.(jpg|jpeg|png|gif|ico|css|js|pdf|txt)$ {
       expires 7d;
       add_header Cache-Control "public, no-transform";
   }
   ```

3. 使用CDN加速静态资源

   ```html
   <!-- index.html -->
   <link rel="stylesheet" href="https://cdn.example.com/css/app.css">
   <script src="https://cdn.example.com/js/app.js"></script>
   ```

## 10. 安全加固

### 10.1 网络安全

1. 配置网络策略

   ```yaml
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

2. 启用TLS加密

   ```yaml
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

   ```nginx
   # nginx.conf
   add_header X-Frame-Options "SAMEORIGIN" always;
   add_header X-Content-Type-Options "nosniff" always;
   add_header X-XSS-Protection "1; mode=block" always;
   add_header Referrer-Policy "strict-origin-when-cross-origin" always;
   add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'" always;
   ```

2. 限制API请求频率

   ```yaml
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

3. 审计日志

   ```python
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

   ```sql
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

2. 敏感数据脱敏

   ```python
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

   ```bash
   # 备份数据库
   ./backup-db.sh

   # 备份模型文件
   ./backup-models.sh
   ```

2. 更新代码

   ```bash
   # 拉取最新代码
   git pull origin main

   # 更新子模块
   git submodule update --init --recursive
   ```

3. 更新依赖

   ```bash
   # 更新后端依赖
   cd backend
   pip install -r requirements.txt --upgrade

   # 更新前端依赖
   cd ../frontend
   npm update
   ```

4. 重新构建镜像

   ```bash
   # 构建后端镜像
   docker build -t your-registry/edu-ai-backend:latest ./backend
   docker push your-registry/edu-ai-backend:latest

   # 构建前端镜像
   docker build -t your-registry/edu-ai-frontend:latest ./frontend
   docker push your-registry/edu-ai-frontend:latest
   ```

5. 应用更新

   ```bash
   # 更新Kubernetes部署
   kubectl set image deployment/backend backend=your-registry/edu-ai-backend:latest -n edu-ai-system
   kubectl set image deployment/frontend frontend=your-registry/edu-ai-frontend:latest -n edu-ai-system
   kubectl set image deployment/celery-worker backend=your-registry/edu-ai-backend:latest -n edu-ai-system

   # 检查更新状态
   kubectl rollout status deployment/backend -n edu-ai-system
   kubectl rollout status deployment/frontend -n edu-ai-system
   kubectl rollout status deployment/celery-worker -n edu-ai-system
   ```

6. 数据库迁移

   ```bash
   # 在后端Pod中运行迁移
   kubectl exec -it deployment/backend -n edu-ai-system -- alembic upgrade head
   ```

7. 验证更新

   ```bash
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

   ```bash
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

2. 执行回滚
   ```bash
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
```

## 其他配置文件


#### .github/workflows/auto-review.yml

GitHub Actions自动审查工作流，用于代码质量检查和文档同步验证

```yaml
name: Auto Review Docs vs Code

on:
  pull_request:
    types: [opened, synchronize, reopened]
  push:
    branches: [main, master]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Clean generated files
        run: python scripts/cleanup_generated_files.py

      - name: Split Markdown docs
        run: python scripts/split_md_code_autosave.py

      - name: Auto Review
        run: python scripts/auto_review_md_vs_code.py
```



#### .github/workflows/auto-review.yml

GitHub Actions自动审查工作流，用于代码质量检查和文档同步验证

```yaml
name: Auto Review Docs vs Code

on:
  pull_request:
    types: [opened, synchronize, reopened]
  push:
    branches: [main, master]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Clean generated files
        run: python scripts/cleanup_generated_files.py

      - name: Split Markdown docs
        run: python scripts/split_md_code_autosave.py

      - name: Auto Review
        run: python scripts/auto_review_md_vs_code.py
```

## 自动化脚本和工具


#### scripts/sync_md_code_by_comment.py

项目自动化脚本，用于代码生成、文档同步、部署和维护等任务

```python
**正确的自动拆分脚本如下：**  
它会自动识别代码块语言和首行文件名注释，将代码保存到对应文件（自动补充扩展名）。

````python
import re
import os

md_path = '../docs/教育AI题库系统文档.md'
project_root = '..'

lang_ext = {
    'python': '.py',
    'javascript': '.js',
    'js': '.js',
    'vue': '.vue',
    'yaml': '.yaml',
    'yml': '.yml',
    'bash': '.sh',
    'plaintext': '.txt',
    'mermaid': '.mmd',
    'sql': '.sql',
    'markdown': '.md',
}

with open(md_path, encoding='utf-8') as f:
    md_content = f.read()

# 匹配代码块，提取语言和内容
pattern = r'```(\w+)\n(.*?)(?=```)'  # 只匹配代码块
matches = re.findall(pattern, md_content, re.DOTALL)

for lang, code in matches:
    lang = lang.strip().lower()
    code_lines = code.strip().splitlines()
    if not code_lines:
        continue
    # 文件名在首行注释，如 "# backend/database.py"
    first_line = code_lines[0].strip()
    file_match = re.match(r'#\s*([\w\-/\.]+)', first_line)
    if file_match:
        filename = file_match.group(1)
        ext = lang_ext.get(lang, '.txt')
        if not filename.endswith(ext):
            filename += ext
        abs_path = os.path.join(project_root, filename)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        # 去掉首行文件名注释
        code_to_write = '\n'.join(code_lines[1:]).strip() + '\n'
        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(code_to_write)
        print(f'已保存: {abs_path}')
```


#### scripts/repo_scanner.py

仓库文件扫描工具，用于分析项目结构和生成文件清单

```python
#!/usr/bin/env python3
"""
Repository Scanner for Auto Documentation Completion
Scans the repository for all code files and generates an inventory.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
import json

# 文件类型映射
FILE_TYPES = {
    '.py': 'python',
    '.js': 'javascript', 
    '.vue': 'vue',
    '.yaml': 'yaml',
    '.yml': 'yaml',
    '.json': 'json',
    '.md': 'markdown',
    '.sql': 'sql',
    '.sh': 'bash',
    '.dockerfile': 'dockerfile',
    '.txt': 'plaintext',
    '.mmd': 'mermaid'
}

# 目录分类
DIRECTORY_CATEGORIES = {
    'backend': ['backend', 'server', 'api'],
    'frontend': ['frontend', 'client', 'web', 'ui'],
    'infrastructure': ['k8s', 'kubernetes', 'infra', 'deploy', 'docker'],
    'scripts': ['scripts', 'tools', 'utils'],
    'docs': ['docs', 'documentation'],
    'config': ['config', 'conf', 'settings']
}

def get_file_category(file_path: str) -> str:
    """根据文件路径确定文件类别"""
    path_parts = Path(file_path).parts
    
    for category, keywords in DIRECTORY_CATEGORIES.items():
        for part in path_parts:
            if any(keyword in part.lower() for keyword in keywords):
                return category
    
    return 'other'

def get_file_type(file_path: str) -> str:
    """根据文件扩展名确定文件类型"""
    ext = Path(file_path).suffix.lower()
    return FILE_TYPES.get(ext, 'unknown')

def scan_repository(repo_root: str) -> Dict:
    """扫描仓库中的所有代码文件"""
    repo_path = Path(repo_root)
    file_inventory = {
        'summary': {
            'total_files': 0,
            'categories': {},
            'file_types': {}
        },
        'files': []
    }
    
    # 忽略的目录和文件
    ignore_patterns = {
        '.git', '__pycache__', 'node_modules', '.DS_Store', 
        '*.pyc', '*.log', '.vscode', '.idea'
    }
    
    for root, dirs, files in os.walk(repo_path):
        # 过滤忽略的目录
        dirs[:] = [d for d in dirs if d not in ignore_patterns]
        
        for file in files:
            # 跳过隐藏文件和忽略的文件
            if file.startswith('.') and file not in ['.gitignore', '.env.example']:
                continue
                
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, repo_root)
            
            # 跳过忽略的文件模式
            if any(pattern in file for pattern in ignore_patterns):
                continue
            
            file_type = get_file_type(file_path)
            if file_type == 'unknown':
                continue
                
            category = get_file_category(relative_path)
            
            file_info = {
                'path': relative_path,
                'absolute_path': file_path,
                'category': category,
                'type': file_type,
                'size': os.path.getsize(file_path),
                'is_documented': False  # 后续会更新
            }
            
            file_inventory['files'].append(file_info)
            
            # 更新统计信息
            file_inventory['summary']['total_files'] += 1
            file_inventory['summary']['categories'][category] = \
                file_inventory['summary']['categories'].get(category, 0) + 1
            file_inventory['summary']['file_types'][file_type] = \
                file_inventory['summary']['file_types'].get(file_type, 0) + 1
    
    return file_inventory

def read_file_content(file_path: str) -> str:
    """安全读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='gb2312') as f:
                return f.read()
        except:
            return f"# 无法读取文件内容 (编码问题): {file_path}"
    except Exception as e:
        return f"# 读取文件失败: {e}"

def generate_file_description(file_info: Dict) -> str:
    """为文件生成描述"""
    category = file_info['category']
    file_type = file_info['type']
    path = file_info['path']
    
    descriptions = {
        'backend': {
            'python': '后端Python源码文件',
            'yaml': '后端部署配置文件',
            'json': '后端配置文件'
        },
        'frontend': {
            'javascript': '前端JavaScript文件',
            'vue': '前端Vue组件文件',
            'json': '前端配置文件'
        },
        'infrastructure': {
            'yaml': 'Kubernetes部署配置文件',
            'python': '基础设施管理脚本'
        },
        'scripts': {
            'python': '自动化脚本文件',
            'bash': 'Shell脚本文件'
        },
        'docs': {
            'markdown': '项目文档文件'
        }
    }
    
    if category in descriptions and file_type in descriptions[category]:
        return descriptions[category][file_type]
    
    return f"{category}目录下的{file_type}文件"

def main():
    """主函数"""
    repo_root = '/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank'
    
    print("🔍 正在扫描仓库文件...")
    inventory = scan_repository(repo_root)
    
    print(f"\n📊 扫描结果统计:")
    print(f"总文件数: {inventory['summary']['total_files']}")
    
    print(f"\n📁 按类别分布:")
    for category, count in inventory['summary']['categories'].items():
        print(f"  {category}: {count} 个文件")
    
    print(f"\n📄 按文件类型分布:")
    for file_type, count in inventory['summary']['file_types'].items():
        print(f"  {file_type}: {count} 个文件")
    
    print(f"\n📋 详细文件清单:")
    for file_info in sorted(inventory['files'], key=lambda x: (x['category'], x['path'])):
        print(f"  [{file_info['category']}] {file_info['path']} ({file_info['type']})")
    
    # 保存扫描结果
    output_file = os.path.join(repo_root, 'scripts', 'repo_inventory.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 扫描结果已保存到: {output_file}")
    
    return inventory

if __name__ == "__main__":
    main()
```


#### scripts/sync_md_code_autoext.py

项目自动化脚本，用于代码生成、文档同步、部署和维护等任务

```python
import re
import os

md_path = 'docs/教育AI题库系统文档.md'
project_root = '.'  # 项目根目录

# 代码块语言到扩展名映射
lang_ext = {
    'python': '.py',
    'javascript': '.js',
    'js': '.js',
    'vue': '.vue',
    'yaml': '.yaml',
    'yml': '.yml',
    'bash': '.sh',
    'plaintext': '.txt',
    'mermaid': '.mmd',
    'sql': '.sql',
    'markdown': '.md',
}

# 支持常见代码块前缀格式
patterns = [
    r'####\s*([^\n]+)\n```(\w+)\n(.*?)```',
    r'文件名[:：] *([^\n]+)\n```(\w+)\n(.*?)```',
    r'#\s*([^\n]+)\n```(\w+)\n(.*?)```',
]

with open(md_path, encoding='utf-8') as f:
    md_content = f.read()

blocks = []
for pattern in patterns:
    for match in re.findall(pattern, md_content, re.DOTALL):
        filename, lang, code = match
        filename = filename.strip()
        lang = lang.strip().lower()
        code = code.strip()
        # 自动补充扩展名
        ext = lang_ext.get(lang, '.txt')
        if not filename.endswith(ext):
            filename += ext
        blocks.append({
            "filename": filename,
            "lang": lang,
            "code": code
        })

for block in blocks:
    rel_path = block["filename"]
    abs_path = os.path.join(project_root, rel_path)
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    with open(abs_path, 'w', encoding='utf-8') as f:
        f.write(block["code"] + '\n')
    print(f'已保存: {abs_path}')
```


#### scripts/md_code_progress_report.py

项目自动化脚本，用于代码生成、文档同步、部署和维护等任务

```python
import re
import os
import difflib
import csv

md_path = '../docs/教育AI题库系统文档.md'
project_root = '../'
report_md = 'code_progress_report.md'
report_csv = 'code_progress_report.csv'

# 支持多种标记格式
patterns = [
    r'# 文件名[:：] *([^\n]+)\n```(\w+)\n(.*?)```',
    r'## *([^\n]+)\n```(\w+)\n(.*?)```',
    r'文件名[:：] *([^\n]+)\n```(\w+)\n(.*?)```',
    r'### *([^\n]+)\n```(\w+)\n(.*?)```',
    r'#### *([^\n]+)\n```(\w+)\n(.*?)```',
]

md_blocks = []
with open(md_path, encoding='utf-8') as f:
    md_content = f.read()
for pattern in patterns:
    for match in re.findall(pattern, md_content, re.DOTALL):
        filename, lang, code = match
        md_blocks.append({
            "filename": filename.strip(),
            "lang": lang,
            "code": code.strip()
        })

results = []
for block in md_blocks:
    rel_path = block["filename"]
    abs_path = os.path.join(project_root, rel_path)
    status = ""
    detail = ""
    md_code = block["code"]

    need_fix = False
    if os.path.isfile(abs_path):
        with open(abs_path, encoding='utf-8') as f:
            actual_code = f.read().strip()
        if actual_code == md_code:
            status = "✅ 完全一致"
            detail = ""
        else:
            ratio = difflib.SequenceMatcher(None, md_code, actual_code).ratio()
            status = f"⚠️ 不一致（已自动修复，相似度 {ratio:.2f}）"
            diff = '\n'.join(list(difflib.unified_diff(md_code.splitlines(), actual_code.splitlines(), lineterm='', n=3)))
            detail = diff[:200] + "..." if len(diff) > 200 else diff
            need_fix = True
    else:
        status = "❌ 缺失（已自动修复）"
        detail = ""
        need_fix = True

    # 自动修复
    if need_fix:
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(md_code + '\n')

    results.append({
        "文件名": rel_path,
        "语言": block["lang"],
        "状态": status,
        "相似度/差异": detail
    })

# 生成 Markdown 报表
with open(report_md, 'w', encoding='utf-8') as f:
    f.write("| 文件名 | 状态 | 语言 | 相似度/差异 |\n")
    f.write("|---|---|---|---|\n")
    for row in results:
        f.write(f"| {row['文件名']} | {row['状态']} | {row['语言']} | {row['相似度/差异'].replace('|', '\\|')[:100]} |\n")

# 生成 CSV 报表
with open(report_csv, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["文件名", "状态", "语言", "相似度/差异"])
    for row in results:
        writer.writerow([row['文件名'], row['状态'], row['语言'], row['相似度/差异'][:100]])

print(f"已生成进度报表：{report_md} 和 {report_csv}")
print("所有不一致或缺失文件已自动修复。")
```


#### scripts/5.2.2 索引优化.sql

SQL数据库脚本，用于数据库结构优化、索引创建和数据维护

```sql
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


#### scripts/split_md_code_autosave.py

项目自动化脚本，用于代码生成、文档同步、部署和维护等任务

```python
import re
import os

md_files = [
    '../docs/系统UI设计方案文档.md',
    '../docs/教育AI全栈设计方案.md',
    '../docs/教育AI题库系统文档.md'
]
project_root = '../'

lang_ext = {
    'python': '.py',
    'javascript': '.js',
    'vue': '.vue',
    'yaml': '.yaml',
    'plaintext': '.txt',
    'mermaid': '.mmd',
    'json': '.json'
}

def auto_dir(filename):
    # 只要是带目录的文件名，直接拼接到 project_root
    if '/' in filename or filename.endswith(('.yml', '.yaml')):
        return os.path.join(project_root, filename)
    else:
        return os.path.join(project_root, 'misc', filename)

patterns = [
    r'[#]{1,3} ?文件名[:：] *([^\n]+)\n```(\w+)\n(.*?)```',
    r'[#]{1,3} ?([^\n]+)\n```(\w+)\n(.*?)```',
]

generated_files = []

for md_path in md_files:
    if not os.path.isfile(md_path):
        print(f"未找到文档: {md_path}")
        continue
    with open(md_path, encoding='utf-8') as f:
        content = f.read()

    found = {}
    for pattern in patterns:
        for match in re.findall(pattern, content, re.DOTALL):
            filename, lang, code = match
            filename = re.sub(r'^[# ]+', '', filename.strip())
            # 只过滤非法字符，不替换 /
            filename = re.sub(r'[:*?"<>|]', '_', filename)
            ext = lang_ext.get(lang.lower(), '.txt')
            if not filename.endswith(ext):
                filename += ext
            path = auto_dir(filename)
            if path not in found:
                found[path] = []
            found[path].append(code.strip())

    for path, codes in found.items():
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(codes))
        print(f'已保存: {path}，包含 {len(codes)} 段代码')
        generated_files.append(os.path.relpath(path, project_root))

# 自动生成文件树
def print_tree(paths):
    tree = {}
    for p in paths:
        parts = p.split(os.sep)
        cur = tree
        for part in parts:
            cur = cur.setdefault(part, {})
    def _print(cur, prefix=''):
        for k, v in cur.items():
            print(prefix + '├── ' + k)
            _print(v, prefix + '│   ')
    print("\n生成文件树：")
    _print(tree, '')

print_tree(generated_files)
```


#### scripts/4.2.9 初始化数据库.sh

系统运维Shell脚本，用于服务管理、数据库操作和系统维护

```bash
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


#### scripts/4.1.4 停止服务.sh

系统运维Shell脚本，用于服务管理、数据库操作和系统维护

```bash
docker-compose down
```


#### scripts/4.2.2 创建命名空间.sh

系统运维Shell脚本，用于服务管理、数据库操作和系统维护

```bash
kubectl create namespace edu-ai-system
```


#### scripts/sync_md_code.py

文档代码同步工具，将文档中的代码块同步到实际文件

```python
import re
import os

md_path = '../docs/教育AI题库系统文档.md'
project_root = '.'  # 当前项目根目录

# 支持常见代码块前缀格式
patterns = [
    r'####\s*([^\n]+)\n```(\w+)\n(.*?)```',
    r'文件名[:：] *([^\n]+)\n```(\w+)\n(.*?)```',
]

with open(md_path, encoding='utf-8') as f:
    md_content = f.read()

blocks = []
for pattern in patterns:
    for match in re.findall(pattern, md_content, re.DOTALL):
        filename, lang, code = match
        blocks.append({
            "filename": filename.strip(),
            "lang": lang,
            "code": code.strip()
        })

for block in blocks:
    rel_path = block["filename"]
    abs_path = os.path.join(project_root, rel_path)
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    with open(abs_path, 'w', encoding='utf-8') as f:
        f.write(block["code"] + '\n')
    print(f'已覆盖保存: {abs_path}')
```


#### scripts/auto_review_md_vs_code.py

文档代码一致性检查工具，对比文档中的代码块与实际文件

```python
import re
import os
import difflib
import sys

md_files = [
    '../docs/系统UI设计方案文档.md',
    '../docs/教育AI全栈设计方案.md',
    '../docs/教育AI题库系统文档.md'
]
output_root = '../generated'
report_md = 'auto_review_report.md'
lang_ext = {
    'python': '.py',
    'javascript': '.js',
    'vue': '.vue',
    'yaml': '.yaml',
    'plaintext': '.txt',
    'mermaid': '.mmd',
    'json': '.json'
}

patterns = [
    r'[#]{1,3} ?文件名[:：] *([^\n]+)\n```(\w+)\n(.*?)```',
    r'[#]{1,3} ?([^\n]+)\n```(\w+)\n(.*?)```',
]

md_blocks = []
for md_path in md_files:
    if not os.path.isfile(md_path):
        continue
    with open(md_path, encoding='utf-8') as f:
        content = f.read()
    for pattern in patterns:
        for match in re.findall(pattern, content, re.DOTALL):
            filename, lang, code = match
            filename = filename.strip()
            filename = re.sub(r'^[# ]+', '', filename)
            filename = re.sub(r'[\\/:*?"<>|]', '_', filename)
            ext = lang_ext.get(lang.lower(), '.txt')
            if not filename.endswith(ext):
                filename += ext
            md_blocks.append({
                "filename": filename,
                "lang": lang,
                "code": code.strip()
            })

results = []
errors = []

for block in md_blocks:
    rel_path = block["filename"]
    abs_path = os.path.join(output_root, rel_path)
    md_code = block["code"]

    try:
        if os.path.isfile(abs_path):
            with open(abs_path, encoding='utf-8') as f:
                actual_code = f.read().strip()
            if actual_code == md_code:
                status = "✅ 完全一致"
            else:
                ratio = difflib.SequenceMatcher(None, md_code, actual_code).ratio()
                status = f"⚠️ 不一致（相似度 {ratio:.2f}）"
                errors.append(f"{rel_path} 内容不一致，相似度 {ratio:.2f}")
        else:
            status = "❌ 缺失"
            errors.append(f"{rel_path} 缺失")
    except Exception as e:
        status = f"❌ 读取失败: {e}"
        errors.append(f"{rel_path} 读取失败: {e}")

    results.append({
        "文件名": rel_path,
        "语言": block["lang"],
        "状态": status,
    })

with open(report_md, 'w', encoding='utf-8') as f:
    f.write("| 文件名 | 状态 | 语言 |\n|---|---|---|\n")
    for row in results:
        f.write(f"| {row['文件名']} | {row['状态']} | {row['语言']} |\n")

if errors:
    print("自动审核未通过：")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)
else:
    print("自动审核全部通过 ✅ ")
    sys.exit(0)
```


#### scripts/split_md_code_advanced.py

项目自动化脚本，用于代码生成、文档同步、部署和维护等任务

```python
import re
import os

md_path = '../docs/教育AI题库系统文档.md'
output_root = '../'

with open(md_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 支持 "#### backend/main.py" 或 "#### frontend/src/api/index.js" 这种格式
pattern = r'####\s*([^\n]+)\n```(\w+)\n(.*?)```'
matches = re.findall(pattern, content, re.DOTALL)

for filename, lang, code in matches:
    file_path = os.path.join(output_root, filename.strip())
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(code.strip() + '\n')
    print(f'已保存: {file_path}')
```


#### scripts/4.2.9 初始化数据库.sh

系统运维Shell脚本，用于服务管理、数据库操作和系统维护

```bash
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


#### scripts/auto_doc_integration.py

项目自动化脚本，用于代码生成、文档同步、部署和维护等任务

```python
#!/usr/bin/env python3
"""
Auto Documentation Completion - Integration Script
完整的自动文档补全流程，包括扫描、分析和更新
"""

import os
import sys
import json
from datetime import datetime

def run_command(command, description):
    """运行命令并显示进度"""
    print(f"🔄 {description}...")
    result = os.system(command)
    if result == 0:
        print(f"✅ {description} - 完成")
        return True
    else:
        print(f"❌ {description} - 失败")
        return False

def main():
    """主流程"""
    print("🚀 教育AI题库系统 - 自动文档补全系统")
    print("=" * 50)
    
    repo_root = '/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank'
    os.chdir(repo_root)
    
    # 步骤1：扫描仓库文件
    if not run_command("python scripts/repo_scanner.py", "扫描仓库文件结构"):
        sys.exit(1)
    
    # 步骤2：分析文档状态
    if not run_command("python scripts/doc_parser.py", "分析文档化状态"):
        sys.exit(1)
    
    # 步骤3：自动补全文档
    if not run_command("python scripts/auto_doc_completion.py", "执行文档自动补全"):
        sys.exit(1)
    
    # 步骤4：验证结果
    print("\n🔍 验证补全结果...")
    if not run_command("python scripts/doc_parser.py > /tmp/final_status.txt", "重新分析文档状态"):
        sys.exit(1)
    
    # 显示最终统计
    print("\n📊 补全结果统计:")
    
    try:
        with open('scripts/auto_completion_report.json', 'r', encoding='utf-8') as f:
            report = json.load(f)
        
        print(f"  处理时间: {report['timestamp']}")
        print(f"  处理文件数: {report['processed_files']}")
        print(f"  更新文档数: {len(report['updated_docs'])}")
        
        print(f"\n📝 更新的文档:")
        for doc_path, info in report['updated_docs'].items():
            print(f"  - {doc_path}: +{info['files_added']} 个文件")
        
        print(f"\n📁 按类别分布:")
        for category, files in report['files_by_category'].items():
            print(f"  - {category}: {len(files)} 个文件")
    
    except Exception as e:
        print(f"⚠️ 无法读取补全报告: {e}")
    
    print("\n✅ 自动文档补全流程完成!")
    print("\n📋 下一步建议:")
    print("1. 检查更新后的文档内容是否准确")
    print("2. 提交更改作为 Pull Request")
    print("3. 团队审核文档补全结果")
    print("4. 考虑添加更多详细说明和使用示例")
    
    return True

if __name__ == "__main__":
    main()
```


#### scripts/auto_doc_completion.py

项目自动化脚本，用于代码生成、文档同步、部署和维护等任务

```python
#!/usr/bin/env python3
"""
Auto Documentation Completion Engine
Automatically adds missing code files to documentation with descriptions and code blocks.
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from datetime import datetime

class AutoDocumentationEngine:
    def __init__(self, repo_root: str):
        self.repo_root = repo_root
        self.main_docs = {
            'docs/教育AI题库系统文档.md': 'system',
            'docs/教育AI全栈设计方案.md': 'design', 
            'docs/系统UI设计方案文档.md': 'ui'
        }
        
        # 文件分类到文档的映射
        self.file_to_doc_mapping = {
            'backend': 'docs/教育AI全栈设计方案.md',
            'frontend': 'docs/系统UI设计方案文档.md',
            'infrastructure': 'docs/教育AI题库系统文档.md',
            'scripts': 'docs/教育AI题库系统文档.md',
            'docs': None,  # 不自动添加文档文件到文档中
            'other': 'docs/教育AI题库系统文档.md'
        }

    def load_analysis_data(self) -> Tuple[Dict, Dict]:
        """加载分析数据"""
        inventory_file = os.path.join(self.repo_root, 'scripts', 'repo_inventory.json')
        analysis_file = os.path.join(self.repo_root, 'scripts', 'doc_analysis.json')
        
        with open(inventory_file, 'r', encoding='utf-8') as f:
            inventory = json.load(f)
        
        with open(analysis_file, 'r', encoding='utf-8') as f:
            analysis = json.load(f)
        
        return inventory, analysis

    def generate_file_description(self, file_info: Dict) -> str:
        """为文件生成中文描述"""
        category = file_info['category']
        file_type = file_info['type']
        file_path = file_info['path']
        
        # 基于文件路径和类型的描述模板
        descriptions = {
            'backend': {
                'yaml': 'Kubernetes后端服务部署配置文件，定义了后端应用的部署规范、服务配置和网络策略',
            },
            'frontend': {
                'yaml': 'Kubernetes前端服务部署配置文件，定义了前端应用的部署规范和负载均衡配置',
                'markdown': '前端UI系统设计文档，包含组件设计、样式规范和交互流程'
            },
            'infrastructure': {
                'yaml': 'Kubernetes基础设施配置文件，用于部署和管理容器化应用的基础组件',
                'python': '基础设施管理和自动化脚本，用于部署、配置和维护系统组件'
            },
            'scripts': {
                'python': '项目自动化脚本，用于代码生成、文档同步、部署和维护等任务',
                'bash': '系统运维Shell脚本，用于服务管理、数据库操作和系统维护',
                'sql': 'SQL数据库脚本，用于数据库结构优化、索引创建和数据维护',
                'markdown': '脚本使用说明和运行报告文档'
            },
            'other': {
                'yaml': 'CI/CD工作流配置文件，定义了自动化构建、测试和部署流程',
                'markdown': '项目相关的说明文档和报告文件'
            }
        }
        
        # 基于具体文件名的特殊描述
        special_descriptions = {
            'repo_scanner.py': '仓库文件扫描工具，用于分析项目结构和生成文件清单',
            'doc_parser.py': '文档解析工具，用于分析文档结构和识别文档化状态',
            'auto_review_md_vs_code.py': '文档代码一致性检查工具，对比文档中的代码块与实际文件',
            'sync_md_code.py': '文档代码同步工具，将文档中的代码块同步到实际文件',
            'rename_yaml_by_content.py': 'YAML文件重命名工具，根据文件内容自动分类和重命名',
            'ingress.yaml': 'Kubernetes Ingress配置，定义了外部访问路由和SSL终止',
            'redis-deployment.yaml': 'Redis缓存服务部署配置，用于会话存储和任务队列',
            'mariadb-configmap.yaml': 'MariaDB数据库配置映射，包含数据库初始化和配置参数',
            'auto-review.yml': 'GitHub Actions自动审查工作流，用于代码质量检查和文档同步验证'
        }
        
        # 获取文件名
        filename = Path(file_path).name
        
        # 检查特殊描述
        if filename in special_descriptions:
            return special_descriptions[filename]
        
        # 使用通用描述
        if category in descriptions and file_type in descriptions[category]:
            return descriptions[category][file_type]
        
        # 默认描述
        return f"{category}目录下的{file_type}文件，{filename}"

    def read_file_content(self, file_path: str) -> str:
        """安全读取文件内容"""
        abs_path = os.path.join(self.repo_root, file_path)
        try:
            with open(abs_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return content.strip()
        except UnicodeDecodeError:
            try:
                with open(abs_path, 'r', encoding='gb2312') as f:
                    content = f.read()
                return content.strip()
            except:
                return f"# 文件编码问题，无法读取: {file_path}"
        except Exception as e:
            return f"# 读取文件失败: {e}"

    def get_language_from_extension(self, file_path: str) -> str:
        """根据文件扩展名获取代码块语言"""
        ext_mapping = {
            '.py': 'python',
            '.js': 'javascript',
            '.vue': 'vue',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.json': 'json',
            '.md': 'markdown',
            '.sql': 'sql',
            '.sh': 'bash',
            '.txt': 'plaintext',
            '.mmd': 'mermaid'
        }
        
        ext = Path(file_path).suffix.lower()
        return ext_mapping.get(ext, 'plaintext')

    def generate_documentation_section(self, file_info: Dict) -> str:
        """为文件生成文档章节"""
        file_path = file_info['path']
        description = self.generate_file_description(file_info)
        content = self.read_file_content(file_path)
        language = self.get_language_from_extension(file_path)
        
        # 生成文档章节
        section = f"""

#### {file_path}

{description}

```{language}
{content}
```
"""
        return section

    def find_insertion_point(self, doc_content: str, category: str) -> int:
        """找到插入新章节的位置"""
        # 为不同类别的文件找到合适的插入位置
        insertion_patterns = {
            'infrastructure': [
                r'## 4\. 部署文档',
                r'### 4\.2 生产环境部署',
                r'## 部署',
                r'## k8s',
                r'## Kubernetes'
            ],
            'scripts': [
                r'## 脚本',
                r'## 工具',
                r'## 自动化',
                r'## 维护',
                r'$'  # 文档末尾
            ],
            'backend': [
                r'## 后端',
                r'## backend',
                r'## 核心文件实现',
                r'### 1\. 后端核心文件'
            ],
            'frontend': [
                r'## 前端',
                r'## frontend',
                r'## UI',
                r'## 组件'
            ],
            'other': [
                r'## 其他',
                r'## 配置',
                r'$'  # 文档末尾
            ]
        }
        
        patterns = insertion_patterns.get(category, [r'$'])
        
        for pattern in patterns:
            if pattern == '$':
                return len(doc_content)
            
            match = re.search(pattern, doc_content, re.MULTILINE)
            if match:
                # 找到下一个同级或更高级标题的位置
                section_start = match.start()
                remaining_content = doc_content[section_start:]
                
                # 查找下一个同级标题
                next_section = re.search(r'\n## ', remaining_content)
                if next_section:
                    return section_start + next_section.start()
                else:
                    return len(doc_content)
        
        # 如果没有找到合适的位置，插入到末尾
        return len(doc_content)

    def add_section_header_if_needed(self, doc_content: str, category: str) -> str:
        """如果需要，添加新的章节标题"""
        section_headers = {
            'infrastructure': '## 基础设施配置文件',
            'scripts': '## 自动化脚本和工具',
            'other': '## 其他配置文件'
        }
        
        header = section_headers.get(category)
        if not header:
            return doc_content
        
        # 检查是否已存在相应的章节
        if re.search(header.replace('##', r'##\s*'), doc_content):
            return doc_content
        
        # 在合适的位置添加章节标题
        insertion_point = self.find_insertion_point(doc_content, category)
        
        new_section = f"\n\n{header}\n"
        new_content = (doc_content[:insertion_point] + 
                      new_section + 
                      doc_content[insertion_point:])
        
        return new_content

    def update_documentation(self, undocumented_files: List[Dict]) -> Dict:
        """更新文档，添加未文档化的文件"""
        updates = {}
        
        # 按文档分组文件
        files_by_doc = {}
        for file_info in undocumented_files:
            category = file_info['category']
            target_doc = self.file_to_doc_mapping.get(category)
            
            if target_doc and target_doc in self.main_docs:
                if target_doc not in files_by_doc:
                    files_by_doc[target_doc] = []
                files_by_doc[target_doc].append(file_info)
        
        # 更新每个文档
        for doc_path, files in files_by_doc.items():
            abs_doc_path = os.path.join(self.repo_root, doc_path)
            
            if not os.path.exists(abs_doc_path):
                print(f"⚠️ 文档文件不存在: {doc_path}")
                continue
            
            # 读取原始文档
            with open(abs_doc_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            updated_content = original_content
            
            # 按类别分组文件
            files_by_category = {}
            for file_info in files:
                category = file_info['category']
                if category not in files_by_category:
                    files_by_category[category] = []
                files_by_category[category].append(file_info)
            
            # 为每个类别添加文件
            for category, category_files in files_by_category.items():
                # 添加章节标题（如果需要）
                updated_content = self.add_section_header_if_needed(updated_content, category)
                
                # 为每个文件生成文档章节
                for file_info in category_files:
                    section = self.generate_documentation_section(file_info)
                    
                    # 找到插入位置
                    insertion_point = self.find_insertion_point(updated_content, category)
                    
                    # 插入新章节
                    updated_content = (updated_content[:insertion_point] + 
                                     section + 
                                     updated_content[insertion_point:])
            
            # 保存更新的文档
            backup_path = abs_doc_path + f'.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
            
            # 创建备份
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            # 保存更新
            with open(abs_doc_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            updates[doc_path] = {
                'files_added': len(files),
                'backup_created': backup_path,
                'categories': list(files_by_category.keys())
            }
            
            print(f"✅ 已更新文档: {doc_path}")
            print(f"   添加文件: {len(files)} 个")
            print(f"   备份创建: {backup_path}")
        
        return updates

def main():
    """主函数"""
    repo_root = '/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank'
    
    # 初始化引擎
    engine = AutoDocumentationEngine(repo_root)
    
    # 加载分析数据
    try:
        inventory, analysis = engine.load_analysis_data()
    except FileNotFoundError as e:
        print(f"❌ 请先运行 repo_scanner.py 和 doc_parser.py: {e}")
        return
    
    # 获取未文档化的文件
    undocumented_files = []
    existing_files = {f['path']: f for f in inventory['files']}
    
    for file_path in analysis['comparison']['existing_but_undocumented']:
        if file_path in existing_files:
            undocumented_files.append(existing_files[file_path])
    
    # 过滤掉不需要自动文档化的文件（如文档文件本身）
    filtered_files = [
        f for f in undocumented_files 
        if f['category'] != 'docs' and not f['path'].endswith('.md')
    ]
    
    print(f"🚀 开始自动补全文档...")
    print(f"📊 将处理 {len(filtered_files)} 个未文档化的文件")
    
    # 按类别显示文件
    categories = {}
    for f in filtered_files:
        cat = f['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(f['path'])
    
    for category, files in categories.items():
        print(f"  [{category}] {len(files)} 个文件")
    
    # 执行文档更新
    updates = engine.update_documentation(filtered_files)
    
    print(f"\n✅ 文档自动补全完成!")
    print(f"📝 更新了 {len(updates)} 个文档文件:")
    
    for doc_path, info in updates.items():
        print(f"  {doc_path}: 添加了 {info['files_added']} 个文件")
    
    # 保存更新报告
    report_file = os.path.join(repo_root, 'scripts', 'auto_completion_report.json')
    report = {
        'timestamp': datetime.now().isoformat(),
        'processed_files': len(filtered_files),
        'updated_docs': updates,
        'files_by_category': categories
    }
    
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n📄 更新报告已保存到: {report_file}")

if __name__ == "__main__":
    main()
```


#### scripts/4.2.2 创建命名空间.sh

系统运维Shell脚本，用于服务管理、数据库操作和系统维护

```bash
kubectl create namespace edu-ai-system
```


#### scripts/auto_completion_report.json

scripts目录下的json文件，auto_completion_report.json

```json
{
  "timestamp": "2025-08-26T03:21:10.674502",
  "processed_files": 26,
  "updated_docs": {
    "docs/教育AI题库系统文档.md": {
      "files_added": 22,
      "backup_created": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/docs/教育AI题库系统文档.md.backup_20250826_032110",
      "categories": [
        "infrastructure",
        "other",
        "scripts"
      ]
    },
    "docs/教育AI全栈设计方案.md": {
      "files_added": 3,
      "backup_created": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/docs/教育AI全栈设计方案.md.backup_20250826_032110",
      "categories": [
        "backend"
      ]
    },
    "docs/系统UI设计方案文档.md": {
      "files_added": 1,
      "backup_created": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/docs/系统UI设计方案文档.md.backup_20250826_032110",
      "categories": [
        "frontend"
      ]
    }
  },
  "files_by_category": {
    "infrastructure": [
      "infra/k8s/rename_yaml_by_content.py",
      "infra/k8s/ingress_2.yaml",
      "infra/k8s/tls-secret.yaml",
      "infra/k8s/redis-persistent.yaml",
      "infra/k8s/network-policy.yaml",
      "infra/k8s/ingress.yaml",
      "infra/k8s/mariadb-configmap_2.yaml",
      "infra/k8s/mariadb-configmap.yaml",
      "infra/k8s/redis-deployment.yaml"
    ],
    "other": [
      ".github/workflows/auto-review.yml"
    ],
    "scripts": [
      "scripts/sync_md_code_by_comment.py",
      "scripts/repo_scanner.py",
      "scripts/sync_md_code_autoext.py",
      "scripts/md_code_progress_report.py",
      "scripts/5.2.2 索引优化.sql",
      "scripts/split_md_code_autosave.py",
      "scripts/4.2.9 初始化数据库.sh",
      "scripts/4.1.4 停止服务.sh",
      "scripts/4.2.2 创建命名空间.sh",
      "scripts/sync_md_code.py",
      "scripts/auto_review_md_vs_code.py",
      "scripts/split_md_code_advanced.py"
    ],
    "backend": [
      "infra/k8s/backend-deployment_2.yaml",
      "infra/k8s/backend-deployment_3.yaml",
      "infra/k8s/backend-deployment.yaml"
    ],
    "frontend": [
      "infra/k8s/frontend-deployment.yaml"
    ]
  }
}
```


#### scripts/5.2.2 索引优化.sql

SQL数据库脚本，用于数据库结构优化、索引创建和数据维护

```sql
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


#### scripts/doc_parser.py

文档解析工具，用于分析文档结构和识别文档化状态

```python
#!/usr/bin/env python3
"""
Documentation Parser for Auto Documentation Completion
Parses existing documentation to identify documented vs missing code files.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple

class DocumentationParser:
    def __init__(self, repo_root: str):
        self.repo_root = repo_root
        self.doc_files = [
            'docs/教育AI题库系统文档.md',
            'docs/教育AI全栈设计方案.md', 
            'docs/系统UI设计方案文档.md'
        ]
        
        # 匹配代码块的正则模式
        self.code_block_patterns = [
            r'####\s*([^\n]+)\n```(\w+)\n(.*?)```',  # #### filename
            r'###\s*([^\n]+)\n```(\w+)\n(.*?)```',   # ### filename
            r'##\s*([^\n]+)\n```(\w+)\n(.*?)```',    # ## filename
            r'文件名[:：]\s*([^\n]+)\n```(\w+)\n(.*?)```',  # 文件名: filename
            r'[#]*\s*([^\n]*\.(?:py|js|vue|yaml|yml|json|md|sql|sh))\s*\n```(\w+)\n(.*?)```'  # 文件扩展名
        ]
        
        # 路径引用模式
        self.path_reference_patterns = [
            r'(?:backend|frontend|k8s|scripts|docs)/[^\s\)]+\.(?:py|js|vue|yaml|yml|json|md|sql|sh)',
            r'[^\s\)]+/[^\s\)]+\.(?:py|js|vue|yaml|yml|json|md|sql|sh)'
        ]

    def parse_documentation(self) -> Dict:
        """解析文档，提取所有代码引用和代码块"""
        result = {
            'documented_files': {},  # 文件路径 -> 文档信息
            'code_blocks': [],       # 代码块列表
            'file_references': set(), # 文件路径引用
            'missing_files': set(),   # 文档中引用但不存在的文件
            'doc_summary': {}         # 每个文档的摘要
        }
        
        for doc_file in self.doc_files:
            doc_path = os.path.join(self.repo_root, doc_file)
            if not os.path.exists(doc_path):
                continue
                
            print(f"📖 解析文档: {doc_file}")
            
            with open(doc_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 解析代码块
            code_blocks = self._extract_code_blocks(content, doc_file)
            result['code_blocks'].extend(code_blocks)
            
            # 解析文件路径引用
            file_refs = self._extract_file_references(content)
            result['file_references'].update(file_refs)
            
            # 文档摘要
            result['doc_summary'][doc_file] = {
                'code_blocks': len(code_blocks),
                'file_references': len(file_refs),
                'size': len(content)
            }
        
        # 处理文档化的文件
        for block in result['code_blocks']:
            if block['filename']:
                result['documented_files'][block['filename']] = {
                    'source_doc': block['source_doc'],
                    'language': block['language'],
                    'has_code': bool(block['code'].strip()),
                    'code_length': len(block['code'])
                }
        
        return result

    def _extract_code_blocks(self, content: str, source_doc: str) -> List[Dict]:
        """从内容中提取代码块"""
        code_blocks = []
        
        for pattern in self.code_block_patterns:
            matches = re.findall(pattern, content, re.DOTALL)
            for match in matches:
                if len(match) == 3:
                    filename, language, code = match
                else:
                    continue
                    
                # 清理文件名
                filename = self._clean_filename(filename)
                
                if filename:
                    code_blocks.append({
                        'filename': filename,
                        'language': language.lower(),
                        'code': code.strip(),
                        'source_doc': source_doc
                    })
        
        return code_blocks

    def _extract_file_references(self, content: str) -> Set[str]:
        """从内容中提取文件路径引用"""
        file_refs = set()
        
        for pattern in self.path_reference_patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                cleaned_path = self._clean_path_reference(match)
                if cleaned_path:
                    file_refs.add(cleaned_path)
        
        return file_refs

    def _clean_filename(self, filename: str) -> str:
        """清理文件名"""
        # 移除前导的 # 符号和空格
        filename = re.sub(r'^[#\s]+', '', filename.strip())
        
        # 移除 "文件名:" 前缀
        filename = re.sub(r'^文件名[:：]\s*', '', filename)
        
        # 移除特殊字符（但保留路径分隔符）
        filename = re.sub(r'[^\w\-_./\\]', '', filename)
        
        # 标准化路径分隔符
        filename = filename.replace('\\', '/')
        
        # 移除多余的路径分隔符
        filename = re.sub(r'/+', '/', filename)
        
        return filename if filename else None

    def _clean_path_reference(self, path: str) -> str:
        """清理路径引用"""
        # 移除周围的标点符号
        path = re.sub(r'^[^\w/]+|[^\w/]+$', '', path)
        
        # 标准化路径分隔符
        path = path.replace('\\', '/')
        
        return path if path else None

    def compare_with_actual_files(self, inventory: Dict) -> Dict:
        """比较文档化的文件与实际存在的文件"""
        doc_result = self.parse_documentation()
        
        actual_files = {f['path'] for f in inventory['files']}
        documented_files = set(doc_result['documented_files'].keys())
        all_referenced_files = documented_files | doc_result['file_references']
        
        comparison = {
            'existing_but_undocumented': actual_files - all_referenced_files,
            'documented_but_missing': all_referenced_files - actual_files,
            'documented_and_existing': actual_files & documented_files,
            'only_referenced': doc_result['file_references'] - documented_files,
            'statistics': {
                'total_actual_files': len(actual_files),
                'total_documented_files': len(documented_files),
                'total_referenced_files': len(doc_result['file_references']),
                'undocumented_count': len(actual_files - all_referenced_files),
                'missing_count': len(all_referenced_files - actual_files)
            }
        }
        
        return comparison, doc_result

def main():
    """主函数"""
    repo_root = '/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank'
    
    # 加载仓库扫描结果
    inventory_file = os.path.join(repo_root, 'scripts', 'repo_inventory.json')
    if not os.path.exists(inventory_file):
        print("❌ 请先运行 repo_scanner.py 生成文件清单")
        return
    
    with open(inventory_file, 'r', encoding='utf-8') as f:
        inventory = json.load(f)
    
    # 解析文档
    parser = DocumentationParser(repo_root)
    comparison, doc_result = parser.compare_with_actual_files(inventory)
    
    print("📚 文档解析完成\n")
    
    print("📊 统计信息:")
    stats = comparison['statistics']
    print(f"  实际文件数: {stats['total_actual_files']}")
    print(f"  文档化文件数: {stats['total_documented_files']}")
    print(f"  引用文件数: {stats['total_referenced_files']}")
    print(f"  未文档化文件数: {stats['undocumented_count']}")
    print(f"  缺失文件数: {stats['missing_count']}")
    
    print(f"\n📝 文档摘要:")
    for doc, summary in doc_result['doc_summary'].items():
        print(f"  {doc}:")
        print(f"    代码块: {summary['code_blocks']} 个")
        print(f"    文件引用: {summary['file_references']} 个")
    
    print(f"\n🆕 存在但未文档化的文件 ({len(comparison['existing_but_undocumented'])}):")
    for file_path in sorted(comparison['existing_but_undocumented']):
        print(f"  - {file_path}")
    
    print(f"\n❌ 文档化但缺失的文件 ({len(comparison['documented_but_missing'])}):")
    for file_path in sorted(comparison['documented_but_missing']):
        print(f"  - {file_path}")
    
    print(f"\n✅ 文档化且存在的文件 ({len(comparison['documented_and_existing'])}):")
    for file_path in sorted(comparison['documented_and_existing']):
        print(f"  - {file_path}")
    
    # 保存分析结果
    output_file = os.path.join(repo_root, 'scripts', 'doc_analysis.json')
    analysis_result = {
        'comparison': comparison,
        'documentation_result': doc_result
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analysis_result, f, ensure_ascii=False, indent=2, default=list)
    
    print(f"\n💾 分析结果已保存到: {output_file}")
    
    return analysis_result

if __name__ == "__main__":
    main()
```


#### scripts/doc_analysis.json

scripts目录下的json文件，doc_analysis.json

```json
{
  "comparison": {
    "existing_but_undocumented": [
      "scripts/4.2.9 初始化数据库.sh",
      "scripts/auto_doc_integration.py",
      "scripts/auto_doc_completion.py",
      "scripts/4.2.2 创建命名空间.sh",
      "scripts/auto_completion_report.json",
      "scripts/5.2.2 索引优化.sql",
      "scripts/doc_parser.py",
      "scripts/doc_analysis.json",
      "scripts/4.1.4 停止服务.sh",
      "auto_review_report.md",
      "scripts/auto_review_report.md",
      ".github/workflows/auto-review.yml",
      "scripts/repo_inventory.json"
    ],
    "documented_but_missing": [
      "/App.vue",
      "frontend/src/components/HomeworkReview.vue",
      "/backup-models.sh",
      "/views/Login.vue",
      "backend/auth.py",
      "frontend/src/components/CustomTable.vue",
      "k8s/backend-deployment.yaml",
      "frontend/src/components/CustomCard.vue",
      "frontend/package.js",
      "/docs/系统UI设计方案文档.md",
      "frontend/src/components/CustomNav.vue",
      "后端/database.py",
      "docker-compose.yml",
      "k8s/ingress_2.yaml",
      "k8s/redis-deployment.yaml",
      "frontend/src/store/index.js",
      "frontend/src/App.vue",
      "k8s/edu-ai-backend-deployment.yaml",
      "k8s/backend-deployment_2.yaml",
      "backend/utils/sanitizer.py",
      "/views/TeacherDashboard.vue",
      "/components/HomeworkReview.vue",
      "/components/QuestionTable.vue",
      "github/workflows/auto-review.yml",
      "backend/controllers/ai.py",
      "frontend/src/components/ExcelImport.vue",
      "3.1题库管理流程",
      "frontend/package.json",
      "/views/Home.vue",
      "media_type=\"application/vnd.openxmlformats-officedocument.spreadsheetml.sh",
      "frontend/src/router/index.js",
      "/path/to/backup-models.sh",
      "/app/backend/main.py",
      "/docs/教育AI全栈设计方案.md",
      "k8s/frontend-deployment.yaml",
      "/path/to/backup-db.sh",
      "更新QuestionTable.vue",
      "/components/HomeworkList.vue",
      "scripts/cleanup_generated_files.py",
      "frontend/src/views/TeacherDashboard.vue",
      "/docs/教育AI题库系统文档.md",
      "frontend/src/components/QuestionTable.vue",
      "k8s/network-policy.yaml",
      "backend/models.py",
      "/views/StudentDashboard.vue",
      "frontend/src/components/CustomButton.vue",
      "k8s/tls-secret.yaml",
      "k8s/mariadb-configmap_2.yaml",
      "/backup-db.sh",
      "12.更新TeacherDashboard.vue",
      "详细表结构请参考backend/models.py",
      "/components/CustomCard.vue",
      "/CustomDialog.vue",
      "/CustomButton.vue",
      "backend/main.py",
      "/restore-db.sh",
      "项目结构总览",
      "/CustomTable.vue",
      "k8s/mariadb-configmap.yaml",
      "src=\"https://cdn.example.com/js/app.js",
      "11.更新ExcelImport.vue",
      "/rollback.sh",
      "10.更新HomeworkReview.vue",
      "/components/ExcelImport.vue",
      "k8s/rename_yaml_by_content.py",
      "backend/database.py",
      "backend/utils/cache.py",
      "/mnt/nas/backups/edu_ai_db_20231001_020000.sql",
      "k8s/backend-deployment_3.yaml",
      "k8s/edu-ai-ingress.yaml",
      "backend/controllers/question.py",
      "BACKUP_DIR/edu_ai_db_$DATE.sql",
      "k8s/ingress.yaml",
      "frontend/vite.config.js",
      "frontend/src/main.js",
      "/CustomCard.vue",
      "k8s/redis-persistent.yaml",
      "frontend/src/api/index.js",
      "修改backend/database.py",
      "backend/celery_worker.py",
      "frontend/src/components/CustomDialog.vue",
      "/views/AdminPanel.vue",
      "/components/CustomNav.vue"
    ],
    "documented_and_existing": [],
    "only_referenced": [
      "k8s/mariadb-configmap.yaml",
      "docs/教育AI全栈设计方案.md",
      "src=\"https://cdn.example.com/js/app.js",
      "/app/backend/main.py",
      "/docs/教育AI全栈设计方案.md",
      "k8s/frontend-deployment.yaml",
      "infra/k8s/tls-secret.yaml",
      "infra/k8s/mariadb-configmap_2.yaml",
      "/rollback.sh",
      "/path/to/backup-db.sh",
      "scripts/repo_scanner.py",
      "/App.vue",
      "scripts/md_code_progress_report.py",
      "k8s/backend-deployment_2.yaml",
      "/components/ExcelImport.vue",
      "/backup-models.sh",
      "k8s/rename_yaml_by_content.py",
      "backend/database.py",
      "/components/HomeworkList.vue",
      "scripts/cleanup_generated_files.py",
      "/docs/教育AI题库系统文档.md",
      "infra/k8s/backend-deployment_2.yaml",
      "scripts/sync_md_code_by_comment.py",
      "infra/k8s/redis-deployment.yaml",
      "backend/utils/cache.py",
      "backend/utils/sanitizer.py",
      "scripts/sync_md_code.py",
      "/views/TeacherDashboard.vue",
      "/components/HomeworkReview.vue",
      "/components/QuestionTable.vue",
      "k8s/network-policy.yaml",
      "/mnt/nas/backups/edu_ai_db_20231001_020000.sql",
      "github/workflows/auto-review.yml",
      "k8s/backend-deployment_3.yaml",
      "/views/Login.vue",
      "/views/StudentDashboard.vue",
      "infra/k8s/frontend-deployment.yaml",
      "BACKUP_DIR/edu_ai_db_$DATE.sql",
      "k8s/backend-deployment.yaml",
      "k8s/tls-secret.yaml",
      "k8s/ingress.yaml",
      "frontend/package.js",
      "k8s/mariadb-configmap_2.yaml",
      "/backup-db.sh",
      "scripts/auto_review_md_vs_code.py",
      "/docs/系统UI设计方案文档.md",
      "infra/k8s/backend-deployment_3.yaml",
      "infra/k8s/rename_yaml_by_content.py",
      "详细表结构请参考backend/models.py",
      "/components/CustomCard.vue",
      "/CustomCard.vue",
      "/CustomDialog.vue",
      "后端/database.py",
      "/CustomButton.vue",
      "k8s/redis-persistent.yaml",
      "修改backend/database.py",
      "scripts/sync_md_code_autoext.py",
      "scripts/split_md_code_advanced.py",
      "/restore-db.sh",
      "/views/Home.vue",
      "media_type=\"application/vnd.openxmlformats-officedocument.spreadsheetml.sh",
      "docs/教育AI题库系统文档.md",
      "infra/k8s/ingress.yaml",
      "/views/AdminPanel.vue",
      "infra/k8s/ingress_2.yaml",
      "scripts/split_md_code_autosave.py",
      "infra/k8s/redis-persistent.yaml",
      "docs/系统UI设计方案文档.md",
      "/components/CustomNav.vue",
      "/CustomTable.vue",
      "/path/to/backup-models.sh",
      "k8s/ingress_2.yaml",
      "infra/k8s/backend-deployment.yaml",
      "infra/k8s/mariadb-configmap.yaml",
      "infra/k8s/network-policy.yaml",
      "k8s/redis-deployment.yaml"
    ],
    "statistics": {
      "total_actual_files": 37,
      "total_documented_files": 31,
      "total_referenced_files": 99,
      "undocumented_count": 13,
      "missing_count": 83
    }
  },
  "documentation_result": {
    "documented_files": {
      "3.1题库管理流程": {
        "source_doc": "docs/教育AI全栈设计方案.md",
        "language": "mermaid",
        "has_code": true,
        "code_length": 255
      },
      "backend/main.py": {
        "source_doc": "docs/教育AI全栈设计方案.md",
        "language": "python",
        "has_code": true,
        "code_length": 842
      },
      "backend/models.py": {
        "source_doc": "docs/教育AI全栈设计方案.md",
        "language": "python",
        "has_code": true,
        "code_length": 2663
      },
      "backend/controllers/question.py": {
        "source_doc": "docs/教育AI全栈设计方案.md",
        "language": "python",
        "has_code": true,
        "code_length": 2693
      },
      "backend/controllers/ai.py": {
        "source_doc": "docs/教育AI全栈设计方案.md",
        "language": "python",
        "has_code": true,
        "code_length": 1210
      },
      "backend/celery_worker.py": {
        "source_doc": "docs/教育AI全栈设计方案.md",
        "language": "python",
        "has_code": true,
        "code_length": 852
      },
      "backend/auth.py": {
        "source_doc": "docs/教育AI全栈设计方案.md",
        "language": "python",
        "has_code": true,
        "code_length": 1378
      },
      "frontend/src/main.js": {
        "source_doc": "docs/系统UI设计方案文档.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 530
      },
      "frontend/src/router/index.js": {
        "source_doc": "docs/系统UI设计方案文档.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 1699
      },
      "frontend/src/views/TeacherDashboard.vue": {
        "source_doc": "docs/教育AI全栈设计方案.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 938
      },
      "frontend/src/components/QuestionTable.vue": {
        "source_doc": "docs/教育AI全栈设计方案.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 1871
      },
      "frontend/src/components/ExcelImport.vue": {
        "source_doc": "docs/教育AI全栈设计方案.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 1747
      },
      "frontend/src/components/HomeworkReview.vue": {
        "source_doc": "docs/教育AI全栈设计方案.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 1898
      },
      "frontend/src/api/index.js": {
        "source_doc": "docs/教育AI全栈设计方案.md",
        "language": "javascript",
        "has_code": true,
        "code_length": 772
      },
      "docker-compose.yml": {
        "source_doc": "docs/教育AI全栈设计方案.md",
        "language": "yaml",
        "has_code": true,
        "code_length": 1194
      },
      "k8s/edu-ai-ingress.yaml": {
        "source_doc": "docs/教育AI全栈设计方案.md",
        "language": "yaml",
        "has_code": true,
        "code_length": 732
      },
      "k8s/edu-ai-backend-deployment.yaml": {
        "source_doc": "docs/教育AI全栈设计方案.md",
        "language": "yaml",
        "has_code": true,
        "code_length": 738
      },
      "项目结构总览": {
        "source_doc": "docs/教育AI全栈设计方案.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 1658
      },
      "frontend/src/App.vue": {
        "source_doc": "docs/系统UI设计方案文档.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 515
      },
      "frontend/src/components/CustomNav.vue": {
        "source_doc": "docs/系统UI设计方案文档.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 2923
      },
      "frontend/src/components/CustomDialog.vue": {
        "source_doc": "docs/系统UI设计方案文档.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 1421
      },
      "frontend/src/components/CustomTable.vue": {
        "source_doc": "docs/系统UI设计方案文档.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 5982
      },
      "frontend/src/components/CustomButton.vue": {
        "source_doc": "docs/系统UI设计方案文档.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 2830
      },
      "frontend/src/components/CustomCard.vue": {
        "source_doc": "docs/系统UI设计方案文档.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 1518
      },
      "更新QuestionTable.vue": {
        "source_doc": "docs/系统UI设计方案文档.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 3733
      },
      "10.更新HomeworkReview.vue": {
        "source_doc": "docs/系统UI设计方案文档.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 2420
      },
      "11.更新ExcelImport.vue": {
        "source_doc": "docs/系统UI设计方案文档.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 3570
      },
      "12.更新TeacherDashboard.vue": {
        "source_doc": "docs/系统UI设计方案文档.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 1479
      },
      "frontend/src/store/index.js": {
        "source_doc": "docs/系统UI设计方案文档.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 1450
      },
      "frontend/vite.config.js": {
        "source_doc": "docs/系统UI设计方案文档.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 748
      },
      "frontend/package.json": {
        "source_doc": "docs/系统UI设计方案文档.md",
        "language": "plaintext",
        "has_code": true,
        "code_length": 731
      }
    },
    "code_blocks": [
      {
        "filename": "3.1题库管理流程",
        "language": "mermaid",
        "code": "graph TD\n    A[教师登录] --> B[进入题库管理]\n    B --> C{操作选择}\n    C -->|创建题目| D[填写题目信息]\n    C -->|编辑题目| E[修改题目信息]\n    C -->|删除题目| F[确认删除]\n    C -->|导入Excel| G[上传Excel文件]\n    D --> H[保存题目]\n    E --> H\n    G --> I[解析Excel数据]\n    I --> H\n    H --> J[更新题库]\n    F --> J",
        "source_doc": "docs/教育AI题库系统文档.md"
      },
      {
        "filename": "3.1题库管理流程",
        "language": "mermaid",
        "code": "graph TD\n    A[教师登录] --> B[进入题库管理]\n    B --> C{操作选择}\n    C -->|创建题目| D[填写题目信息]\n    C -->|编辑题目| E[修改题目信息]\n    C -->|删除题目| F[确认删除]\n    C -->|导入Excel| G[上传Excel文件]\n    D --> H[保存题目]\n    E --> H\n    G --> I[解析Excel数据]\n    I --> H\n    H --> J[更新题库]\n    F --> J",
        "source_doc": "docs/教育AI题库系统文档.md"
      },
      {
        "filename": "backend/main.py",
        "language": "python",
        "code": "from fastapi import FastAPI\nfrom fastapi.middleware.cors import CORSMiddleware\nfrom backend.controllers import ai, homework, question\nfrom backend.database import engine\nfrom backend.models import Base\n\n# 创建数据库表\nBase.metadata.create_all(bind=engine)\n\napp = FastAPI(title=\"教育AI题库系统\", version=\"1.0.0\")\n\n# 配置CORS\napp.add_middleware(\n    CORSMiddleware,\n    allow_origins=[\"*\"],\n    allow_credentials=True,\n    allow_methods=[\"*\"],\n    allow_headers=[\"*\"],\n)\n\n# 注册路由\napp.include_router(question.router, prefix=\"/api/questions\", tags=[\"题库管理\"])\napp.include_router(homework.router, prefix=\"/api/homework\", tags=[\"作业管理\"])\napp.include_router(ai.router, prefix=\"/api/ai\", tags=[\"AI服务\"])\n\n@app.get(\"/\")\ndef read_root():\n    return {\"message\": \"教育AI题库系统 API\"}\n\nif __name__ == \"__main__\":\n    import uvicorn\n    uvicorn.run(app, host=\"0.0.0.0\", port=8000)",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/models.py",
        "language": "python",
        "code": "from sqlalchemy import Column, Integer, String, Text, Enum, DateTime, ForeignKey, DECIMAL\nfrom sqlalchemy.orm import declarative_base, relationship\nimport enum\n\nBase = declarative_base()\n\nclass Difficulty(enum.Enum):\n    easy = '易'\n    medium = '中'\n    hard = '难'\n    olympiad = '奥数'\n\nclass User(Base):\n    __tablename__ = 'users'\n    id = Column(Integer, primary_key=True)\n    username = Column(String(100), unique=True)\n    password_hash = Column(String(255))\n    name = Column(String(100))\n    role = Column(Enum('student','teacher','admin','parent'))\n    register_time = Column(DateTime)\n\nclass Subject(Base):\n    __tablename__ = 'subjects'\n    id = Column(Integer, primary_key=True)\n    name = Column(String(50))\n    description = Column(String(255))\n\nclass Question(Base):\n    __tablename__ = 'questions'\n    id = Column(Integer, primary_key=True)\n    subject_id = Column(Integer, ForeignKey('subjects.id'))\n    type_id = Column(Integer)\n    content = Column(Text)\n    option_a = Column(String(255))\n    option_b = Column(String(255))\n    option_c = Column(String(255))\n    option_d = Column(String(255))\n    answer = Column(String(255))\n    explanation = Column(Text)\n    knowledge_point = Column(String(255))\n    difficulty = Column(Enum(Difficulty))\n    tags = Column(String(255))\n    image_url = Column(String(255))\n    extra_json = Column(Text)\n    created_by = Column(Integer, ForeignKey('users.id'))\n    created_at = Column(DateTime)\n    updated_at = Column(DateTime)\n    subject = relationship(\"Subject\")\n    creator = relationship(\"User\")\n\nclass StudentAnswer(Base):\n    __tablename__ = 'student_answers'\n    id = Column(Integer, primary_key=True)\n    question_id = Column(Integer, ForeignKey('questions.id'))\n    student_id = Column(Integer, ForeignKey('users.id'))\n    answer = Column(Text)\n    score = Column(DECIMAL(5,2))\n    ai_explanation = Column(Text)\n    answer_image_url = Column(String(255))\n    submit_time = Column(DateTime)\n\nclass Homework(Base):\n    __tablename__ = 'homework'\n    id = Column(Integer, primary_key=True)\n    teacher_id = Column(Integer, ForeignKey('users.id'))\n    title = Column(String(255))\n    publish_time = Column(DateTime)\n\nclass HomeworkAssignment(Base):\n    __tablename__ = 'homework_assignments'\n    id = Column(Integer, primary_key=True)\n    homework_id = Column(Integer, ForeignKey('homework.id'))\n    student_id = Column(Integer, ForeignKey('users.id'))\n    question_id = Column(Integer, ForeignKey('questions.id'))\n    answer = Column(Text)\n    score = Column(DECIMAL(5,2))\n    comment = Column(Text)\n    ai_explanation = Column(Text)\n    submit_time = Column(DateTime)\n    review_time = Column(DateTime)",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/controllers/question.py",
        "language": "python",
        "code": "from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Response\nfrom sqlalchemy.orm import Session\nfrom backend.models import Question, User\nfrom backend.database import get_db\nfrom backend.auth import get_current_user\nimport pandas as pd\nimport datetime\nimport os\n\nrouter = APIRouter()\n\n@router.get(\"/\")\ndef get_questions(subject_id: int = None, db: Session = Depends(get_db)):\n    query = db.query(Question)\n    if subject_id:\n        query = query.filter(Question.subject_id == subject_id)\n    return {\"items\": [q.to_dict() for q in query.limit(100)]}\n\n@router.post(\"/\", dependencies=[Depends(get_current_user)])\ndef create_question(q: dict, db: Session = Depends(get_db), user: User = Depends(get_current_user)):\n    nq = Question(**q, created_by=user.id, created_at=datetime.datetime.now())\n    db.add(nq)\n    db.commit()\n    return {\"msg\": \"题目已创建\", \"id\": nq.id}\n\n@router.post(\"/import-excel\", dependencies=[Depends(get_current_user)])\nasync def import_excel(file: UploadFile = File(...), db: Session = Depends(get_db), user: User = Depends(get_current_user)):\n    df = pd.read_excel(file.file)\n    for _, row in df.iterrows():\n        nq = Question(\n            content=row['题干'],\n            subject_id=row['学科ID'],\n            difficulty=row['难度'],\n            tags=row.get('标签',''),\n            option_a=row.get('option_a',''),\n            option_b=row.get('option_b',''),\n            option_c=row.get('option_c',''),\n            option_d=row.get('option_d',''),\n            answer=row.get('answer',''),\n            explanation=row.get('解析',''),\n            image_url=row.get('image_url',''),\n            extra_json=row.get('extra_json',None),\n            created_by=user.id,\n            created_at=datetime.datetime.now()\n        )\n        db.add(nq)\n    db.commit()\n    return {\"msg\": \"Excel导入成功\"}\n\n@router.get(\"/excel-template\")\ndef download_excel_template():\n    template_path = \"static/question_import_template.xlsx\"\n    if not os.path.exists(template_path):\n        # 创建模板文件\n        import pandas as pd\n        df = pd.DataFrame([{\n            \"题干\": \"勾股定理是什么\",\n            \"学科ID\": 1,\n            \"难度\": \"奥数\",\n            \"标签\": \"数学\",\n            \"option_a\": \"\",\n            \"option_b\": \"\",\n            \"option_c\": \"\",\n            \"option_d\": \"\",\n            \"answer\": \"\",\n            \"解析\": \"a^2+b^2=c^2\",\n            \"image_url\": \"http://xxx\",\n            \"extra_json\": '{\"latex\":\"a^2+b^2=c^2\"}'\n        }])\n        os.makedirs(\"static\", exist_ok=True)\n        df.to_excel(template_path, index=False)\n    return Response(content=open(template_path, \"rb\").read(), \n                   media_type=\"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet\")",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/controllers/ai.py",
        "language": "python",
        "code": "from fastapi import APIRouter, Depends, BackgroundTasks\nfrom backend.auth import get_current_user\nfrom backend.celery_worker import grade_answer\nfrom sqlalchemy.orm import Session\nfrom backend.database import get_db\nfrom backend.models import StudentAnswer, User\nimport datetime\n\nrouter = APIRouter()\n\n@router.post(\"/grade\")\ndef ai_grade(payload: dict, db: Session = Depends(get_db), user: User = Depends(get_current_user)):\n    task = grade_answer.apply_async(args=(payload.get('model', 'gemma-3-270m'), payload['question'], payload['answer']))\n    # 保存答题记录，状态pending\n    sa = StudentAnswer(\n        question_id=payload.get('question_id'),\n        student_id=user.id,\n        answer=payload['answer'],\n        score=None,\n        ai_explanation='',\n        answer_image_url=payload.get('answer_image_url',''),\n        submit_time=datetime.datetime.now()\n    )\n    db.add(sa)\n    db.commit()\n    return {\"task_id\": task.id}\n\n@router.get(\"/grade-result/{task_id}\")\ndef get_grade_result(task_id: str):\n    from backend.celery_worker import grade_answer\n    task = grade_answer.AsyncResult(task_id)\n    if not task.ready():\n        return {\"status\": \"pending\"}\n    return {\"status\": \"done\", \"result\": task.result}",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/celery_worker.py",
        "language": "python",
        "code": "from celery import Celery\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\ncelery_app = Celery('ai_tasks', broker='redis://redis:6379/0')\n\nMODEL_CACHE = {}\n\ndef load_model(model_name):\n    if model_name not in MODEL_CACHE:\n        path = f\"/mnt/nas/models/{model_name}\"\n        tokenizer = AutoTokenizer.from_pretrained(path)\n        model = AutoModelForCausalLM.from_pretrained(path)\n        MODEL_CACHE[model_name] = (tokenizer, model)\n    return MODEL_CACHE[model_name]\n\n@celery_app.task\ndef grade_answer(model_name, question, answer):\n    tokenizer, model = load_model(model_name)\n    prompt = f\"题目：{question}\\n学生答案：{answer}\\n请判断正误并给出解析：\"\n    inputs = tokenizer(prompt, return_tensors=\"pt\")\n    outputs = model.generate(**inputs, max_new_tokens=128)\n    result = tokenizer.decode(outputs[0], skip_special_tokens=True)\n    return result",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/auth.py",
        "language": "python",
        "code": "from fastapi import Depends, HTTPException, status\nfrom fastapi.security import OAuth2PasswordBearer\nfrom jose import JWTError, jwt\nfrom sqlalchemy.orm import Session\nfrom backend.database import get_db\nfrom backend.models import User\nimport datetime\n\nSECRET_KEY = \"your-secret-key\"\nALGORITHM = \"HS256\"\nACCESS_TOKEN_EXPIRE_MINUTES = 30\n\noauth2_scheme = OAuth2PasswordBearer(tokenUrl=\"token\")\n\ndef create_access_token(data: dict):\n    to_encode = data.copy()\n    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)\n    to_encode.update({\"exp\": expire})\n    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)\n    return encoded_jwt\n\nasync def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):\n    credentials_exception = HTTPException(\n        status_code=status.HTTP_401_UNAUTHORIZED,\n        detail=\"Could not validate credentials\",\n        headers={\"WWW-Authenticate\": \"Bearer\"},\n    )\n    try:\n        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])\n        username: str = payload.get(\"sub\")\n        if username is None:\n            raise credentials_exception\n    except JWTError:\n        raise credentials_exception\n    \n    user = db.query(User).filter(User.username == username).first()\n    if user is None:\n        raise credentials_exception\n    return user",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/main.js",
        "language": "javascript",
        "code": "import { createApp } from 'vue'\nimport ElementPlus from 'element-plus'\nimport 'element-plus/dist/index.css'\nimport { createPinia } from 'pinia'\nimport App from './App.vue'\nimport router from './router'\n\nconst app = createApp(App)\napp.use(ElementPlus)\napp.use(createPinia())\napp.use(router)\napp.mount('#app')",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/router/index.js",
        "language": "javascript",
        "code": "import { createRouter, createWebHistory } from 'vue-router'\nimport Home from '../views/Home.vue'\nimport Login from '../views/Login.vue'\nimport StudentDashboard from '../views/StudentDashboard.vue'\nimport TeacherDashboard from '../views/TeacherDashboard.vue'\nimport AdminPanel from '../views/AdminPanel.vue'\n\nconst routes = [\n  { path: '/', component: Home },\n  { path: '/login', component: Login },\n  { \n    path: '/student', \n    component: StudentDashboard, \n    meta: { requiresAuth: true, role: 'student' } \n  },\n  { \n    path: '/teacher', \n    component: TeacherDashboard, \n    meta: { requiresAuth: true, role: 'teacher' } \n  },\n  { \n    path: '/admin', \n    component: AdminPanel, \n    meta: { requiresAuth: true, role: 'admin' } \n  }\n]\n\nconst router = createRouter({\n  history: createWebHistory(),\n  routes\n})\n\n// 路由守卫\nrouter.beforeEach((to, from, next) => {\n  const token = localStorage.getItem('token')\n  const role = localStorage.getItem('role')\n  \n  if (to.meta.requiresAuth) {\n    if (!token) {\n      next('/login')\n    } else if (to.meta.role && to.meta.role !== role) {\n      next('/login')\n    } else {\n      next()\n    }\n  } else {\n    next()\n  }\n})\n\nexport default router",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/views/TeacherDashboard.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"teacher-dashboard\">\n    <h1>教师控制台</h1>\n    <el-tabs v-model=\"activeTab\">\n      <el-tab-pane label=\"题库管理\" name=\"questions\">\n        <QuestionTable @importExcel=\"showImport = true\" />\n        <ExcelImport v-if=\"showImport\" @close=\"showImport = false\" />\n      </el-tab-pane>\n      <el-tab-pane label=\"作业管理\" name=\"homework\">\n        <HomeworkList />\n      </el-tab-pane>\n      <el-tab-pane label=\"作业批改\" name=\"review\">\n        <HomeworkReview />\n      </el-tab-pane>\n    </el-tabs>\n  </div>\n</template>\n\n<script setup>\nimport { ref } from 'vue'\nimport QuestionTable from '@/components/QuestionTable.vue'\nimport ExcelImport from '@/components/ExcelImport.vue'\nimport HomeworkList from '@/components/HomeworkList.vue'\nimport HomeworkReview from '@/components/HomeworkReview.vue'\n\nconst activeTab = ref('questions')\nconst showImport = ref(false)\n</script>\n\n<style scoped>\n.teacher-dashboard {\n  padding: 20px;\n}\n</style>",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/components/QuestionTable.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"question-table\">\n    <div class=\"actions\">\n      <el-button type=\"primary\" @click=\"$emit('importExcel')\">Excel导入</el-button>\n    </div>\n    \n    <el-table :data=\"questions\" style=\"width: 100%\">\n      <el-table-column prop=\"content\" label=\"题干\" />\n      <el-table-column prop=\"difficulty\" label=\"难度\" />\n      <el-table-column prop=\"tags\" label=\"标签\" />\n      <el-table-column label=\"操作\">\n        <template #default=\"scope\">\n          <el-button @click=\"viewQuestion(scope.row)\">查看</el-button>\n        </template>\n      </el-table-column>\n    </el-table>\n    \n    <el-dialog v-model=\"dialogVisible\" title=\"题目详情\" width=\"50%\">\n      <div v-if=\"selectedQuestion\">\n        <p><strong>题干:</strong> {{ selectedQuestion.content }}</p>\n        <p v-if=\"selectedQuestion.image_url\">\n          <img :src=\"selectedQuestion.image_url\" style=\"max-width: 300px;\" />\n        </p>\n        <p><strong>难度:</strong> {{ selectedQuestion.difficulty }}</p>\n        <p><strong>标签:</strong> {{ selectedQuestion.tags }}</p>\n        <p><strong>解析:</strong> {{ selectedQuestion.explanation }}</p>\n      </div>\n      <template #footer>\n        <el-button @click=\"dialogVisible = false\">关闭</el-button>\n      </template>\n    </el-dialog>\n  </div>\n</template>\n\n<script setup>\nimport { ref, onMounted } from 'vue'\nimport axios from '@/api'\n\nconst questions = ref([])\nconst dialogVisible = ref(false)\nconst selectedQuestion = ref(null)\n\nconst emit = defineEmits(['importExcel'])\n\nonMounted(async () => {\n  try {\n    const response = await axios.get('/questions')\n    questions.value = response.data.items\n  } catch (error) {\n    console.error('获取题库失败:', error)\n  }\n})\n\nconst viewQuestion = (question) => {\n  selectedQuestion.value = question\n  dialogVisible.value = true\n}\n</script>\n\n<style scoped>\n.question-table {\n  margin-top: 20px;\n}\n.actions {\n  margin-bottom: 20px;\n}\n</style>",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/components/ExcelImport.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"excel-import\">\n    <el-card>\n      <h2>题库Excel导入</h2>\n      <div class=\"template-download\">\n        <el-link :href=\"templateUrl\" target=\"_blank\">下载Excel模板</el-link>\n      </div>\n      \n      <el-upload\n        class=\"upload-demo\"\n        :action=\"uploadUrl\"\n        :headers=\"{ Authorization: 'Bearer ' + token }\"\n        :on-success=\"handleSuccess\"\n        :on-error=\"handleError\"\n        :file-list=\"fileList\"\n        accept=\".xlsx, .xls\"\n      >\n        <el-button type=\"primary\">点击上传</el-button>\n        <template #tip>\n          <div class=\"el-upload__tip\">\n            只能上传xlsx/xls文件，且不超过10MB\n          </div>\n        </template>\n      </el-upload>\n      \n      <el-alert\n        v-if=\"message\"\n        :title=\"message\"\n        :type=\"messageType\"\n        show-icon\n        style=\"margin-top: 20px;\"\n      />\n      \n      <div class=\"actions\">\n        <el-button @click=\"$emit('close')\">关闭</el-button>\n      </div>\n    </el-card>\n  </div>\n</template>\n\n<script setup>\nimport { ref } from 'vue'\nimport axios from '@/api'\n\nconst emit = defineEmits(['close'])\n\nconst token = localStorage.getItem('token')\nconst templateUrl = '/api/questions/excel-template'\nconst uploadUrl = '/api/questions/import-excel'\nconst fileList = ref([])\nconst message = ref('')\nconst messageType = ref('success')\n\nconst handleSuccess = (response) => {\n  message.value = response.msg || '导入成功'\n  messageType.value = 'success'\n  fileList.value = []\n}\n\nconst handleError = (error) => {\n  message.value = '导入失败'\n  messageType.value = 'error'\n  console.error('导入错误:', error)\n}\n</script>\n\n<style scoped>\n.excel-import {\n  margin-top: 20px;\n}\n.template-download {\n  margin-bottom: 20px;\n}\n.actions {\n  margin-top: 20px;\n  text-align: right;\n}\n</style>",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/components/HomeworkReview.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"homework-review\">\n    <h2>作业批改</h2>\n    \n    <el-table :data=\"assignments\" style=\"width: 100%\">\n      <el-table-column prop=\"studentName\" label=\"学生\" />\n      <el-table-column prop=\"question\" label=\"题目\" />\n      <el-table-column prop=\"answer\" label=\"学生答案\" />\n      <el-table-column prop=\"ai_explanation\" label=\"AI解析\" />\n      <el-table-column label=\"评分\">\n        <template #default=\"scope\">\n          <el-input-number \n            v-model=\"scope.row.score\" \n            :min=\"0\" \n            :max=\"100\" \n            :precision=\"1\"\n          />\n        </template>\n      </el-table-column>\n      <el-table-column label=\"批语\">\n        <template #default=\"scope\">\n          <el-input v-model=\"scope.row.comment\" />\n        </template>\n      </el-table-column>\n      <el-table-column label=\"操作\">\n        <template #default=\"scope\">\n          <el-button \n            type=\"primary\" \n            @click=\"submitReview(scope.row)\"\n            :disabled=\"scope.row.submitted\"\n          >\n            {{ scope.row.submitted ? '已提交' : '提交' }}\n          </el-button>\n        </template>\n      </el-table-column>\n    </el-table>\n  </div>\n</template>\n\n<script setup>\nimport { ref, onMounted } from 'vue'\nimport axios from '@/api'\n\nconst assignments = ref([])\n\nonMounted(async () => {\n  try {\n    const response = await axios.get('/homework/review-list')\n    assignments.value = response.data.items\n  } catch (error) {\n    console.error('获取作业列表失败:', error)\n  }\n})\n\nconst submitReview = async (assignment) => {\n  try {\n    await axios.post('/homework/review', {\n      id: assignment.id,\n      score: assignment.score,\n      comment: assignment.comment\n    })\n    \n    assignment.submitted = true\n    ElMessage.success('批改成功')\n  } catch (error) {\n    console.error('提交批改失败:', error)\n    ElMessage.error('提交失败')\n  }\n}\n</script>\n\n<style scoped>\n.homework-review {\n  margin-top: 20px;\n}\n</style>",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/api/index.js",
        "language": "javascript",
        "code": "import axios from 'axios'\nimport { ElMessage } from 'element-plus'\n\nconst api = axios.create({\n  baseURL: '/api', // 配置代理\n  timeout: 10000\n})\n\n// 请求拦截器\napi.interceptors.request.use(\n  config => {\n    const token = localStorage.getItem('token')\n    if (token) {\n      config.headers.Authorization = `Bearer ${token}`\n    }\n    return config\n  },\n  error => {\n    return Promise.reject(error)\n  }\n)\n\n// 响应拦截器\napi.interceptors.response.use(\n  response => {\n    return response.data\n  },\n  error => {\n    if (error.response && error.response.status === 401) {\n      localStorage.removeItem('token')\n      localStorage.removeItem('role')\n      window.location.href = '/login'\n      ElMessage.error('登录已过期，请重新登录')\n    }\n    return Promise.reject(error)\n  }\n)\n\nexport default api",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "docker-compose.yml",
        "language": "yaml",
        "code": "version: '3.8'\n\nservices:\n  backend:\n    build: ./backend\n    container_name: edu-ai-backend\n    ports:\n      - \"8000:8000\"\n    environment:\n      - DATABASE_URL=mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db\n      - CELERY_BROKER_URL=redis://redis:6379/0\n    volumes:\n      - /mnt/nas/models:/mnt/nas/models\n    depends_on:\n      - mariadb\n      - redis\n\n  frontend:\n    build: ./frontend\n    container_name: edu-ai-frontend\n    ports:\n      - \"5173:80\"\n    depends_on:\n      - backend\n\n  mariadb:\n    image: mariadb:10.6\n    container_name: edu-ai-mariadb\n    environment:\n      MYSQL_ROOT_PASSWORD: yourpassword\n      MYSQL_DATABASE: edu_ai_db\n    volumes:\n      - /mnt/nas/db:/var/lib/mysql\n    ports:\n      - \"3306:3306\"\n\n  redis:\n    image: redis:6-alpine\n    container_name: edu-ai-redis\n    ports:\n      - \"6379:6379\"\n\n  celery:\n    build: \n      context: ./backend\n      dockerfile: Dockerfile.celery\n    container_name: edu-ai-celery\n    environment:\n      - DATABASE_URL=mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db\n      - CELERY_BROKER_URL=redis://redis:6379/0\n    volumes:\n      - /mnt/nas/models:/mnt/nas/models\n    depends_on:\n      - mariadb\n      - redis",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "k8s/edu-ai-ingress.yaml",
        "language": "yaml",
        "code": "apiVersion: networking.k8s.io/v1\nkind: Ingress\nmetadata:\n  name: edu-ai-ingress\n  annotations:\n    nginx.ingress.kubernetes.io/rewrite-target: /$2\n    nginx.ingress.kubernetes.io/ssl-redirect: \"true\"\n    cert-manager.io/cluster-issuer: \"letsencrypt-prod\"\nspec:\n  tls:\n  - hosts:\n    - ai.yourdomain.com\n    secretName: edu-ai-tls\n  rules:\n  - host: ai.yourdomain.com\n    http:\n      paths:\n      - path: /api(/|$)(.*)\n        pathType: Prefix\n        backend:\n          service:\n            name: edu-ai-backend-service\n            port:\n              number: 8000\n      - path: /()(.*)\n        pathType: Prefix\n        backend:\n          service:\n            name: edu-ai-frontend-service\n            port:\n              number: 80",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "k8s/edu-ai-backend-deployment.yaml",
        "language": "yaml",
        "code": "apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: edu-ai-backend\nspec:\n  replicas: 2\n  selector:\n    matchLabels:\n      app: edu-ai-backend\n  template:\n    metadata:\n      labels:\n        app: edu-ai-backend\n    spec:\n      containers:\n      - name: backend\n        image: yourrepo/edu-ai-backend:latest\n        ports:\n        - containerPort: 8000\n        env:\n        - name: DATABASE_URL\n          value: \"mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db\"\n        - name: CELERY_BROKER_URL\n          value: \"redis://redis:6379/0\"\n        volumeMounts:\n        - name: nas-models\n          mountPath: /mnt/nas/models\n      volumes:\n      - name: nas-models\n        persistentVolumeClaim:\n          claimName: nas-models-pvc",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/main.py",
        "language": "python",
        "code": "from fastapi import FastAPI\nfrom fastapi.middleware.cors import CORSMiddleware\nfrom backend.controllers import ai, homework, question\nfrom backend.database import engine\nfrom backend.models import Base\n\n# 创建数据库表\nBase.metadata.create_all(bind=engine)\n\napp = FastAPI(title=\"教育AI题库系统\", version=\"1.0.0\")\n\n# 配置CORS\napp.add_middleware(\n    CORSMiddleware,\n    allow_origins=[\"*\"],\n    allow_credentials=True,\n    allow_methods=[\"*\"],\n    allow_headers=[\"*\"],\n)\n\n# 注册路由\napp.include_router(question.router, prefix=\"/api/questions\", tags=[\"题库管理\"])\napp.include_router(homework.router, prefix=\"/api/homework\", tags=[\"作业管理\"])\napp.include_router(ai.router, prefix=\"/api/ai\", tags=[\"AI服务\"])\n\n@app.get(\"/\")\ndef read_root():\n    return {\"message\": \"教育AI题库系统 API\"}\n\nif __name__ == \"__main__\":\n    import uvicorn\n    uvicorn.run(app, host=\"0.0.0.0\", port=8000)",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/models.py",
        "language": "python",
        "code": "from sqlalchemy import Column, Integer, String, Text, Enum, DateTime, ForeignKey, DECIMAL\nfrom sqlalchemy.orm import declarative_base, relationship\nimport enum\n\nBase = declarative_base()\n\nclass Difficulty(enum.Enum):\n    easy = '易'\n    medium = '中'\n    hard = '难'\n    olympiad = '奥数'\n\nclass User(Base):\n    __tablename__ = 'users'\n    id = Column(Integer, primary_key=True)\n    username = Column(String(100), unique=True)\n    password_hash = Column(String(255))\n    name = Column(String(100))\n    role = Column(Enum('student','teacher','admin','parent'))\n    register_time = Column(DateTime)\n\nclass Subject(Base):\n    __tablename__ = 'subjects'\n    id = Column(Integer, primary_key=True)\n    name = Column(String(50))\n    description = Column(String(255))\n\nclass Question(Base):\n    __tablename__ = 'questions'\n    id = Column(Integer, primary_key=True)\n    subject_id = Column(Integer, ForeignKey('subjects.id'))\n    type_id = Column(Integer)\n    content = Column(Text)\n    option_a = Column(String(255))\n    option_b = Column(String(255))\n    option_c = Column(String(255))\n    option_d = Column(String(255))\n    answer = Column(String(255))\n    explanation = Column(Text)\n    knowledge_point = Column(String(255))\n    difficulty = Column(Enum(Difficulty))\n    tags = Column(String(255))\n    image_url = Column(String(255))\n    extra_json = Column(Text)\n    created_by = Column(Integer, ForeignKey('users.id'))\n    created_at = Column(DateTime)\n    updated_at = Column(DateTime)\n    subject = relationship(\"Subject\")\n    creator = relationship(\"User\")\n\nclass StudentAnswer(Base):\n    __tablename__ = 'student_answers'\n    id = Column(Integer, primary_key=True)\n    question_id = Column(Integer, ForeignKey('questions.id'))\n    student_id = Column(Integer, ForeignKey('users.id'))\n    answer = Column(Text)\n    score = Column(DECIMAL(5,2))\n    ai_explanation = Column(Text)\n    answer_image_url = Column(String(255))\n    submit_time = Column(DateTime)\n\nclass Homework(Base):\n    __tablename__ = 'homework'\n    id = Column(Integer, primary_key=True)\n    teacher_id = Column(Integer, ForeignKey('users.id'))\n    title = Column(String(255))\n    publish_time = Column(DateTime)\n\nclass HomeworkAssignment(Base):\n    __tablename__ = 'homework_assignments'\n    id = Column(Integer, primary_key=True)\n    homework_id = Column(Integer, ForeignKey('homework.id'))\n    student_id = Column(Integer, ForeignKey('users.id'))\n    question_id = Column(Integer, ForeignKey('questions.id'))\n    answer = Column(Text)\n    score = Column(DECIMAL(5,2))\n    comment = Column(Text)\n    ai_explanation = Column(Text)\n    submit_time = Column(DateTime)\n    review_time = Column(DateTime)",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/controllers/question.py",
        "language": "python",
        "code": "from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Response\nfrom sqlalchemy.orm import Session\nfrom backend.models import Question, User\nfrom backend.database import get_db\nfrom backend.auth import get_current_user\nimport pandas as pd\nimport datetime\nimport os\n\nrouter = APIRouter()\n\n@router.get(\"/\")\ndef get_questions(subject_id: int = None, db: Session = Depends(get_db)):\n    query = db.query(Question)\n    if subject_id:\n        query = query.filter(Question.subject_id == subject_id)\n    return {\"items\": [q.to_dict() for q in query.limit(100)]}\n\n@router.post(\"/\", dependencies=[Depends(get_current_user)])\ndef create_question(q: dict, db: Session = Depends(get_db), user: User = Depends(get_current_user)):\n    nq = Question(**q, created_by=user.id, created_at=datetime.datetime.now())\n    db.add(nq)\n    db.commit()\n    return {\"msg\": \"题目已创建\", \"id\": nq.id}\n\n@router.post(\"/import-excel\", dependencies=[Depends(get_current_user)])\nasync def import_excel(file: UploadFile = File(...), db: Session = Depends(get_db), user: User = Depends(get_current_user)):\n    df = pd.read_excel(file.file)\n    for _, row in df.iterrows():\n        nq = Question(\n            content=row['题干'],\n            subject_id=row['学科ID'],\n            difficulty=row['难度'],\n            tags=row.get('标签',''),\n            option_a=row.get('option_a',''),\n            option_b=row.get('option_b',''),\n            option_c=row.get('option_c',''),\n            option_d=row.get('option_d',''),\n            answer=row.get('answer',''),\n            explanation=row.get('解析',''),\n            image_url=row.get('image_url',''),\n            extra_json=row.get('extra_json',None),\n            created_by=user.id,\n            created_at=datetime.datetime.now()\n        )\n        db.add(nq)\n    db.commit()\n    return {\"msg\": \"Excel导入成功\"}\n\n@router.get(\"/excel-template\")\ndef download_excel_template():\n    template_path = \"static/question_import_template.xlsx\"\n    if not os.path.exists(template_path):\n        # 创建模板文件\n        import pandas as pd\n        df = pd.DataFrame([{\n            \"题干\": \"勾股定理是什么\",\n            \"学科ID\": 1,\n            \"难度\": \"奥数\",\n            \"标签\": \"数学\",\n            \"option_a\": \"\",\n            \"option_b\": \"\",\n            \"option_c\": \"\",\n            \"option_d\": \"\",\n            \"answer\": \"\",\n            \"解析\": \"a^2+b^2=c^2\",\n            \"image_url\": \"http://xxx\",\n            \"extra_json\": '{\"latex\":\"a^2+b^2=c^2\"}'\n        }])\n        os.makedirs(\"static\", exist_ok=True)\n        df.to_excel(template_path, index=False)\n    return Response(content=open(template_path, \"rb\").read(), \n                   media_type=\"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet\")",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/controllers/ai.py",
        "language": "python",
        "code": "from fastapi import APIRouter, Depends, BackgroundTasks\nfrom backend.auth import get_current_user\nfrom backend.celery_worker import grade_answer\nfrom sqlalchemy.orm import Session\nfrom backend.database import get_db\nfrom backend.models import StudentAnswer, User\nimport datetime\n\nrouter = APIRouter()\n\n@router.post(\"/grade\")\ndef ai_grade(payload: dict, db: Session = Depends(get_db), user: User = Depends(get_current_user)):\n    task = grade_answer.apply_async(args=(payload.get('model', 'gemma-3-270m'), payload['question'], payload['answer']))\n    # 保存答题记录，状态pending\n    sa = StudentAnswer(\n        question_id=payload.get('question_id'),\n        student_id=user.id,\n        answer=payload['answer'],\n        score=None,\n        ai_explanation='',\n        answer_image_url=payload.get('answer_image_url',''),\n        submit_time=datetime.datetime.now()\n    )\n    db.add(sa)\n    db.commit()\n    return {\"task_id\": task.id}\n\n@router.get(\"/grade-result/{task_id}\")\ndef get_grade_result(task_id: str):\n    from backend.celery_worker import grade_answer\n    task = grade_answer.AsyncResult(task_id)\n    if not task.ready():\n        return {\"status\": \"pending\"}\n    return {\"status\": \"done\", \"result\": task.result}",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/celery_worker.py",
        "language": "python",
        "code": "from celery import Celery\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\ncelery_app = Celery('ai_tasks', broker='redis://redis:6379/0')\n\nMODEL_CACHE = {}\n\ndef load_model(model_name):\n    if model_name not in MODEL_CACHE:\n        path = f\"/mnt/nas/models/{model_name}\"\n        tokenizer = AutoTokenizer.from_pretrained(path)\n        model = AutoModelForCausalLM.from_pretrained(path)\n        MODEL_CACHE[model_name] = (tokenizer, model)\n    return MODEL_CACHE[model_name]\n\n@celery_app.task\ndef grade_answer(model_name, question, answer):\n    tokenizer, model = load_model(model_name)\n    prompt = f\"题目：{question}\\n学生答案：{answer}\\n请判断正误并给出解析：\"\n    inputs = tokenizer(prompt, return_tensors=\"pt\")\n    outputs = model.generate(**inputs, max_new_tokens=128)\n    result = tokenizer.decode(outputs[0], skip_special_tokens=True)\n    return result",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/auth.py",
        "language": "python",
        "code": "from fastapi import Depends, HTTPException, status\nfrom fastapi.security import OAuth2PasswordBearer\nfrom jose import JWTError, jwt\nfrom sqlalchemy.orm import Session\nfrom backend.database import get_db\nfrom backend.models import User\nimport datetime\n\nSECRET_KEY = \"your-secret-key\"\nALGORITHM = \"HS256\"\nACCESS_TOKEN_EXPIRE_MINUTES = 30\n\noauth2_scheme = OAuth2PasswordBearer(tokenUrl=\"token\")\n\ndef create_access_token(data: dict):\n    to_encode = data.copy()\n    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)\n    to_encode.update({\"exp\": expire})\n    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)\n    return encoded_jwt\n\nasync def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):\n    credentials_exception = HTTPException(\n        status_code=status.HTTP_401_UNAUTHORIZED,\n        detail=\"Could not validate credentials\",\n        headers={\"WWW-Authenticate\": \"Bearer\"},\n    )\n    try:\n        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])\n        username: str = payload.get(\"sub\")\n        if username is None:\n            raise credentials_exception\n    except JWTError:\n        raise credentials_exception\n    \n    user = db.query(User).filter(User.username == username).first()\n    if user is None:\n        raise credentials_exception\n    return user",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/main.js",
        "language": "javascript",
        "code": "import { createApp } from 'vue'\nimport ElementPlus from 'element-plus'\nimport 'element-plus/dist/index.css'\nimport { createPinia } from 'pinia'\nimport App from './App.vue'\nimport router from './router'\n\nconst app = createApp(App)\napp.use(ElementPlus)\napp.use(createPinia())\napp.use(router)\napp.mount('#app')",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/router/index.js",
        "language": "javascript",
        "code": "import { createRouter, createWebHistory } from 'vue-router'\nimport Home from '../views/Home.vue'\nimport Login from '../views/Login.vue'\nimport StudentDashboard from '../views/StudentDashboard.vue'\nimport TeacherDashboard from '../views/TeacherDashboard.vue'\nimport AdminPanel from '../views/AdminPanel.vue'\n\nconst routes = [\n  { path: '/', component: Home },\n  { path: '/login', component: Login },\n  { \n    path: '/student', \n    component: StudentDashboard, \n    meta: { requiresAuth: true, role: 'student' } \n  },\n  { \n    path: '/teacher', \n    component: TeacherDashboard, \n    meta: { requiresAuth: true, role: 'teacher' } \n  },\n  { \n    path: '/admin', \n    component: AdminPanel, \n    meta: { requiresAuth: true, role: 'admin' } \n  }\n]\n\nconst router = createRouter({\n  history: createWebHistory(),\n  routes\n})\n\n// 路由守卫\nrouter.beforeEach((to, from, next) => {\n  const token = localStorage.getItem('token')\n  const role = localStorage.getItem('role')\n  \n  if (to.meta.requiresAuth) {\n    if (!token) {\n      next('/login')\n    } else if (to.meta.role && to.meta.role !== role) {\n      next('/login')\n    } else {\n      next()\n    }\n  } else {\n    next()\n  }\n})\n\nexport default router",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/views/TeacherDashboard.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"teacher-dashboard\">\n    <h1>教师控制台</h1>\n    <el-tabs v-model=\"activeTab\">\n      <el-tab-pane label=\"题库管理\" name=\"questions\">\n        <QuestionTable @importExcel=\"showImport = true\" />\n        <ExcelImport v-if=\"showImport\" @close=\"showImport = false\" />\n      </el-tab-pane>\n      <el-tab-pane label=\"作业管理\" name=\"homework\">\n        <HomeworkList />\n      </el-tab-pane>\n      <el-tab-pane label=\"作业批改\" name=\"review\">\n        <HomeworkReview />\n      </el-tab-pane>\n    </el-tabs>\n  </div>\n</template>\n\n<script setup>\nimport { ref } from 'vue'\nimport QuestionTable from '@/components/QuestionTable.vue'\nimport ExcelImport from '@/components/ExcelImport.vue'\nimport HomeworkList from '@/components/HomeworkList.vue'\nimport HomeworkReview from '@/components/HomeworkReview.vue'\n\nconst activeTab = ref('questions')\nconst showImport = ref(false)\n</script>\n\n<style scoped>\n.teacher-dashboard {\n  padding: 20px;\n}\n</style>",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/components/QuestionTable.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"question-table\">\n    <div class=\"actions\">\n      <el-button type=\"primary\" @click=\"$emit('importExcel')\">Excel导入</el-button>\n    </div>\n    \n    <el-table :data=\"questions\" style=\"width: 100%\">\n      <el-table-column prop=\"content\" label=\"题干\" />\n      <el-table-column prop=\"difficulty\" label=\"难度\" />\n      <el-table-column prop=\"tags\" label=\"标签\" />\n      <el-table-column label=\"操作\">\n        <template #default=\"scope\">\n          <el-button @click=\"viewQuestion(scope.row)\">查看</el-button>\n        </template>\n      </el-table-column>\n    </el-table>\n    \n    <el-dialog v-model=\"dialogVisible\" title=\"题目详情\" width=\"50%\">\n      <div v-if=\"selectedQuestion\">\n        <p><strong>题干:</strong> {{ selectedQuestion.content }}</p>\n        <p v-if=\"selectedQuestion.image_url\">\n          <img :src=\"selectedQuestion.image_url\" style=\"max-width: 300px;\" />\n        </p>\n        <p><strong>难度:</strong> {{ selectedQuestion.difficulty }}</p>\n        <p><strong>标签:</strong> {{ selectedQuestion.tags }}</p>\n        <p><strong>解析:</strong> {{ selectedQuestion.explanation }}</p>\n      </div>\n      <template #footer>\n        <el-button @click=\"dialogVisible = false\">关闭</el-button>\n      </template>\n    </el-dialog>\n  </div>\n</template>\n\n<script setup>\nimport { ref, onMounted } from 'vue'\nimport axios from '@/api'\n\nconst questions = ref([])\nconst dialogVisible = ref(false)\nconst selectedQuestion = ref(null)\n\nconst emit = defineEmits(['importExcel'])\n\nonMounted(async () => {\n  try {\n    const response = await axios.get('/questions')\n    questions.value = response.data.items\n  } catch (error) {\n    console.error('获取题库失败:', error)\n  }\n})\n\nconst viewQuestion = (question) => {\n  selectedQuestion.value = question\n  dialogVisible.value = true\n}\n</script>\n\n<style scoped>\n.question-table {\n  margin-top: 20px;\n}\n.actions {\n  margin-bottom: 20px;\n}\n</style>",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/components/ExcelImport.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"excel-import\">\n    <el-card>\n      <h2>题库Excel导入</h2>\n      <div class=\"template-download\">\n        <el-link :href=\"templateUrl\" target=\"_blank\">下载Excel模板</el-link>\n      </div>\n      \n      <el-upload\n        class=\"upload-demo\"\n        :action=\"uploadUrl\"\n        :headers=\"{ Authorization: 'Bearer ' + token }\"\n        :on-success=\"handleSuccess\"\n        :on-error=\"handleError\"\n        :file-list=\"fileList\"\n        accept=\".xlsx, .xls\"\n      >\n        <el-button type=\"primary\">点击上传</el-button>\n        <template #tip>\n          <div class=\"el-upload__tip\">\n            只能上传xlsx/xls文件，且不超过10MB\n          </div>\n        </template>\n      </el-upload>\n      \n      <el-alert\n        v-if=\"message\"\n        :title=\"message\"\n        :type=\"messageType\"\n        show-icon\n        style=\"margin-top: 20px;\"\n      />\n      \n      <div class=\"actions\">\n        <el-button @click=\"$emit('close')\">关闭</el-button>\n      </div>\n    </el-card>\n  </div>\n</template>\n\n<script setup>\nimport { ref } from 'vue'\nimport axios from '@/api'\n\nconst emit = defineEmits(['close'])\n\nconst token = localStorage.getItem('token')\nconst templateUrl = '/api/questions/excel-template'\nconst uploadUrl = '/api/questions/import-excel'\nconst fileList = ref([])\nconst message = ref('')\nconst messageType = ref('success')\n\nconst handleSuccess = (response) => {\n  message.value = response.msg || '导入成功'\n  messageType.value = 'success'\n  fileList.value = []\n}\n\nconst handleError = (error) => {\n  message.value = '导入失败'\n  messageType.value = 'error'\n  console.error('导入错误:', error)\n}\n</script>\n\n<style scoped>\n.excel-import {\n  margin-top: 20px;\n}\n.template-download {\n  margin-bottom: 20px;\n}\n.actions {\n  margin-top: 20px;\n  text-align: right;\n}\n</style>",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/components/HomeworkReview.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"homework-review\">\n    <h2>作业批改</h2>\n    \n    <el-table :data=\"assignments\" style=\"width: 100%\">\n      <el-table-column prop=\"studentName\" label=\"学生\" />\n      <el-table-column prop=\"question\" label=\"题目\" />\n      <el-table-column prop=\"answer\" label=\"学生答案\" />\n      <el-table-column prop=\"ai_explanation\" label=\"AI解析\" />\n      <el-table-column label=\"评分\">\n        <template #default=\"scope\">\n          <el-input-number \n            v-model=\"scope.row.score\" \n            :min=\"0\" \n            :max=\"100\" \n            :precision=\"1\"\n          />\n        </template>\n      </el-table-column>\n      <el-table-column label=\"批语\">\n        <template #default=\"scope\">\n          <el-input v-model=\"scope.row.comment\" />\n        </template>\n      </el-table-column>\n      <el-table-column label=\"操作\">\n        <template #default=\"scope\">\n          <el-button \n            type=\"primary\" \n            @click=\"submitReview(scope.row)\"\n            :disabled=\"scope.row.submitted\"\n          >\n            {{ scope.row.submitted ? '已提交' : '提交' }}\n          </el-button>\n        </template>\n      </el-table-column>\n    </el-table>\n  </div>\n</template>\n\n<script setup>\nimport { ref, onMounted } from 'vue'\nimport axios from '@/api'\n\nconst assignments = ref([])\n\nonMounted(async () => {\n  try {\n    const response = await axios.get('/homework/review-list')\n    assignments.value = response.data.items\n  } catch (error) {\n    console.error('获取作业列表失败:', error)\n  }\n})\n\nconst submitReview = async (assignment) => {\n  try {\n    await axios.post('/homework/review', {\n      id: assignment.id,\n      score: assignment.score,\n      comment: assignment.comment\n    })\n    \n    assignment.submitted = true\n    ElMessage.success('批改成功')\n  } catch (error) {\n    console.error('提交批改失败:', error)\n    ElMessage.error('提交失败')\n  }\n}\n</script>\n\n<style scoped>\n.homework-review {\n  margin-top: 20px;\n}\n</style>",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/api/index.js",
        "language": "javascript",
        "code": "import axios from 'axios'\nimport { ElMessage } from 'element-plus'\n\nconst api = axios.create({\n  baseURL: '/api', // 配置代理\n  timeout: 10000\n})\n\n// 请求拦截器\napi.interceptors.request.use(\n  config => {\n    const token = localStorage.getItem('token')\n    if (token) {\n      config.headers.Authorization = `Bearer ${token}`\n    }\n    return config\n  },\n  error => {\n    return Promise.reject(error)\n  }\n)\n\n// 响应拦截器\napi.interceptors.response.use(\n  response => {\n    return response.data\n  },\n  error => {\n    if (error.response && error.response.status === 401) {\n      localStorage.removeItem('token')\n      localStorage.removeItem('role')\n      window.location.href = '/login'\n      ElMessage.error('登录已过期，请重新登录')\n    }\n    return Promise.reject(error)\n  }\n)\n\nexport default api",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "docker-compose.yml",
        "language": "yaml",
        "code": "version: '3.8'\n\nservices:\n  backend:\n    build: ./backend\n    container_name: edu-ai-backend\n    ports:\n      - \"8000:8000\"\n    environment:\n      - DATABASE_URL=mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db\n      - CELERY_BROKER_URL=redis://redis:6379/0\n    volumes:\n      - /mnt/nas/models:/mnt/nas/models\n    depends_on:\n      - mariadb\n      - redis\n\n  frontend:\n    build: ./frontend\n    container_name: edu-ai-frontend\n    ports:\n      - \"5173:80\"\n    depends_on:\n      - backend\n\n  mariadb:\n    image: mariadb:10.6\n    container_name: edu-ai-mariadb\n    environment:\n      MYSQL_ROOT_PASSWORD: yourpassword\n      MYSQL_DATABASE: edu_ai_db\n    volumes:\n      - /mnt/nas/db:/var/lib/mysql\n    ports:\n      - \"3306:3306\"\n\n  redis:\n    image: redis:6-alpine\n    container_name: edu-ai-redis\n    ports:\n      - \"6379:6379\"\n\n  celery:\n    build: \n      context: ./backend\n      dockerfile: Dockerfile.celery\n    container_name: edu-ai-celery\n    environment:\n      - DATABASE_URL=mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db\n      - CELERY_BROKER_URL=redis://redis:6379/0\n    volumes:\n      - /mnt/nas/models:/mnt/nas/models\n    depends_on:\n      - mariadb\n      - redis",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "k8s/edu-ai-ingress.yaml",
        "language": "yaml",
        "code": "apiVersion: networking.k8s.io/v1\nkind: Ingress\nmetadata:\n  name: edu-ai-ingress\n  annotations:\n    nginx.ingress.kubernetes.io/rewrite-target: /$2\n    nginx.ingress.kubernetes.io/ssl-redirect: \"true\"\n    cert-manager.io/cluster-issuer: \"letsencrypt-prod\"\nspec:\n  tls:\n  - hosts:\n    - ai.yourdomain.com\n    secretName: edu-ai-tls\n  rules:\n  - host: ai.yourdomain.com\n    http:\n      paths:\n      - path: /api(/|$)(.*)\n        pathType: Prefix\n        backend:\n          service:\n            name: edu-ai-backend-service\n            port:\n              number: 8000\n      - path: /()(.*)\n        pathType: Prefix\n        backend:\n          service:\n            name: edu-ai-frontend-service\n            port:\n              number: 80",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "k8s/edu-ai-backend-deployment.yaml",
        "language": "yaml",
        "code": "apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: edu-ai-backend\nspec:\n  replicas: 2\n  selector:\n    matchLabels:\n      app: edu-ai-backend\n  template:\n    metadata:\n      labels:\n        app: edu-ai-backend\n    spec:\n      containers:\n      - name: backend\n        image: yourrepo/edu-ai-backend:latest\n        ports:\n        - containerPort: 8000\n        env:\n        - name: DATABASE_URL\n          value: \"mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db\"\n        - name: CELERY_BROKER_URL\n          value: \"redis://redis:6379/0\"\n        volumeMounts:\n        - name: nas-models\n          mountPath: /mnt/nas/models\n      volumes:\n      - name: nas-models\n        persistentVolumeClaim:\n          claimName: nas-models-pvc",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "3.1题库管理流程",
        "language": "mermaid",
        "code": "graph TD\n    A[教师登录] --> B[进入题库管理]\n    B --> C{操作选择}\n    C -->|创建题目| D[填写题目信息]\n    C -->|编辑题目| E[修改题目信息]\n    C -->|删除题目| F[确认删除]\n    C -->|导入Excel| G[上传Excel文件]\n    D --> H[保存题目]\n    E --> H\n    G --> I[解析Excel数据]\n    I --> H\n    H --> J[更新题库]\n    F --> J",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "项目结构总览",
        "language": "plaintext",
        "code": "edu-ai-question-bank/\n├── backend/\n│   ├── controllers/\n│   │   ├── __init__.py\n│   │   ├── ai.py              # AI批改相关API\n│   │   ├── homework.py        # 作业相关API\n│   │   └── question.py       # 题库相关API\n│   ├── migrations/\n│   │   ├── env.py\n│   │   ├── script.py.mako\n│   │   └── versions/\n│   │       └── 20250101_init.py\n│   ├── static/\n│   │   └── question_import_template.xlsx\n│   ├── __init__.py\n│   ├── auth.py               # JWT认证\n│   ├── celery_worker.py      # Celery异步任务\n│   ├── database.py           # 数据库连接\n│   ├── main.py               # FastAPI入口\n│   ├── models.py             # 数据库模型\n│   ├── requirements.txt      # Python依赖\n│   └── Dockerfile            # 后端Dockerfile\n├── frontend/\n│   ├── public/\n│   │   └── index.html\n│   ├── src/\n│   │   ├── api/\n│   │   │   └── index.js      # axios封装\n│   │   ├── assets/\n│   │   ├── components/\n│   │   │   ├── ExcelImport.vue\n│   │   │   ├── HomeworkList.vue\n│   │   │   ├── HomeworkReview.vue\n│   │   │   └── QuestionTable.vue\n│   │   ├── router/\n│   │   │   └── index.js      # 路由配置\n│   │   ├── store/\n│   │   │   └── index.js      # Pinia状态管理\n│   │   ├── views/\n│   │   │   ├── AdminPanel.vue\n│   │   │   ├── Home.vue\n│   │   │   ├── Login.vue\n│   │   │   ├── StudentDashboard.vue\n│   │   │   ├── TeacherDashboard.vue\n│   │   │   └── Register.vue\n│   │   ├── App.vue\n│   │   └── main.js\n│   ├── package.json\n│   ├── vite.config.js\n│   └── Dockerfile            # 前端Dockerfile\n├── k8s/\n│   ├── edu-ai-backend-deployment.yaml\n│   ├── edu-ai-backend-service.yaml\n│   ├── edu-ai-ingress.yaml\n│   └── redis-deployment.yaml\n├── docker-compose.yml         # 本地开发环境\n└── README.md                 # 项目说明",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/main.py",
        "language": "python",
        "code": "from fastapi import FastAPI\nfrom fastapi.middleware.cors import CORSMiddleware\nfrom backend.controllers import ai, homework, question\nfrom backend.database import engine\nfrom backend.models import Base\n\n# 创建数据库表\nBase.metadata.create_all(bind=engine)\n\napp = FastAPI(title=\"教育AI题库系统\", version=\"1.0.0\")\n\n# 配置CORS\napp.add_middleware(\n    CORSMiddleware,\n    allow_origins=[\"*\"],\n    allow_credentials=True,\n    allow_methods=[\"*\"],\n    allow_headers=[\"*\"],\n)\n\n# 注册路由\napp.include_router(question.router, prefix=\"/api/questions\", tags=[\"题库管理\"])\napp.include_router(homework.router, prefix=\"/api/homework\", tags=[\"作业管理\"])\napp.include_router(ai.router, prefix=\"/api/ai\", tags=[\"AI服务\"])\n\n@app.get(\"/\")\ndef read_root():\n    return {\"message\": \"教育AI题库系统 API\"}\n\nif __name__ == \"__main__\":\n    import uvicorn\n    uvicorn.run(app, host=\"0.0.0.0\", port=8000)",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/models.py",
        "language": "python",
        "code": "from sqlalchemy import Column, Integer, String, Text, Enum, DateTime, ForeignKey, DECIMAL\nfrom sqlalchemy.orm import declarative_base, relationship\nimport enum\n\nBase = declarative_base()\n\nclass Difficulty(enum.Enum):\n    easy = '易'\n    medium = '中'\n    hard = '难'\n    olympiad = '奥数'\n\nclass User(Base):\n    __tablename__ = 'users'\n    id = Column(Integer, primary_key=True)\n    username = Column(String(100), unique=True)\n    password_hash = Column(String(255))\n    name = Column(String(100))\n    role = Column(Enum('student','teacher','admin','parent'))\n    register_time = Column(DateTime)\n\nclass Subject(Base):\n    __tablename__ = 'subjects'\n    id = Column(Integer, primary_key=True)\n    name = Column(String(50))\n    description = Column(String(255))\n\nclass Question(Base):\n    __tablename__ = 'questions'\n    id = Column(Integer, primary_key=True)\n    subject_id = Column(Integer, ForeignKey('subjects.id'))\n    type_id = Column(Integer)\n    content = Column(Text)\n    option_a = Column(String(255))\n    option_b = Column(String(255))\n    option_c = Column(String(255))\n    option_d = Column(String(255))\n    answer = Column(String(255))\n    explanation = Column(Text)\n    knowledge_point = Column(String(255))\n    difficulty = Column(Enum(Difficulty))\n    tags = Column(String(255))\n    image_url = Column(String(255))\n    extra_json = Column(Text)\n    created_by = Column(Integer, ForeignKey('users.id'))\n    created_at = Column(DateTime)\n    updated_at = Column(DateTime)\n    subject = relationship(\"Subject\")\n    creator = relationship(\"User\")\n\nclass StudentAnswer(Base):\n    __tablename__ = 'student_answers'\n    id = Column(Integer, primary_key=True)\n    question_id = Column(Integer, ForeignKey('questions.id'))\n    student_id = Column(Integer, ForeignKey('users.id'))\n    answer = Column(Text)\n    score = Column(DECIMAL(5,2))\n    ai_explanation = Column(Text)\n    answer_image_url = Column(String(255))\n    submit_time = Column(DateTime)\n\nclass Homework(Base):\n    __tablename__ = 'homework'\n    id = Column(Integer, primary_key=True)\n    teacher_id = Column(Integer, ForeignKey('users.id'))\n    title = Column(String(255))\n    publish_time = Column(DateTime)\n\nclass HomeworkAssignment(Base):\n    __tablename__ = 'homework_assignments'\n    id = Column(Integer, primary_key=True)\n    homework_id = Column(Integer, ForeignKey('homework.id'))\n    student_id = Column(Integer, ForeignKey('users.id'))\n    question_id = Column(Integer, ForeignKey('questions.id'))\n    answer = Column(Text)\n    score = Column(DECIMAL(5,2))\n    comment = Column(Text)\n    ai_explanation = Column(Text)\n    submit_time = Column(DateTime)\n    review_time = Column(DateTime)",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/controllers/question.py",
        "language": "python",
        "code": "from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Response\nfrom sqlalchemy.orm import Session\nfrom backend.models import Question, User\nfrom backend.database import get_db\nfrom backend.auth import get_current_user\nimport pandas as pd\nimport datetime\nimport os\n\nrouter = APIRouter()\n\n@router.get(\"/\")\ndef get_questions(subject_id: int = None, db: Session = Depends(get_db)):\n    query = db.query(Question)\n    if subject_id:\n        query = query.filter(Question.subject_id == subject_id)\n    return {\"items\": [q.to_dict() for q in query.limit(100)]}\n\n@router.post(\"/\", dependencies=[Depends(get_current_user)])\ndef create_question(q: dict, db: Session = Depends(get_db), user: User = Depends(get_current_user)):\n    nq = Question(**q, created_by=user.id, created_at=datetime.datetime.now())\n    db.add(nq)\n    db.commit()\n    return {\"msg\": \"题目已创建\", \"id\": nq.id}\n\n@router.post(\"/import-excel\", dependencies=[Depends(get_current_user)])\nasync def import_excel(file: UploadFile = File(...), db: Session = Depends(get_db), user: User = Depends(get_current_user)):\n    df = pd.read_excel(file.file)\n    for _, row in df.iterrows():\n        nq = Question(\n            content=row['题干'],\n            subject_id=row['学科ID'],\n            difficulty=row['难度'],\n            tags=row.get('标签',''),\n            option_a=row.get('option_a',''),\n            option_b=row.get('option_b',''),\n            option_c=row.get('option_c',''),\n            option_d=row.get('option_d',''),\n            answer=row.get('answer',''),\n            explanation=row.get('解析',''),\n            image_url=row.get('image_url',''),\n            extra_json=row.get('extra_json',None),\n            created_by=user.id,\n            created_at=datetime.datetime.now()\n        )\n        db.add(nq)\n    db.commit()\n    return {\"msg\": \"Excel导入成功\"}\n\n@router.get(\"/excel-template\")\ndef download_excel_template():\n    template_path = \"static/question_import_template.xlsx\"\n    if not os.path.exists(template_path):\n        # 创建模板文件\n        import pandas as pd\n        df = pd.DataFrame([{\n            \"题干\": \"勾股定理是什么\",\n            \"学科ID\": 1,\n            \"难度\": \"奥数\",\n            \"标签\": \"数学\",\n            \"option_a\": \"\",\n            \"option_b\": \"\",\n            \"option_c\": \"\",\n            \"option_d\": \"\",\n            \"answer\": \"\",\n            \"解析\": \"a^2+b^2=c^2\",\n            \"image_url\": \"http://xxx\",\n            \"extra_json\": '{\"latex\":\"a^2+b^2=c^2\"}'\n        }])\n        os.makedirs(\"static\", exist_ok=True)\n        df.to_excel(template_path, index=False)\n    return Response(content=open(template_path, \"rb\").read(), \n                   media_type=\"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet\")",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/controllers/ai.py",
        "language": "python",
        "code": "from fastapi import APIRouter, Depends, BackgroundTasks\nfrom backend.auth import get_current_user\nfrom backend.celery_worker import grade_answer\nfrom sqlalchemy.orm import Session\nfrom backend.database import get_db\nfrom backend.models import StudentAnswer, User\nimport datetime\n\nrouter = APIRouter()\n\n@router.post(\"/grade\")\ndef ai_grade(payload: dict, db: Session = Depends(get_db), user: User = Depends(get_current_user)):\n    task = grade_answer.apply_async(args=(payload.get('model', 'gemma-3-270m'), payload['question'], payload['answer']))\n    # 保存答题记录，状态pending\n    sa = StudentAnswer(\n        question_id=payload.get('question_id'),\n        student_id=user.id,\n        answer=payload['answer'],\n        score=None,\n        ai_explanation='',\n        answer_image_url=payload.get('answer_image_url',''),\n        submit_time=datetime.datetime.now()\n    )\n    db.add(sa)\n    db.commit()\n    return {\"task_id\": task.id}\n\n@router.get(\"/grade-result/{task_id}\")\ndef get_grade_result(task_id: str):\n    from backend.celery_worker import grade_answer\n    task = grade_answer.AsyncResult(task_id)\n    if not task.ready():\n        return {\"status\": \"pending\"}\n    return {\"status\": \"done\", \"result\": task.result}",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/celery_worker.py",
        "language": "python",
        "code": "from celery import Celery\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\ncelery_app = Celery('ai_tasks', broker='redis://redis:6379/0')\n\nMODEL_CACHE = {}\n\ndef load_model(model_name):\n    if model_name not in MODEL_CACHE:\n        path = f\"/mnt/nas/models/{model_name}\"\n        tokenizer = AutoTokenizer.from_pretrained(path)\n        model = AutoModelForCausalLM.from_pretrained(path)\n        MODEL_CACHE[model_name] = (tokenizer, model)\n    return MODEL_CACHE[model_name]\n\n@celery_app.task\ndef grade_answer(model_name, question, answer):\n    tokenizer, model = load_model(model_name)\n    prompt = f\"题目：{question}\\n学生答案：{answer}\\n请判断正误并给出解析：\"\n    inputs = tokenizer(prompt, return_tensors=\"pt\")\n    outputs = model.generate(**inputs, max_new_tokens=128)\n    result = tokenizer.decode(outputs[0], skip_special_tokens=True)\n    return result",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/auth.py",
        "language": "python",
        "code": "from fastapi import Depends, HTTPException, status\nfrom fastapi.security import OAuth2PasswordBearer\nfrom jose import JWTError, jwt\nfrom sqlalchemy.orm import Session\nfrom backend.database import get_db\nfrom backend.models import User\nimport datetime\n\nSECRET_KEY = \"your-secret-key\"\nALGORITHM = \"HS256\"\nACCESS_TOKEN_EXPIRE_MINUTES = 30\n\noauth2_scheme = OAuth2PasswordBearer(tokenUrl=\"token\")\n\ndef create_access_token(data: dict):\n    to_encode = data.copy()\n    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)\n    to_encode.update({\"exp\": expire})\n    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)\n    return encoded_jwt\n\nasync def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):\n    credentials_exception = HTTPException(\n        status_code=status.HTTP_401_UNAUTHORIZED,\n        detail=\"Could not validate credentials\",\n        headers={\"WWW-Authenticate\": \"Bearer\"},\n    )\n    try:\n        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])\n        username: str = payload.get(\"sub\")\n        if username is None:\n            raise credentials_exception\n    except JWTError:\n        raise credentials_exception\n    \n    user = db.query(User).filter(User.username == username).first()\n    if user is None:\n        raise credentials_exception\n    return user",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/main.js",
        "language": "javascript",
        "code": "import { createApp } from 'vue'\nimport ElementPlus from 'element-plus'\nimport 'element-plus/dist/index.css'\nimport { createPinia } from 'pinia'\nimport App from './App.vue'\nimport router from './router'\n\nconst app = createApp(App)\napp.use(ElementPlus)\napp.use(createPinia())\napp.use(router)\napp.mount('#app')",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/router/index.js",
        "language": "javascript",
        "code": "import { createRouter, createWebHistory } from 'vue-router'\nimport Home from '../views/Home.vue'\nimport Login from '../views/Login.vue'\nimport StudentDashboard from '../views/StudentDashboard.vue'\nimport TeacherDashboard from '../views/TeacherDashboard.vue'\nimport AdminPanel from '../views/AdminPanel.vue'\n\nconst routes = [\n  { path: '/', component: Home },\n  { path: '/login', component: Login },\n  { \n    path: '/student', \n    component: StudentDashboard, \n    meta: { requiresAuth: true, role: 'student' } \n  },\n  { \n    path: '/teacher', \n    component: TeacherDashboard, \n    meta: { requiresAuth: true, role: 'teacher' } \n  },\n  { \n    path: '/admin', \n    component: AdminPanel, \n    meta: { requiresAuth: true, role: 'admin' } \n  }\n]\n\nconst router = createRouter({\n  history: createWebHistory(),\n  routes\n})\n\n// 路由守卫\nrouter.beforeEach((to, from, next) => {\n  const token = localStorage.getItem('token')\n  const role = localStorage.getItem('role')\n  \n  if (to.meta.requiresAuth) {\n    if (!token) {\n      next('/login')\n    } else if (to.meta.role && to.meta.role !== role) {\n      next('/login')\n    } else {\n      next()\n    }\n  } else {\n    next()\n  }\n})\n\nexport default router",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/views/TeacherDashboard.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"teacher-dashboard\">\n    <h1>教师控制台</h1>\n    <el-tabs v-model=\"activeTab\">\n      <el-tab-pane label=\"题库管理\" name=\"questions\">\n        <QuestionTable @importExcel=\"showImport = true\" />\n        <ExcelImport v-if=\"showImport\" @close=\"showImport = false\" />\n      </el-tab-pane>\n      <el-tab-pane label=\"作业管理\" name=\"homework\">\n        <HomeworkList />\n      </el-tab-pane>\n      <el-tab-pane label=\"作业批改\" name=\"review\">\n        <HomeworkReview />\n      </el-tab-pane>\n    </el-tabs>\n  </div>\n</template>\n\n<script setup>\nimport { ref } from 'vue'\nimport QuestionTable from '@/components/QuestionTable.vue'\nimport ExcelImport from '@/components/ExcelImport.vue'\nimport HomeworkList from '@/components/HomeworkList.vue'\nimport HomeworkReview from '@/components/HomeworkReview.vue'\n\nconst activeTab = ref('questions')\nconst showImport = ref(false)\n</script>\n\n<style scoped>\n.teacher-dashboard {\n  padding: 20px;\n}\n</style>",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/components/QuestionTable.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"question-table\">\n    <div class=\"actions\">\n      <el-button type=\"primary\" @click=\"$emit('importExcel')\">Excel导入</el-button>\n    </div>\n    \n    <el-table :data=\"questions\" style=\"width: 100%\">\n      <el-table-column prop=\"content\" label=\"题干\" />\n      <el-table-column prop=\"difficulty\" label=\"难度\" />\n      <el-table-column prop=\"tags\" label=\"标签\" />\n      <el-table-column label=\"操作\">\n        <template #default=\"scope\">\n          <el-button @click=\"viewQuestion(scope.row)\">查看</el-button>\n        </template>\n      </el-table-column>\n    </el-table>\n    \n    <el-dialog v-model=\"dialogVisible\" title=\"题目详情\" width=\"50%\">\n      <div v-if=\"selectedQuestion\">\n        <p><strong>题干:</strong> {{ selectedQuestion.content }}</p>\n        <p v-if=\"selectedQuestion.image_url\">\n          <img :src=\"selectedQuestion.image_url\" style=\"max-width: 300px;\" />\n        </p>\n        <p><strong>难度:</strong> {{ selectedQuestion.difficulty }}</p>\n        <p><strong>标签:</strong> {{ selectedQuestion.tags }}</p>\n        <p><strong>解析:</strong> {{ selectedQuestion.explanation }}</p>\n      </div>\n      <template #footer>\n        <el-button @click=\"dialogVisible = false\">关闭</el-button>\n      </template>\n    </el-dialog>\n  </div>\n</template>\n\n<script setup>\nimport { ref, onMounted } from 'vue'\nimport axios from '@/api'\n\nconst questions = ref([])\nconst dialogVisible = ref(false)\nconst selectedQuestion = ref(null)\n\nconst emit = defineEmits(['importExcel'])\n\nonMounted(async () => {\n  try {\n    const response = await axios.get('/questions')\n    questions.value = response.data.items\n  } catch (error) {\n    console.error('获取题库失败:', error)\n  }\n})\n\nconst viewQuestion = (question) => {\n  selectedQuestion.value = question\n  dialogVisible.value = true\n}\n</script>\n\n<style scoped>\n.question-table {\n  margin-top: 20px;\n}\n.actions {\n  margin-bottom: 20px;\n}\n</style>",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/components/ExcelImport.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"excel-import\">\n    <el-card>\n      <h2>题库Excel导入</h2>\n      <div class=\"template-download\">\n        <el-link :href=\"templateUrl\" target=\"_blank\">下载Excel模板</el-link>\n      </div>\n      \n      <el-upload\n        class=\"upload-demo\"\n        :action=\"uploadUrl\"\n        :headers=\"{ Authorization: 'Bearer ' + token }\"\n        :on-success=\"handleSuccess\"\n        :on-error=\"handleError\"\n        :file-list=\"fileList\"\n        accept=\".xlsx, .xls\"\n      >\n        <el-button type=\"primary\">点击上传</el-button>\n        <template #tip>\n          <div class=\"el-upload__tip\">\n            只能上传xlsx/xls文件，且不超过10MB\n          </div>\n        </template>\n      </el-upload>\n      \n      <el-alert\n        v-if=\"message\"\n        :title=\"message\"\n        :type=\"messageType\"\n        show-icon\n        style=\"margin-top: 20px;\"\n      />\n      \n      <div class=\"actions\">\n        <el-button @click=\"$emit('close')\">关闭</el-button>\n      </div>\n    </el-card>\n  </div>\n</template>\n\n<script setup>\nimport { ref } from 'vue'\nimport axios from '@/api'\n\nconst emit = defineEmits(['close'])\n\nconst token = localStorage.getItem('token')\nconst templateUrl = '/api/questions/excel-template'\nconst uploadUrl = '/api/questions/import-excel'\nconst fileList = ref([])\nconst message = ref('')\nconst messageType = ref('success')\n\nconst handleSuccess = (response) => {\n  message.value = response.msg || '导入成功'\n  messageType.value = 'success'\n  fileList.value = []\n}\n\nconst handleError = (error) => {\n  message.value = '导入失败'\n  messageType.value = 'error'\n  console.error('导入错误:', error)\n}\n</script>\n\n<style scoped>\n.excel-import {\n  margin-top: 20px;\n}\n.template-download {\n  margin-bottom: 20px;\n}\n.actions {\n  margin-top: 20px;\n  text-align: right;\n}\n</style>",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/components/HomeworkReview.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"homework-review\">\n    <h2>作业批改</h2>\n    \n    <el-table :data=\"assignments\" style=\"width: 100%\">\n      <el-table-column prop=\"studentName\" label=\"学生\" />\n      <el-table-column prop=\"question\" label=\"题目\" />\n      <el-table-column prop=\"answer\" label=\"学生答案\" />\n      <el-table-column prop=\"ai_explanation\" label=\"AI解析\" />\n      <el-table-column label=\"评分\">\n        <template #default=\"scope\">\n          <el-input-number \n            v-model=\"scope.row.score\" \n            :min=\"0\" \n            :max=\"100\" \n            :precision=\"1\"\n          />\n        </template>\n      </el-table-column>\n      <el-table-column label=\"批语\">\n        <template #default=\"scope\">\n          <el-input v-model=\"scope.row.comment\" />\n        </template>\n      </el-table-column>\n      <el-table-column label=\"操作\">\n        <template #default=\"scope\">\n          <el-button \n            type=\"primary\" \n            @click=\"submitReview(scope.row)\"\n            :disabled=\"scope.row.submitted\"\n          >\n            {{ scope.row.submitted ? '已提交' : '提交' }}\n          </el-button>\n        </template>\n      </el-table-column>\n    </el-table>\n  </div>\n</template>\n\n<script setup>\nimport { ref, onMounted } from 'vue'\nimport axios from '@/api'\n\nconst assignments = ref([])\n\nonMounted(async () => {\n  try {\n    const response = await axios.get('/homework/review-list')\n    assignments.value = response.data.items\n  } catch (error) {\n    console.error('获取作业列表失败:', error)\n  }\n})\n\nconst submitReview = async (assignment) => {\n  try {\n    await axios.post('/homework/review', {\n      id: assignment.id,\n      score: assignment.score,\n      comment: assignment.comment\n    })\n    \n    assignment.submitted = true\n    ElMessage.success('批改成功')\n  } catch (error) {\n    console.error('提交批改失败:', error)\n    ElMessage.error('提交失败')\n  }\n}\n</script>\n\n<style scoped>\n.homework-review {\n  margin-top: 20px;\n}\n</style>",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/api/index.js",
        "language": "javascript",
        "code": "import axios from 'axios'\nimport { ElMessage } from 'element-plus'\n\nconst api = axios.create({\n  baseURL: '/api', // 配置代理\n  timeout: 10000\n})\n\n// 请求拦截器\napi.interceptors.request.use(\n  config => {\n    const token = localStorage.getItem('token')\n    if (token) {\n      config.headers.Authorization = `Bearer ${token}`\n    }\n    return config\n  },\n  error => {\n    return Promise.reject(error)\n  }\n)\n\n// 响应拦截器\napi.interceptors.response.use(\n  response => {\n    return response.data\n  },\n  error => {\n    if (error.response && error.response.status === 401) {\n      localStorage.removeItem('token')\n      localStorage.removeItem('role')\n      window.location.href = '/login'\n      ElMessage.error('登录已过期，请重新登录')\n    }\n    return Promise.reject(error)\n  }\n)\n\nexport default api",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "docker-compose.yml",
        "language": "yaml",
        "code": "version: '3.8'\n\nservices:\n  backend:\n    build: ./backend\n    container_name: edu-ai-backend\n    ports:\n      - \"8000:8000\"\n    environment:\n      - DATABASE_URL=mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db\n      - CELERY_BROKER_URL=redis://redis:6379/0\n    volumes:\n      - /mnt/nas/models:/mnt/nas/models\n    depends_on:\n      - mariadb\n      - redis\n\n  frontend:\n    build: ./frontend\n    container_name: edu-ai-frontend\n    ports:\n      - \"5173:80\"\n    depends_on:\n      - backend\n\n  mariadb:\n    image: mariadb:10.6\n    container_name: edu-ai-mariadb\n    environment:\n      MYSQL_ROOT_PASSWORD: yourpassword\n      MYSQL_DATABASE: edu_ai_db\n    volumes:\n      - /mnt/nas/db:/var/lib/mysql\n    ports:\n      - \"3306:3306\"\n\n  redis:\n    image: redis:6-alpine\n    container_name: edu-ai-redis\n    ports:\n      - \"6379:6379\"\n\n  celery:\n    build: \n      context: ./backend\n      dockerfile: Dockerfile.celery\n    container_name: edu-ai-celery\n    environment:\n      - DATABASE_URL=mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db\n      - CELERY_BROKER_URL=redis://redis:6379/0\n    volumes:\n      - /mnt/nas/models:/mnt/nas/models\n    depends_on:\n      - mariadb\n      - redis",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "k8s/edu-ai-ingress.yaml",
        "language": "yaml",
        "code": "apiVersion: networking.k8s.io/v1\nkind: Ingress\nmetadata:\n  name: edu-ai-ingress\n  annotations:\n    nginx.ingress.kubernetes.io/rewrite-target: /$2\n    nginx.ingress.kubernetes.io/ssl-redirect: \"true\"\n    cert-manager.io/cluster-issuer: \"letsencrypt-prod\"\nspec:\n  tls:\n  - hosts:\n    - ai.yourdomain.com\n    secretName: edu-ai-tls\n  rules:\n  - host: ai.yourdomain.com\n    http:\n      paths:\n      - path: /api(/|$)(.*)\n        pathType: Prefix\n        backend:\n          service:\n            name: edu-ai-backend-service\n            port:\n              number: 8000\n      - path: /()(.*)\n        pathType: Prefix\n        backend:\n          service:\n            name: edu-ai-frontend-service\n            port:\n              number: 80",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "k8s/edu-ai-backend-deployment.yaml",
        "language": "yaml",
        "code": "apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: edu-ai-backend\nspec:\n  replicas: 2\n  selector:\n    matchLabels:\n      app: edu-ai-backend\n  template:\n    metadata:\n      labels:\n        app: edu-ai-backend\n    spec:\n      containers:\n      - name: backend\n        image: yourrepo/edu-ai-backend:latest\n        ports:\n        - containerPort: 8000\n        env:\n        - name: DATABASE_URL\n          value: \"mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db\"\n        - name: CELERY_BROKER_URL\n          value: \"redis://redis:6379/0\"\n        volumeMounts:\n        - name: nas-models\n          mountPath: /mnt/nas/models\n      volumes:\n      - name: nas-models\n        persistentVolumeClaim:\n          claimName: nas-models-pvc",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "3.1题库管理流程",
        "language": "mermaid",
        "code": "graph TD\n    A[教师登录] --> B[进入题库管理]\n    B --> C{操作选择}\n    C -->|创建题目| D[填写题目信息]\n    C -->|编辑题目| E[修改题目信息]\n    C -->|删除题目| F[确认删除]\n    C -->|导入Excel| G[上传Excel文件]\n    D --> H[保存题目]\n    E --> H\n    G --> I[解析Excel数据]\n    I --> H\n    H --> J[更新题库]\n    F --> J",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/main.py",
        "language": "python",
        "code": "from fastapi import FastAPI\nfrom fastapi.middleware.cors import CORSMiddleware\nfrom backend.controllers import ai, homework, question\nfrom backend.database import engine\nfrom backend.models import Base\n\n# 创建数据库表\nBase.metadata.create_all(bind=engine)\n\napp = FastAPI(title=\"教育AI题库系统\", version=\"1.0.0\")\n\n# 配置CORS\napp.add_middleware(\n    CORSMiddleware,\n    allow_origins=[\"*\"],\n    allow_credentials=True,\n    allow_methods=[\"*\"],\n    allow_headers=[\"*\"],\n)\n\n# 注册路由\napp.include_router(question.router, prefix=\"/api/questions\", tags=[\"题库管理\"])\napp.include_router(homework.router, prefix=\"/api/homework\", tags=[\"作业管理\"])\napp.include_router(ai.router, prefix=\"/api/ai\", tags=[\"AI服务\"])\n\n@app.get(\"/\")\ndef read_root():\n    return {\"message\": \"教育AI题库系统 API\"}\n\nif __name__ == \"__main__\":\n    import uvicorn\n    uvicorn.run(app, host=\"0.0.0.0\", port=8000)",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/models.py",
        "language": "python",
        "code": "from sqlalchemy import Column, Integer, String, Text, Enum, DateTime, ForeignKey, DECIMAL\nfrom sqlalchemy.orm import declarative_base, relationship\nimport enum\n\nBase = declarative_base()\n\nclass Difficulty(enum.Enum):\n    easy = '易'\n    medium = '中'\n    hard = '难'\n    olympiad = '奥数'\n\nclass User(Base):\n    __tablename__ = 'users'\n    id = Column(Integer, primary_key=True)\n    username = Column(String(100), unique=True)\n    password_hash = Column(String(255))\n    name = Column(String(100))\n    role = Column(Enum('student','teacher','admin','parent'))\n    register_time = Column(DateTime)\n\nclass Subject(Base):\n    __tablename__ = 'subjects'\n    id = Column(Integer, primary_key=True)\n    name = Column(String(50))\n    description = Column(String(255))\n\nclass Question(Base):\n    __tablename__ = 'questions'\n    id = Column(Integer, primary_key=True)\n    subject_id = Column(Integer, ForeignKey('subjects.id'))\n    type_id = Column(Integer)\n    content = Column(Text)\n    option_a = Column(String(255))\n    option_b = Column(String(255))\n    option_c = Column(String(255))\n    option_d = Column(String(255))\n    answer = Column(String(255))\n    explanation = Column(Text)\n    knowledge_point = Column(String(255))\n    difficulty = Column(Enum(Difficulty))\n    tags = Column(String(255))\n    image_url = Column(String(255))\n    extra_json = Column(Text)\n    created_by = Column(Integer, ForeignKey('users.id'))\n    created_at = Column(DateTime)\n    updated_at = Column(DateTime)\n    subject = relationship(\"Subject\")\n    creator = relationship(\"User\")\n\nclass StudentAnswer(Base):\n    __tablename__ = 'student_answers'\n    id = Column(Integer, primary_key=True)\n    question_id = Column(Integer, ForeignKey('questions.id'))\n    student_id = Column(Integer, ForeignKey('users.id'))\n    answer = Column(Text)\n    score = Column(DECIMAL(5,2))\n    ai_explanation = Column(Text)\n    answer_image_url = Column(String(255))\n    submit_time = Column(DateTime)\n\nclass Homework(Base):\n    __tablename__ = 'homework'\n    id = Column(Integer, primary_key=True)\n    teacher_id = Column(Integer, ForeignKey('users.id'))\n    title = Column(String(255))\n    publish_time = Column(DateTime)\n\nclass HomeworkAssignment(Base):\n    __tablename__ = 'homework_assignments'\n    id = Column(Integer, primary_key=True)\n    homework_id = Column(Integer, ForeignKey('homework.id'))\n    student_id = Column(Integer, ForeignKey('users.id'))\n    question_id = Column(Integer, ForeignKey('questions.id'))\n    answer = Column(Text)\n    score = Column(DECIMAL(5,2))\n    comment = Column(Text)\n    ai_explanation = Column(Text)\n    submit_time = Column(DateTime)\n    review_time = Column(DateTime)",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/controllers/question.py",
        "language": "python",
        "code": "from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Response\nfrom sqlalchemy.orm import Session\nfrom backend.models import Question, User\nfrom backend.database import get_db\nfrom backend.auth import get_current_user\nimport pandas as pd\nimport datetime\nimport os\n\nrouter = APIRouter()\n\n@router.get(\"/\")\ndef get_questions(subject_id: int = None, db: Session = Depends(get_db)):\n    query = db.query(Question)\n    if subject_id:\n        query = query.filter(Question.subject_id == subject_id)\n    return {\"items\": [q.to_dict() for q in query.limit(100)]}\n\n@router.post(\"/\", dependencies=[Depends(get_current_user)])\ndef create_question(q: dict, db: Session = Depends(get_db), user: User = Depends(get_current_user)):\n    nq = Question(**q, created_by=user.id, created_at=datetime.datetime.now())\n    db.add(nq)\n    db.commit()\n    return {\"msg\": \"题目已创建\", \"id\": nq.id}\n\n@router.post(\"/import-excel\", dependencies=[Depends(get_current_user)])\nasync def import_excel(file: UploadFile = File(...), db: Session = Depends(get_db), user: User = Depends(get_current_user)):\n    df = pd.read_excel(file.file)\n    for _, row in df.iterrows():\n        nq = Question(\n            content=row['题干'],\n            subject_id=row['学科ID'],\n            difficulty=row['难度'],\n            tags=row.get('标签',''),\n            option_a=row.get('option_a',''),\n            option_b=row.get('option_b',''),\n            option_c=row.get('option_c',''),\n            option_d=row.get('option_d',''),\n            answer=row.get('answer',''),\n            explanation=row.get('解析',''),\n            image_url=row.get('image_url',''),\n            extra_json=row.get('extra_json',None),\n            created_by=user.id,\n            created_at=datetime.datetime.now()\n        )\n        db.add(nq)\n    db.commit()\n    return {\"msg\": \"Excel导入成功\"}\n\n@router.get(\"/excel-template\")\ndef download_excel_template():\n    template_path = \"static/question_import_template.xlsx\"\n    if not os.path.exists(template_path):\n        # 创建模板文件\n        import pandas as pd\n        df = pd.DataFrame([{\n            \"题干\": \"勾股定理是什么\",\n            \"学科ID\": 1,\n            \"难度\": \"奥数\",\n            \"标签\": \"数学\",\n            \"option_a\": \"\",\n            \"option_b\": \"\",\n            \"option_c\": \"\",\n            \"option_d\": \"\",\n            \"answer\": \"\",\n            \"解析\": \"a^2+b^2=c^2\",\n            \"image_url\": \"http://xxx\",\n            \"extra_json\": '{\"latex\":\"a^2+b^2=c^2\"}'\n        }])\n        os.makedirs(\"static\", exist_ok=True)\n        df.to_excel(template_path, index=False)\n    return Response(content=open(template_path, \"rb\").read(), \n                   media_type=\"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet\")",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/controllers/ai.py",
        "language": "python",
        "code": "from fastapi import APIRouter, Depends, BackgroundTasks\nfrom backend.auth import get_current_user\nfrom backend.celery_worker import grade_answer\nfrom sqlalchemy.orm import Session\nfrom backend.database import get_db\nfrom backend.models import StudentAnswer, User\nimport datetime\n\nrouter = APIRouter()\n\n@router.post(\"/grade\")\ndef ai_grade(payload: dict, db: Session = Depends(get_db), user: User = Depends(get_current_user)):\n    task = grade_answer.apply_async(args=(payload.get('model', 'gemma-3-270m'), payload['question'], payload['answer']))\n    # 保存答题记录，状态pending\n    sa = StudentAnswer(\n        question_id=payload.get('question_id'),\n        student_id=user.id,\n        answer=payload['answer'],\n        score=None,\n        ai_explanation='',\n        answer_image_url=payload.get('answer_image_url',''),\n        submit_time=datetime.datetime.now()\n    )\n    db.add(sa)\n    db.commit()\n    return {\"task_id\": task.id}\n\n@router.get(\"/grade-result/{task_id}\")\ndef get_grade_result(task_id: str):\n    from backend.celery_worker import grade_answer\n    task = grade_answer.AsyncResult(task_id)\n    if not task.ready():\n        return {\"status\": \"pending\"}\n    return {\"status\": \"done\", \"result\": task.result}",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/celery_worker.py",
        "language": "python",
        "code": "from celery import Celery\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\ncelery_app = Celery('ai_tasks', broker='redis://redis:6379/0')\n\nMODEL_CACHE = {}\n\ndef load_model(model_name):\n    if model_name not in MODEL_CACHE:\n        path = f\"/mnt/nas/models/{model_name}\"\n        tokenizer = AutoTokenizer.from_pretrained(path)\n        model = AutoModelForCausalLM.from_pretrained(path)\n        MODEL_CACHE[model_name] = (tokenizer, model)\n    return MODEL_CACHE[model_name]\n\n@celery_app.task\ndef grade_answer(model_name, question, answer):\n    tokenizer, model = load_model(model_name)\n    prompt = f\"题目：{question}\\n学生答案：{answer}\\n请判断正误并给出解析：\"\n    inputs = tokenizer(prompt, return_tensors=\"pt\")\n    outputs = model.generate(**inputs, max_new_tokens=128)\n    result = tokenizer.decode(outputs[0], skip_special_tokens=True)\n    return result",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "backend/auth.py",
        "language": "python",
        "code": "from fastapi import Depends, HTTPException, status\nfrom fastapi.security import OAuth2PasswordBearer\nfrom jose import JWTError, jwt\nfrom sqlalchemy.orm import Session\nfrom backend.database import get_db\nfrom backend.models import User\nimport datetime\n\nSECRET_KEY = \"your-secret-key\"\nALGORITHM = \"HS256\"\nACCESS_TOKEN_EXPIRE_MINUTES = 30\n\noauth2_scheme = OAuth2PasswordBearer(tokenUrl=\"token\")\n\ndef create_access_token(data: dict):\n    to_encode = data.copy()\n    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)\n    to_encode.update({\"exp\": expire})\n    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)\n    return encoded_jwt\n\nasync def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):\n    credentials_exception = HTTPException(\n        status_code=status.HTTP_401_UNAUTHORIZED,\n        detail=\"Could not validate credentials\",\n        headers={\"WWW-Authenticate\": \"Bearer\"},\n    )\n    try:\n        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])\n        username: str = payload.get(\"sub\")\n        if username is None:\n            raise credentials_exception\n    except JWTError:\n        raise credentials_exception\n    \n    user = db.query(User).filter(User.username == username).first()\n    if user is None:\n        raise credentials_exception\n    return user",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/main.js",
        "language": "javascript",
        "code": "import { createApp } from 'vue'\nimport ElementPlus from 'element-plus'\nimport 'element-plus/dist/index.css'\nimport { createPinia } from 'pinia'\nimport App from './App.vue'\nimport router from './router'\n\nconst app = createApp(App)\napp.use(ElementPlus)\napp.use(createPinia())\napp.use(router)\napp.mount('#app')",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/router/index.js",
        "language": "javascript",
        "code": "import { createRouter, createWebHistory } from 'vue-router'\nimport Home from '../views/Home.vue'\nimport Login from '../views/Login.vue'\nimport StudentDashboard from '../views/StudentDashboard.vue'\nimport TeacherDashboard from '../views/TeacherDashboard.vue'\nimport AdminPanel from '../views/AdminPanel.vue'\n\nconst routes = [\n  { path: '/', component: Home },\n  { path: '/login', component: Login },\n  { \n    path: '/student', \n    component: StudentDashboard, \n    meta: { requiresAuth: true, role: 'student' } \n  },\n  { \n    path: '/teacher', \n    component: TeacherDashboard, \n    meta: { requiresAuth: true, role: 'teacher' } \n  },\n  { \n    path: '/admin', \n    component: AdminPanel, \n    meta: { requiresAuth: true, role: 'admin' } \n  }\n]\n\nconst router = createRouter({\n  history: createWebHistory(),\n  routes\n})\n\n// 路由守卫\nrouter.beforeEach((to, from, next) => {\n  const token = localStorage.getItem('token')\n  const role = localStorage.getItem('role')\n  \n  if (to.meta.requiresAuth) {\n    if (!token) {\n      next('/login')\n    } else if (to.meta.role && to.meta.role !== role) {\n      next('/login')\n    } else {\n      next()\n    }\n  } else {\n    next()\n  }\n})\n\nexport default router",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/views/TeacherDashboard.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"teacher-dashboard\">\n    <h1>教师控制台</h1>\n    <el-tabs v-model=\"activeTab\">\n      <el-tab-pane label=\"题库管理\" name=\"questions\">\n        <QuestionTable @importExcel=\"showImport = true\" />\n        <ExcelImport v-if=\"showImport\" @close=\"showImport = false\" />\n      </el-tab-pane>\n      <el-tab-pane label=\"作业管理\" name=\"homework\">\n        <HomeworkList />\n      </el-tab-pane>\n      <el-tab-pane label=\"作业批改\" name=\"review\">\n        <HomeworkReview />\n      </el-tab-pane>\n    </el-tabs>\n  </div>\n</template>\n\n<script setup>\nimport { ref } from 'vue'\nimport QuestionTable from '@/components/QuestionTable.vue'\nimport ExcelImport from '@/components/ExcelImport.vue'\nimport HomeworkList from '@/components/HomeworkList.vue'\nimport HomeworkReview from '@/components/HomeworkReview.vue'\n\nconst activeTab = ref('questions')\nconst showImport = ref(false)\n</script>\n\n<style scoped>\n.teacher-dashboard {\n  padding: 20px;\n}\n</style>",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/components/QuestionTable.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"question-table\">\n    <div class=\"actions\">\n      <el-button type=\"primary\" @click=\"$emit('importExcel')\">Excel导入</el-button>\n    </div>\n    \n    <el-table :data=\"questions\" style=\"width: 100%\">\n      <el-table-column prop=\"content\" label=\"题干\" />\n      <el-table-column prop=\"difficulty\" label=\"难度\" />\n      <el-table-column prop=\"tags\" label=\"标签\" />\n      <el-table-column label=\"操作\">\n        <template #default=\"scope\">\n          <el-button @click=\"viewQuestion(scope.row)\">查看</el-button>\n        </template>\n      </el-table-column>\n    </el-table>\n    \n    <el-dialog v-model=\"dialogVisible\" title=\"题目详情\" width=\"50%\">\n      <div v-if=\"selectedQuestion\">\n        <p><strong>题干:</strong> {{ selectedQuestion.content }}</p>\n        <p v-if=\"selectedQuestion.image_url\">\n          <img :src=\"selectedQuestion.image_url\" style=\"max-width: 300px;\" />\n        </p>\n        <p><strong>难度:</strong> {{ selectedQuestion.difficulty }}</p>\n        <p><strong>标签:</strong> {{ selectedQuestion.tags }}</p>\n        <p><strong>解析:</strong> {{ selectedQuestion.explanation }}</p>\n      </div>\n      <template #footer>\n        <el-button @click=\"dialogVisible = false\">关闭</el-button>\n      </template>\n    </el-dialog>\n  </div>\n</template>\n\n<script setup>\nimport { ref, onMounted } from 'vue'\nimport axios from '@/api'\n\nconst questions = ref([])\nconst dialogVisible = ref(false)\nconst selectedQuestion = ref(null)\n\nconst emit = defineEmits(['importExcel'])\n\nonMounted(async () => {\n  try {\n    const response = await axios.get('/questions')\n    questions.value = response.data.items\n  } catch (error) {\n    console.error('获取题库失败:', error)\n  }\n})\n\nconst viewQuestion = (question) => {\n  selectedQuestion.value = question\n  dialogVisible.value = true\n}\n</script>\n\n<style scoped>\n.question-table {\n  margin-top: 20px;\n}\n.actions {\n  margin-bottom: 20px;\n}\n</style>",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/components/ExcelImport.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"excel-import\">\n    <el-card>\n      <h2>题库Excel导入</h2>\n      <div class=\"template-download\">\n        <el-link :href=\"templateUrl\" target=\"_blank\">下载Excel模板</el-link>\n      </div>\n      \n      <el-upload\n        class=\"upload-demo\"\n        :action=\"uploadUrl\"\n        :headers=\"{ Authorization: 'Bearer ' + token }\"\n        :on-success=\"handleSuccess\"\n        :on-error=\"handleError\"\n        :file-list=\"fileList\"\n        accept=\".xlsx, .xls\"\n      >\n        <el-button type=\"primary\">点击上传</el-button>\n        <template #tip>\n          <div class=\"el-upload__tip\">\n            只能上传xlsx/xls文件，且不超过10MB\n          </div>\n        </template>\n      </el-upload>\n      \n      <el-alert\n        v-if=\"message\"\n        :title=\"message\"\n        :type=\"messageType\"\n        show-icon\n        style=\"margin-top: 20px;\"\n      />\n      \n      <div class=\"actions\">\n        <el-button @click=\"$emit('close')\">关闭</el-button>\n      </div>\n    </el-card>\n  </div>\n</template>\n\n<script setup>\nimport { ref } from 'vue'\nimport axios from '@/api'\n\nconst emit = defineEmits(['close'])\n\nconst token = localStorage.getItem('token')\nconst templateUrl = '/api/questions/excel-template'\nconst uploadUrl = '/api/questions/import-excel'\nconst fileList = ref([])\nconst message = ref('')\nconst messageType = ref('success')\n\nconst handleSuccess = (response) => {\n  message.value = response.msg || '导入成功'\n  messageType.value = 'success'\n  fileList.value = []\n}\n\nconst handleError = (error) => {\n  message.value = '导入失败'\n  messageType.value = 'error'\n  console.error('导入错误:', error)\n}\n</script>\n\n<style scoped>\n.excel-import {\n  margin-top: 20px;\n}\n.template-download {\n  margin-bottom: 20px;\n}\n.actions {\n  margin-top: 20px;\n  text-align: right;\n}\n</style>",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/components/HomeworkReview.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"homework-review\">\n    <h2>作业批改</h2>\n    \n    <el-table :data=\"assignments\" style=\"width: 100%\">\n      <el-table-column prop=\"studentName\" label=\"学生\" />\n      <el-table-column prop=\"question\" label=\"题目\" />\n      <el-table-column prop=\"answer\" label=\"学生答案\" />\n      <el-table-column prop=\"ai_explanation\" label=\"AI解析\" />\n      <el-table-column label=\"评分\">\n        <template #default=\"scope\">\n          <el-input-number \n            v-model=\"scope.row.score\" \n            :min=\"0\" \n            :max=\"100\" \n            :precision=\"1\"\n          />\n        </template>\n      </el-table-column>\n      <el-table-column label=\"批语\">\n        <template #default=\"scope\">\n          <el-input v-model=\"scope.row.comment\" />\n        </template>\n      </el-table-column>\n      <el-table-column label=\"操作\">\n        <template #default=\"scope\">\n          <el-button \n            type=\"primary\" \n            @click=\"submitReview(scope.row)\"\n            :disabled=\"scope.row.submitted\"\n          >\n            {{ scope.row.submitted ? '已提交' : '提交' }}\n          </el-button>\n        </template>\n      </el-table-column>\n    </el-table>\n  </div>\n</template>\n\n<script setup>\nimport { ref, onMounted } from 'vue'\nimport axios from '@/api'\n\nconst assignments = ref([])\n\nonMounted(async () => {\n  try {\n    const response = await axios.get('/homework/review-list')\n    assignments.value = response.data.items\n  } catch (error) {\n    console.error('获取作业列表失败:', error)\n  }\n})\n\nconst submitReview = async (assignment) => {\n  try {\n    await axios.post('/homework/review', {\n      id: assignment.id,\n      score: assignment.score,\n      comment: assignment.comment\n    })\n    \n    assignment.submitted = true\n    ElMessage.success('批改成功')\n  } catch (error) {\n    console.error('提交批改失败:', error)\n    ElMessage.error('提交失败')\n  }\n}\n</script>\n\n<style scoped>\n.homework-review {\n  margin-top: 20px;\n}\n</style>",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/api/index.js",
        "language": "javascript",
        "code": "import axios from 'axios'\nimport { ElMessage } from 'element-plus'\n\nconst api = axios.create({\n  baseURL: '/api', // 配置代理\n  timeout: 10000\n})\n\n// 请求拦截器\napi.interceptors.request.use(\n  config => {\n    const token = localStorage.getItem('token')\n    if (token) {\n      config.headers.Authorization = `Bearer ${token}`\n    }\n    return config\n  },\n  error => {\n    return Promise.reject(error)\n  }\n)\n\n// 响应拦截器\napi.interceptors.response.use(\n  response => {\n    return response.data\n  },\n  error => {\n    if (error.response && error.response.status === 401) {\n      localStorage.removeItem('token')\n      localStorage.removeItem('role')\n      window.location.href = '/login'\n      ElMessage.error('登录已过期，请重新登录')\n    }\n    return Promise.reject(error)\n  }\n)\n\nexport default api",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "docker-compose.yml",
        "language": "yaml",
        "code": "version: '3.8'\n\nservices:\n  backend:\n    build: ./backend\n    container_name: edu-ai-backend\n    ports:\n      - \"8000:8000\"\n    environment:\n      - DATABASE_URL=mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db\n      - CELERY_BROKER_URL=redis://redis:6379/0\n    volumes:\n      - /mnt/nas/models:/mnt/nas/models\n    depends_on:\n      - mariadb\n      - redis\n\n  frontend:\n    build: ./frontend\n    container_name: edu-ai-frontend\n    ports:\n      - \"5173:80\"\n    depends_on:\n      - backend\n\n  mariadb:\n    image: mariadb:10.6\n    container_name: edu-ai-mariadb\n    environment:\n      MYSQL_ROOT_PASSWORD: yourpassword\n      MYSQL_DATABASE: edu_ai_db\n    volumes:\n      - /mnt/nas/db:/var/lib/mysql\n    ports:\n      - \"3306:3306\"\n\n  redis:\n    image: redis:6-alpine\n    container_name: edu-ai-redis\n    ports:\n      - \"6379:6379\"\n\n  celery:\n    build: \n      context: ./backend\n      dockerfile: Dockerfile.celery\n    container_name: edu-ai-celery\n    environment:\n      - DATABASE_URL=mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db\n      - CELERY_BROKER_URL=redis://redis:6379/0\n    volumes:\n      - /mnt/nas/models:/mnt/nas/models\n    depends_on:\n      - mariadb\n      - redis",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "k8s/edu-ai-ingress.yaml",
        "language": "yaml",
        "code": "apiVersion: networking.k8s.io/v1\nkind: Ingress\nmetadata:\n  name: edu-ai-ingress\n  annotations:\n    nginx.ingress.kubernetes.io/rewrite-target: /$2\n    nginx.ingress.kubernetes.io/ssl-redirect: \"true\"\n    cert-manager.io/cluster-issuer: \"letsencrypt-prod\"\nspec:\n  tls:\n  - hosts:\n    - ai.yourdomain.com\n    secretName: edu-ai-tls\n  rules:\n  - host: ai.yourdomain.com\n    http:\n      paths:\n      - path: /api(/|$)(.*)\n        pathType: Prefix\n        backend:\n          service:\n            name: edu-ai-backend-service\n            port:\n              number: 8000\n      - path: /()(.*)\n        pathType: Prefix\n        backend:\n          service:\n            name: edu-ai-frontend-service\n            port:\n              number: 80",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "k8s/edu-ai-backend-deployment.yaml",
        "language": "yaml",
        "code": "apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: edu-ai-backend\nspec:\n  replicas: 2\n  selector:\n    matchLabels:\n      app: edu-ai-backend\n  template:\n    metadata:\n      labels:\n        app: edu-ai-backend\n    spec:\n      containers:\n      - name: backend\n        image: yourrepo/edu-ai-backend:latest\n        ports:\n        - containerPort: 8000\n        env:\n        - name: DATABASE_URL\n          value: \"mysql+pymysql://root:yourpassword@mariadb:3306/edu_ai_db\"\n        - name: CELERY_BROKER_URL\n          value: \"redis://redis:6379/0\"\n        volumeMounts:\n        - name: nas-models\n          mountPath: /mnt/nas/models\n      volumes:\n      - name: nas-models\n        persistentVolumeClaim:\n          claimName: nas-models-pvc",
        "source_doc": "docs/教育AI全栈设计方案.md"
      },
      {
        "filename": "frontend/src/App.vue",
        "language": "plaintext",
        "code": "<template>\n  <div id=\"app\">\n    <router-view v-slot=\"{ Component }\">\n      <transition name=\"page-fade\" mode=\"out-in\">\n        <component :is=\"Component\" />\n      </transition>\n    </router-view>\n  </div>\n</template>\n\n<script setup>\n// 引入全局样式\nimport './styles/theme.css'\n</script>\n\n<style>\n#app {\n  font-family: var(--font-family);\n  -webkit-font-smoothing: antialiased;\n  -moz-osx-font-smoothing: grayscale;\n  color: var(--text-primary);\n  background-color: var(--background-color);\n  min-height: 100vh;\n}\n</style>",
        "source_doc": "docs/系统UI设计方案文档.md"
      },
      {
        "filename": "frontend/src/components/CustomNav.vue",
        "language": "plaintext",
        "code": "<template>\n  <nav class=\"custom-nav\">\n    <div class=\"nav-container\">\n      <div class=\"nav-logo\">\n        <img src=\"@/assets/logo.png\" alt=\"Logo\" class=\"logo\" />\n        <span class=\"logo-text\">教育AI题库系统</span>\n      </div>\n      <div class=\"nav-menu\">\n        <div \n          v-for=\"item in menuItems\" \n          :key=\"item.path\" \n          class=\"nav-item\" \n          :class=\"{ active: currentPath === item.path }\"\n          @click=\"navigateTo(item.path)\"\n        >\n          {{ item.title }}\n        </div>\n      </div>\n      <div class=\"nav-user\">\n        <el-dropdown v-if=\"user\" trigger=\"click\">\n          <div class=\"user-info\">\n            <el-avatar :size=\"32\" :src=\"user.avatar || defaultAvatar\" />\n            <span class=\"username\">{{ user.name || user.username }}</span>\n          </div>\n          <template #dropdown>\n            <el-dropdown-menu>\n              <el-dropdown-item @click=\"goToProfile\">个人中心</el-dropdown-item>\n              <el-dropdown-item @click=\"logout\">退出登录</el-dropdown-item>\n            </el-dropdown-menu>\n          </template>\n        </el-dropdown>\n        <el-button v-else type=\"primary\" @click=\"goToLogin\">登录</el-button>\n      </div>\n    </div>\n  </nav>\n</template>\n\n<script setup>\nimport { ref, computed } from 'vue'\nimport { useRouter, useRoute } from 'vue-router'\nimport { useUserStore } from '@/store'\n\nconst router = useRouter()\nconst route = useRoute()\nconst userStore = useUserStore()\n\nconst currentPath = computed(() => route.path)\nconst user = computed(() => userStore.user)\nconst defaultAvatar = 'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'\n\nconst menuItems = [\n  { title: '首页', path: '/' },\n  { title: '题库', path: '/questions' },\n  { title: '作业', path: '/homework' },\n  { title: '关于', path: '/about' }\n]\n\nconst navigateTo = (path) => {\n  router.push(path)\n}\n\nconst goToLogin = () => {\n  router.push('/login')\n}\n\nconst goToProfile = () => {\n  router.push('/profile')\n}\n\nconst logout = () => {\n  userStore.logout()\n  router.push('/login')\n}\n</script>\n\n<style scoped>\n.custom-nav {\n  background: var(--background-white);\n  box-shadow: var(--box-shadow-light);\n  position: sticky;\n  top: 0;\n  z-index: 1000;\n}\n\n.nav-container {\n  max-width: 1200px;\n  margin: 0 auto;\n  display: flex;\n  align-items: center;\n  justify-content: space-between;\n  height: 60px;\n  padding: 0 20px;\n}\n\n.nav-logo {\n  display: flex;\n  align-items: center;\n}\n\n.logo {\n  height: 32px;\n  margin-right: 10px;\n}\n\n.logo-text {\n  font-size: 18px;\n  font-weight: 600;\n  color: var(--primary-color);\n}\n\n.nav-menu {\n  display: flex;\n  height: 100%;\n}\n\n.nav-user {\n  display: flex;\n  align-items: center;\n}\n\n.user-info {\n  display: flex;\n  align-items: center;\n  cursor: pointer;\n}\n\n.username {\n  margin-left: 10px;\n  font-size: 14px;\n  color: var(--text-regular);\n}\n\n@media (max-width: 768px) {\n  .logo-text {\n    display: none;\n  }\n  \n  .nav-menu {\n    display: none;\n  }\n}\n</style>",
        "source_doc": "docs/系统UI设计方案文档.md"
      },
      {
        "filename": "frontend/src/components/CustomDialog.vue",
        "language": "plaintext",
        "code": "<template>\n  <el-dialog\n    v-model=\"visible\"\n    :title=\"title\"\n    :width=\"width\"\n    :before-close=\"handleClose\"\n    class=\"custom-dialog\"\n    :close-on-click-modal=\"false\"\n    destroy-on-close\n  >\n    <div class=\"dialog-content\">\n      <slot></slot>\n    </div>\n    <template #footer>\n      <div class=\"dialog-footer\">\n        <slot name=\"footer\">\n          <el-button @click=\"handleClose\">取消</el-button>\n          <el-button type=\"primary\" @click=\"handleConfirm\">确定</el-button>\n        </slot>\n      </div>\n    </template>\n  </el-dialog>\n</template>\n\n<script setup>\nimport { ref, watch } from 'vue'\n\nconst props = defineProps({\n  modelValue: {\n    type: Boolean,\n    default: false\n  },\n  title: {\n    type: String,\n    default: '提示'\n  },\n  width: {\n    type: String,\n    default: '50%'\n  }\n})\n\nconst emit = defineEmits(['update:modelValue', 'confirm', 'cancel'])\n\nconst visible = ref(props.modelValue)\n\nwatch(() => props.modelValue, (val) => {\n  visible.value = val\n})\n\nwatch(visible, (val) => {\n  emit('update:modelValue', val)\n})\n\nconst handleClose = () => {\n  visible.value = false\n  emit('cancel')\n}\n\nconst handleConfirm = () => {\n  emit('confirm')\n  visible.value = false\n}\n</script>\n\n<style scoped>\n.custom-dialog {\n  border-radius: var(--border-radius-large);\n  overflow: hidden;\n}\n\n.dialog-content {\n  padding: 20px 0;\n}\n\n.dialog-footer {\n  display: flex;\n  justify-content: flex-end;\n  gap: 10px;\n}\n</style>",
        "source_doc": "docs/系统UI设计方案文档.md"
      },
      {
        "filename": "frontend/src/components/CustomTable.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"custom-table-container\">\n    <el-table\n      :data=\"data\"\n      :border=\"border\"\n      :stripe=\"stripe\"\n      :height=\"height\"\n      :max-height=\"maxHeight\"\n      :row-key=\"rowKey\"\n      :tree-props=\"treeProps\"\n      :default-expand-all=\"defaultExpandAll\"\n      :show-summary=\"showSummary\"\n      :sum-text=\"sumText\"\n      :summary-method=\"summaryMethod\"\n      :span-method=\"spanMethod\"\n      :select-on-indeterminate=\"selectOnIndeterminate\"\n      :indent=\"indent\"\n      :lazy=\"lazy\"\n      :load=\"load\"\n      @select=\"handleSelect\"\n      @select-all=\"handleSelectAll\"\n      @selection-change=\"handleSelectionChange\"\n      @cell-mouse-enter=\"handleCellMouseEnter\"\n      @cell-mouse-leave=\"handleCellMouseLeave\"\n      @cell-click=\"handleCellClick\"\n      @cell-dblclick=\"handleCellDblclick\"\n      @row-click=\"handleRowClick\"\n      @row-contextmenu=\"handleRowContextmenu\"\n      @row-dblclick=\"handleRowDblclick\"\n      @header-click=\"handleHeaderClick\"\n      @header-contextmenu=\"handleHeaderContextmenu\"\n      @sort-change=\"handleSortChange\"\n      @filter-change=\"handleFilterChange\"\n      @current-change=\"handleCurrentChange\"\n      @header-dragend=\"handleHeaderDragend\"\n      @expand-change=\"handleExpandChange\"\n      class=\"custom-table\"\n    >\n      <slot></slot>\n    </el-table>\n    \n    <div v-if=\"pagination\" class=\"table-pagination\">\n      <el-pagination\n        v-model:current-page=\"currentPage\"\n        v-model:page-size=\"pageSize\"\n        :page-sizes=\"pageSizes\"\n        :total=\"total\"\n        :layout=\"layout\"\n        :small=\"small\"\n        :background=\"background\"\n        @size-change=\"handleSizeChange\"\n        @current-change=\"handleCurrentChange\"\n      />\n    </div>\n  </div>\n</template>\n\n<script setup>\nimport { ref } from 'vue'\n\nconst props = defineProps({\n  data: {\n    type: Array,\n    default: () => []\n  },\n  border: {\n    type: Boolean,\n    default: true\n  },\n  stripe: {\n    type: Boolean,\n    default: true\n  },\n  height: [String, Number],\n  maxHeight: [String, Number],\n  rowKey: [String, Function],\n  treeProps: {\n    type: Object,\n    default: () => ({})\n  },\n  defaultExpandAll: {\n    type: Boolean,\n    default: false\n  },\n  showSummary: {\n    type: Boolean,\n    default: false\n  },\n  sumText: {\n    type: String,\n    default: '合计'\n  },\n  summaryMethod: Function,\n  spanMethod: Function,\n  selectOnIndeterminate: {\n    type: Boolean,\n    default: true\n  },\n  indent: {\n    type: Number,\n    default: 16\n  },\n  lazy: {\n    type: Boolean,\n    default: false\n  },\n  load: Function,\n  pagination: {\n    type: Boolean,\n    default: true\n  },\n  total: {\n    type: Number,\n    default: 0\n  },\n  pageSizes: {\n    type: Array,\n    default: () => [10, 20, 50, 100]\n  },\n  layout: {\n    type: String,\n    default: 'total, sizes, prev, pager, next, jumper'\n  },\n  small: {\n    type: Boolean,\n    default: false\n  },\n  background: {\n    type: Boolean,\n    default: true\n  }\n})\n\nconst emit = defineEmits([\n  'select',\n  'select-all',\n  'selection-change',\n  'cell-mouse-enter',\n  'cell-mouse-leave',\n  'cell-click',\n  'cell-dblclick',\n  'row-click',\n  'row-contextmenu',\n  'row-dblclick',\n  'header-click',\n  'header-contextmenu',\n  'sort-change',\n  'filter-change',\n  'current-change',\n  'header-dragend',\n  'expand-change',\n  'size-change',\n  'update:currentPage',\n  'update:pageSize'\n])\n\nconst currentPage = ref(1)\nconst pageSize = ref(10)\n\nconst handleSelect = (selection, row) => {\n  emit('select', selection, row)\n}\n\nconst handleSelectAll = (selection) => {\n  emit('select-all', selection)\n}\n\nconst handleSelectionChange = (selection) => {\n  emit('selection-change', selection)\n}\n\nconst handleCellMouseEnter = (row, column, cell, event) => {\n  emit('cell-mouse-enter', row, column, cell, event)\n}\n\nconst handleCellMouseLeave = (row, column, cell, event) => {\n  emit('cell-mouse-leave', row, column, cell, event)\n}\n\nconst handleCellClick = (row, column, cell, event) => {\n  emit('cell-click', row, column, cell, event)\n}\n\nconst handleCellDblclick = (row, column, cell, event) => {\n  emit('cell-dblclick', row, column, cell, event)\n}\n\nconst handleRowClick = (row, column, event) => {\n  emit('row-click', row, column, event)\n}\n\nconst handleRowContextmenu = (row, column, event) => {\n  emit('row-contextmenu', row, column, event)\n}\n\nconst handleRowDblclick = (row, column, event) => {\n  emit('row-dblclick', row, column, event)\n}\n\nconst handleHeaderClick = (column, event) => {\n  emit('header-click', column, event)\n}\n\nconst handleHeaderContextmenu = (column, event) => {\n  emit('header-contextmenu', column, event)\n}\n\nconst handleSortChange = (column) => {\n  emit('sort-change', column)\n}\n\nconst handleFilterChange = (filters) => {\n  emit('filter-change', filters)\n}\n\nconst handleCurrentChange = (val) => {\n  emit('current-change', val)\n  emit('update:currentPage', val)\n}\n\nconst handleHeaderDragend = (newWidth, oldWidth, column, event) => {\n  emit('header-dragend', newWidth, oldWidth, column, event)\n}\n\nconst handleExpandChange = (row, expanded) => {\n  emit('expand-change', row, expanded)\n}\n\nconst handleSizeChange = (val) => {\n  emit('size-change', val)\n  emit('update:pageSize', val)\n  currentPage.value = 1\n  emit('update:currentPage', 1)\n}\n</script>\n\n<style scoped>\n.custom-table-container {\n  background: var(--background-white);\n  border-radius: var(--border-radius-large);\n  overflow: hidden;\n  box-shadow: var(--box-shadow-light);\n  transition: var(--transition-all);\n}\n\n.custom-table-container:hover {\n  box-shadow: var(--box-shadow-base);\n}\n\n.custom-table {\n  width: 100%;\n}\n\n.custom-table .el-table__header-wrapper {\n  background-color: var(--primary-light);\n}\n\n.custom-table .el-table__header th {\n  background-color: var(--primary-light);\n  color: var(--primary-dark);\n  font-weight: 600;\n  border-bottom: 2px solid var(--primary-color);\n}\n\n.custom-table .el-table__body tr:hover > td {\n  background-color: var(--primary-light);\n}\n\n.table-pagination {\n  padding: 15px;\n  display: flex;\n  justify-content: flex-end;\n}\n</style>",
        "source_doc": "docs/系统UI设计方案文档.md"
      },
      {
        "filename": "frontend/src/components/CustomButton.vue",
        "language": "plaintext",
        "code": "<template>\n  <el-button\n    :type=\"type\"\n    :size=\"size\"\n    :plain=\"plain\"\n    :round=\"round\"\n    :circle=\"circle\"\n    :loading=\"loading\"\n    :disabled=\"disabled\"\n    :icon=\"icon\"\n    :autofocus=\"autofocus\"\n    :native-type=\"nativeType\"\n    :loading-icon=\"loadingIcon\"\n    :use-throttle=\"useThrottle\"\n    :throttle-duration=\"throttleDuration\"\n    @click=\"handleClick\"\n    class=\"custom-button\"\n  >\n    <slot></slot>\n  </el-button>\n</template>\n\n<script setup>\nimport { computed } from 'vue'\n\nconst props = defineProps({\n  type: {\n    type: String,\n    default: 'default'\n  },\n  size: {\n    type: String,\n    default: 'default'\n  },\n  plain: {\n    type: Boolean,\n    default: false\n  },\n  round: {\n    type: Boolean,\n    default: false\n  },\n  circle: {\n    type: Boolean,\n    default: false\n  },\n  loading: {\n    type: Boolean,\n    default: false\n  },\n  disabled: {\n    type: Boolean,\n    default: false\n  },\n  icon: {\n    type: String,\n    default: ''\n  },\n  autofocus: {\n    type: Boolean,\n    default: false\n  },\n  nativeType: {\n    type: String,\n    default: 'button'\n  },\n  loadingIcon: {\n    type: String,\n    default: ''\n  },\n  useThrottle: {\n    type: Boolean,\n    default: true\n  },\n  throttleDuration: {\n    type: Number,\n    default: 300\n  }\n})\n\nconst emit = defineEmits(['click'])\n\nconst handleClick = (event) => {\n  emit('click', event)\n}\n</script>\n\n<style scoped>\n.custom-button {\n  transition: var(--transition-all);\n  border-radius: var(--border-radius-base);\n  font-weight: 500;\n  box-shadow: 0 2px 0 rgba(0, 0, 0, 0.015);\n}\n\n.custom-button:hover {\n  transform: translateY(-2px);\n  box-shadow: var(--box-shadow-base);\n}\n\n.custom-button:active {\n  transform: translateY(0);\n  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.015);\n}\n\n.custom-button--primary {\n  background-color: var(--primary-color);\n  border-color: var(--primary-color);\n}\n\n.custom-button--primary:hover {\n  background-color: var(--primary-dark);\n  border-color: var(--primary-dark);\n}\n\n.custom-button--success {\n  background-color: var(--success-color);\n  border-color: var(--success-color);\n}\n\n.custom-button--success:hover {\n  background-color: var(--success-dark);\n  border-color: var(--success-dark);\n}\n\n.custom-button--warning {\n  background-color: var(--warning-color);\n  border-color: var(--warning-color);\n}\n\n.custom-button--warning:hover {\n  background-color: var(--warning-dark);\n  border-color: var(--warning-dark);\n}\n\n.custom-button--danger {\n  background-color: var(--danger-color);\n  border-color: var(--danger-color);\n}\n\n.custom-button--danger:hover {\n  background-color: var(--danger-dark);\n  border-color: var(--danger-dark);\n}\n\n.custom-button--info {\n  background-color: var(--info-color);\n  border-color: var(--info-color);\n}\n\n.custom-button--info:hover {\n  background-color: var(--info-dark);\n  border-color: var(--info-dark);\n}\n</style>",
        "source_doc": "docs/系统UI设计方案文档.md"
      },
      {
        "filename": "frontend/src/components/CustomCard.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"custom-card\" :class=\"`custom-card-${variant}`\">\n    <div v-if=\"$slots.header\" class=\"card-header\">\n      <slot name=\"header\"></slot>\n    </div>\n    <div class=\"card-content\">\n      <slot></slot>\n    </div>\n    <div v-if=\"$slots.footer\" class=\"card-footer\">\n      <slot name=\"footer\"></slot>\n    </div>\n  </div>\n</template>\n\n<script setup>\nconst props = defineProps({\n  variant: {\n    type: String,\n    default: 'default',\n    validator: (value) => ['default', 'primary', 'success', 'warning', 'danger', 'info'].includes(value)\n  }\n})\n</script>\n\n<style scoped>\n.custom-card {\n  background: var(--background-white);\n  border-radius: var(--border-radius-large);\n  box-shadow: var(--box-shadow-light);\n  padding: 20px;\n  margin-bottom: 20px;\n  transition: var(--transition-all);\n  border: 1px solid var(--border-light);\n}\n\n.custom-card:hover {\n  box-shadow: var(--box-shadow-base);\n  transform: translateY(-2px);\n}\n\n.custom-card-primary {\n  border-left: 4px solid var(--primary-color);\n}\n\n.custom-card-success {\n  border-left: 4px solid var(--success-color);\n}\n\n.custom-card-warning {\n  border-left: 4px solid var(--warning-color);\n}\n\n.custom-card-danger {\n  border-left: 4px solid var(--danger-color);\n}\n\n.custom-card-info {\n  border-left: 4px solid var(--info-color);\n}\n\n.card-header {\n  padding-bottom: 15px;\n  border-bottom: 1px solid var(--border-light);\n  margin-bottom: 15px;\n}\n\n.card-footer {\n  padding-top: 15px;\n  border-top: 1px solid var(--border-light);\n  margin-top: 15px;\n}\n</style>",
        "source_doc": "docs/系统UI设计方案文档.md"
      },
      {
        "filename": "更新QuestionTable.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"question-table\">\n    <CustomCard>\n      <template #header>\n        <div class=\"card-header-content\">\n          <h2>题库管理</h2>\n          <CustomButton type=\"primary\" @click=\"$emit('importExcel')\">\n            <el-icon><Upload /></el-icon>\n            Excel导入\n          </CustomButton>\n        </div>\n      </template>\n      \n      <CustomTable\n        :data=\"questions\"\n        border\n        stripe\n        @row-click=\"viewQuestion\"\n      >\n        <el-table-column prop=\"content\" label=\"题干\" min-width=\"200\" />\n        <el-table-column prop=\"difficulty\" label=\"难度\" width=\"100\" />\n        <el-table-column prop=\"tags\" label=\"标签\" width=\"150\" />\n        <el-table-column label=\"操作\" width=\"100\">\n          <template #default=\"scope\">\n            <CustomButton type=\"primary\" size=\"small\" @click.stop=\"viewQuestion(scope.row)\">\n              查看\n            </CustomButton>\n          </template>\n        </el-table-column>\n      </CustomTable>\n    </CustomCard>\n    \n    <CustomDialog\n      v-model=\"dialogVisible\"\n      title=\"题目详情\"\n      width=\"60%\"\n    >\n      <div v-if=\"selectedQuestion\" class=\"question-detail\">\n        <h3>题干</h3>\n        <p>{{ selectedQuestion.content }}</p>\n        \n        <div v-if=\"selectedQuestion.image_url\" class=\"question-image\">\n          <h3>图片</h3>\n          <el-image \n            :src=\"selectedQuestion.image_url\" \n            fit=\"contain\"\n            style=\"max-width: 100%; max-height: 300px;\"\n          />\n        </div>\n        \n        <div class=\"question-meta\">\n          <div class=\"meta-item\">\n            <span class=\"label\">难度:</span>\n            <span class=\"value\">{{ selectedQuestion.difficulty }}</span>\n          </div>\n          <div class=\"meta-item\">\n            <span class=\"label\">标签:</span>\n            <span class=\"value\">{{ selectedQuestion.tags }}</span>\n          </div>\n        </div>\n        \n        <div class=\"question-explanation\">\n          <h3>解析</h3>\n          <p>{{ selectedQuestion.explanation }}</p>\n        </div>\n      </div>\n      \n      <template #footer>\n        <CustomButton @click=\"dialogVisible = false\">关闭</CustomButton>\n      </template>\n    </CustomDialog>\n  </div>\n</template>\n\n<script setup>\nimport { ref, onMounted } from 'vue'\nimport axios from '@/api'\nimport CustomCard from './CustomCard.vue'\nimport CustomTable from './CustomTable.vue'\nimport CustomButton from './CustomButton.vue'\nimport CustomDialog from './CustomDialog.vue'\nimport { Upload } from '@element-plus/icons-vue'\n\nconst questions = ref([])\nconst dialogVisible = ref(false)\nconst selectedQuestion = ref(null)\n\nconst emit = defineEmits(['importExcel'])\n\nonMounted(async () => {\n  try {\n    const response = await axios.get('/questions')\n    questions.value = response.data.items\n  } catch (error) {\n    console.error('获取题库失败:', error)\n  }\n})\n\nconst viewQuestion = (question) => {\n  selectedQuestion.value = question\n  dialogVisible.value = true\n}\n</script>\n\n<style scoped>\n.question-table {\n  margin-top: 20px;\n}\n\n.card-header-content {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}\n\n.card-header-content h2 {\n  margin: 0;\n  color: var(--text-primary);\n}\n\n.question-detail h3 {\n  margin-top: 20px;\n  margin-bottom: 10px;\n  color: var(--text-primary);\n  font-size: 16px;\n  font-weight: 600;\n}\n\n.question-detail h3:first-child {\n  margin-top: 0;\n}\n\n.question-image {\n  margin-top: 20px;\n}\n\n.question-meta {\n  display: flex;\n  flex-wrap: wrap;\n  margin-top: 20px;\n}\n\n.meta-item {\n  margin-right: 30px;\n  margin-bottom: 10px;\n}\n\n.meta-item .label {\n  font-weight: 600;\n  margin-right: 5px;\n  color: var(--text-regular);\n}\n\n.meta-item .value {\n  color: var(--text-primary);\n}\n\n.question-explanation {\n  margin-top: 20px;\n}\n</style>",
        "source_doc": "docs/系统UI设计方案文档.md"
      },
      {
        "filename": "10.更新HomeworkReview.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"homework-review\">\n    <CustomCard>\n      <template #header>\n        <h2>作业批改</h2>\n      </template>\n      \n      <CustomTable\n        :data=\"assignments\"\n        border\n        stripe\n      >\n        <el-table-column prop=\"studentName\" label=\"学生\" width=\"120\" />\n        <el-table-column prop=\"question\" label=\"题目\" min-width=\"200\" />\n        <el-table-column prop=\"answer\" label=\"学生答案\" min-width=\"200\" />\n        <el-table-column prop=\"ai_explanation\" label=\"AI解析\" min-width=\"200\" />\n        <el-table-column label=\"评分\" width=\"150\">\n          <template #default=\"scope\">\n            <el-input-number \n              v-model=\"scope.row.score\" \n              :min=\"0\" \n              :max=\"100\" \n              :precision=\"1\"\n              size=\"small\"\n            />\n          </template>\n        </el-table-column>\n        <el-table-column label=\"批语\" width=\"200\">\n          <template #default=\"scope\">\n            <el-input v-model=\"scope.row.comment\" size=\"small\" />\n          </template>\n        </el-table-column>\n        <el-table-column label=\"操作\" width=\"120\">\n          <template #default=\"scope\">\n            <CustomButton \n              type=\"primary\" \n              size=\"small\" \n              @click=\"submitReview(scope.row)\"\n              :disabled=\"scope.row.submitted\"\n            >\n              {{ scope.row.submitted ? '已提交' : '提交' }}\n            </CustomButton>\n          </template>\n        </el-table-column>\n      </CustomTable>\n    </CustomCard>\n  </div>\n</template>\n\n<script setup>\nimport { ref, onMounted } from 'vue'\nimport axios from '@/api'\nimport { ElMessage } from 'element-plus'\nimport CustomCard from './CustomCard.vue'\nimport CustomTable from './CustomTable.vue'\nimport CustomButton from './CustomButton.vue'\n\nconst assignments = ref([])\n\nonMounted(async () => {\n  try {\n    const response = await axios.get('/homework/review-list')\n    assignments.value = response.data.items\n  } catch (error) {\n    console.error('获取作业列表失败:', error)\n  }\n})\n\nconst submitReview = async (assignment) => {\n  try {\n    await axios.post('/homework/review', {\n      id: assignment.id,\n      score: assignment.score,\n      comment: assignment.comment\n    })\n    \n    assignment.submitted = true\n    ElMessage.success('批改成功')\n  } catch (error) {\n    console.error('提交批改失败:', error)\n    ElMessage.error('提交失败')\n  }\n}\n</script>\n\n<style scoped>\n.homework-review {\n  margin-top: 20px;\n}\n</style>",
        "source_doc": "docs/系统UI设计方案文档.md"
      },
      {
        "filename": "11.更新ExcelImport.vue",
        "language": "plaintext",
        "code": "<template>\n  <CustomDialog\n    v-model=\"visible\"\n    title=\"题库Excel导入\"\n    width=\"50%\"\n    @close=\"$emit('close')\"\n  >\n    <div class=\"excel-import-content\">\n      <div class=\"template-download\">\n        <CustomButton type=\"primary\" @click=\"downloadTemplate\">\n          <el-icon><Download /></el-icon>\n          下载Excel模板\n        </CustomButton>\n      </div>\n      \n      <div class=\"upload-section\">\n        <el-upload\n          class=\"upload-demo\"\n          :action=\"uploadUrl\"\n          :headers=\"{ Authorization: 'Bearer ' + token }\"\n          :on-success=\"handleSuccess\"\n          :on-error=\"handleError\"\n          :on-progress=\"handleProgress\"\n          :file-list=\"fileList\"\n          :limit=\"1\"\n          accept=\".xlsx, .xls\"\n          :auto-upload=\"false\"\n          ref=\"uploadRef\"\n        >\n          <template #trigger>\n            <CustomButton type=\"primary\">选择文件</CustomButton>\n          </template>\n          <CustomButton \n            type=\"success\" \n            class=\"upload-btn\"\n            @click=\"submitUpload\"\n            :disabled=\"fileList.length === 0\"\n          >\n            上传\n          </CustomButton>\n          <template #tip>\n            <div class=\"el-upload__tip\">\n              只能上传xlsx/xls文件，且不超过10MB\n            </div>\n          </template>\n        </el-upload>\n      </div>\n      \n      <div v-if=\"uploading\" class=\"upload-progress\">\n        <el-progress :percentage=\"uploadPercentage\" :status=\"uploadStatus\" />\n      </div>\n      \n      <el-alert\n        v-if=\"message\"\n        :title=\"message\"\n        :type=\"messageType\"\n        show-icon\n        :closable=\"false\"\n        style=\"margin-top: 20px;\"\n      />\n    </div>\n    \n    <template #footer>\n      <CustomButton @click=\"$emit('close')\">关闭</CustomButton>\n    </template>\n  </CustomDialog>\n</template>\n\n<script setup>\nimport { ref, computed } from 'vue'\nimport axios from '@/api'\nimport { Download } from '@element-plus/icons-vue'\nimport CustomButton from './CustomButton.vue'\nimport CustomDialog from './CustomDialog.vue'\n\nconst props = defineProps({\n  modelValue: {\n    type: Boolean,\n    default: false\n  }\n})\n\nconst emit = defineEmits(['update:modelValue', 'close'])\n\nconst visible = computed({\n  get: () => props.modelValue,\n  set: (val) => emit('update:modelValue', val)\n})\n\nconst token = localStorage.getItem('token')\nconst templateUrl = '/api/questions/excel-template'\nconst uploadUrl = '/api/questions/import-excel'\nconst uploadRef = ref()\nconst fileList = ref([])\nconst uploading = ref(false)\nconst uploadPercentage = ref(0)\nconst uploadStatus = ref('')\nconst message = ref('')\nconst messageType = ref('success')\n\nconst downloadTemplate = () => {\n  window.open(templateUrl)\n}\n\nconst submitUpload = () => {\n  uploadRef.value.submit()\n}\n\nconst handleSuccess = (response) => {\n  uploading.value = false\n  message.value = response.msg || '导入成功'\n  messageType.value = 'success'\n  fileList.value = []\n  uploadPercentage.value = 100\n  uploadStatus.value = 'success'\n}\n\nconst handleError = (error) => {\n  uploading.value = false\n  message.value = '导入失败'\n  messageType.value = 'error'\n  uploadPercentage.value = 0\n  uploadStatus.value = 'exception'\n  console.error('导入错误:', error)\n}\n\nconst handleProgress = (event) => {\n  uploading.value = true\n  uploadPercentage.value = Math.floor(event.percent)\n  uploadStatus.value = ''\n}\n</script>\n\n<style scoped>\n.excel-import-content {\n  padding: 10px 0;\n}\n\n.template-download {\n  margin-bottom: 20px;\n}\n\n.upload-section {\n  margin-bottom: 20px;\n}\n\n.upload-btn {\n  margin-left: 10px;\n}\n\n.upload-progress {\n  margin-top: 20px;\n}\n</style>",
        "source_doc": "docs/系统UI设计方案文档.md"
      },
      {
        "filename": "12.更新TeacherDashboard.vue",
        "language": "plaintext",
        "code": "<template>\n  <div class=\"teacher-dashboard\">\n    <CustomNav />\n    \n    <div class=\"dashboard-container\">\n      <CustomCard>\n        <template #header>\n          <h2>教师控制台</h2>\n        </template>\n        \n        <el-tabs v-model=\"activeTab\" class=\"dashboard-tabs\">\n          <el-tab-pane label=\"题库管理\" name=\"questions\">\n            <QuestionTable @importExcel=\"showImport = true\" />\n            <ExcelImport v-if=\"showImport\" v-model=\"showImport\" @close=\"showImport = false\" />\n          </el-tab-pane>\n          <el-tab-pane label=\"作业管理\" name=\"homework\">\n            <HomeworkList />\n          </el-tab-pane>\n          <el-tab-pane label=\"作业批改\" name=\"review\">\n            <HomeworkReview />\n          </el-tab-pane>\n        </el-tabs>\n      </CustomCard>\n    </div>\n  </div>\n</template>\n\n<script setup>\nimport { ref } from 'vue'\nimport CustomNav from '@/components/CustomNav.vue'\nimport CustomCard from '@/components/CustomCard.vue'\nimport QuestionTable from '@/components/QuestionTable.vue'\nimport ExcelImport from '@/components/ExcelImport.vue'\nimport HomeworkList from '@/components/HomeworkList.vue'\nimport HomeworkReview from '@/components/HomeworkReview.vue'\n\nconst activeTab = ref('questions')\nconst showImport = ref(false)\n</script>\n\n<style scoped>\n.teacher-dashboard {\n  min-height: 100vh;\n  background-color: var(--background-color);\n}\n\n.dashboard-container {\n  max-width: 1200px;\n  margin: 0 auto;\n  padding: 20px;\n}\n\n.dashboard-tabs {\n  margin-top: 20px;\n}\n</style>",
        "source_doc": "docs/系统UI设计方案文档.md"
      },
      {
        "filename": "frontend/src/router/index.js",
        "language": "plaintext",
        "code": "import { createRouter, createWebHistory } from 'vue-router'\nimport Home from '../views/Home.vue'\nimport Login from '../views/Login.vue'\nimport StudentDashboard from '../views/StudentDashboard.vue'\nimport TeacherDashboard from '../views/TeacherDashboard.vue'\nimport AdminPanel from '../views/AdminPanel.vue'\nimport { useUserStore } from '@/store'\n\nconst routes = [\n  { \n    path: '/', \n    component: Home,\n    meta: { title: '首页' }\n  },\n  { \n    path: '/login', \n    component: Login,\n    meta: { title: '登录' }\n  },\n  { \n    path: '/student', \n    component: StudentDashboard, \n    meta: { \n      requiresAuth: true, \n      role: 'student',\n      title: '学生控制台'\n    } \n  },\n  { \n    path: '/teacher', \n    component: TeacherDashboard, \n    meta: { \n      requiresAuth: true, \n      role: 'teacher',\n      title: '教师控制台'\n    } \n  },\n  { \n    path: '/admin', \n    component: AdminPanel, \n    meta: { \n      requiresAuth: true, \n      role: 'admin',\n      title: '管理员控制台'\n    } \n  }\n]\n\nconst router = createRouter({\n  history: createWebHistory(),\n  routes,\n  scrollBehavior(to, from, savedPosition) {\n    if (savedPosition) {\n      return savedPosition\n    } else {\n      return { top: 0 }\n    }\n  }\n})\n\n// 路由守卫\nrouter.beforeEach((to, from, next) => {\n  const userStore = useUserStore()\n  const token = localStorage.getItem('token')\n  const role = localStorage.getItem('role')\n  \n  // 设置页面标题\n  document.title = to.meta.title ? `${to.meta.title} - 教育AI题库系统` : '教育AI题库系统'\n  \n  if (to.meta.requiresAuth) {\n    if (!token) {\n      next('/login')\n    } else if (to.meta.role && to.meta.role !== role) {\n      next('/login')\n    } else {\n      next()\n    }\n  } else {\n    next()\n  }\n})\n\nexport default router",
        "source_doc": "docs/系统UI设计方案文档.md"
      },
      {
        "filename": "frontend/src/store/index.js",
        "language": "plaintext",
        "code": "import { createPinia, defineStore } from 'pinia'\nimport axios from '@/api'\n\nconst pinia = createPinia()\n\nexport const useUserStore = defineStore('user', {\n  state: () => ({\n    user: null,\n    token: localStorage.getItem('token') || '',\n    role: localStorage.getItem('role') || ''\n  }),\n  \n  getters: {\n    isLoggedIn: (state) => !!state.token,\n    isAdmin: (state) => state.role === 'admin',\n    isTeacher: (state) => state.role === 'teacher',\n    isStudent: (state) => state.role === 'student'\n  },\n  \n  actions: {\n    async login(username, password) {\n      try {\n        const response = await axios.post('/auth/login', { username, password })\n        const { token, role } = response\n        \n        this.token = token\n        this.role = role\n        \n        localStorage.setItem('token', token)\n        localStorage.setItem('role', role)\n        \n        // 获取用户信息\n        await this.fetchUserInfo()\n        \n        return true\n      } catch (error) {\n        console.error('登录失败:', error)\n        return false\n      }\n    },\n    \n    async fetchUserInfo() {\n      try {\n        const response = await axios.get('/users/me')\n        this.user = response\n      } catch (error) {\n        console.error('获取用户信息失败:', error)\n      }\n    },\n    \n    logout() {\n      this.user = null\n      this.token = ''\n      this.role = ''\n      \n      localStorage.removeItem('token')\n      localStorage.removeItem('role')\n    }\n  }\n})\n\nexport default pinia",
        "source_doc": "docs/系统UI设计方案文档.md"
      },
      {
        "filename": "frontend/src/main.js",
        "language": "plaintext",
        "code": "import { createApp } from 'vue'\nimport ElementPlus from 'element-plus'\nimport 'element-plus/dist/index.css'\nimport * as ElementPlusIconsVue from '@element-plus/icons-vue'\nimport { createPinia } from 'pinia'\nimport pinia from './store'\nimport App from './App.vue'\nimport router from './router'\n\nconst app = createApp(App)\n\n// 注册所有图标\nfor (const [key, component] of Object.entries(ElementPlusIconsVue)) {\n  app.component(key, component)\n}\n\napp.use(ElementPlus)\napp.use(createPinia())\napp.use(pinia)\napp.use(router)\n\napp.mount('#app')",
        "source_doc": "docs/系统UI设计方案文档.md"
      },
      {
        "filename": "frontend/vite.config.js",
        "language": "plaintext",
        "code": "import { defineConfig } from 'vite'\nimport vue from '@vitejs/plugin-vue'\nimport { resolve } from 'path'\n\n// https://vitejs.dev/config/\nexport default defineConfig({\n  plugins: [vue()],\n  resolve: {\n    alias: {\n      '@': resolve(__dirname, 'src')\n    }\n  },\n  server: {\n    port: 5173,\n    proxy: {\n      '/api': {\n        target: 'http://localhost:8000',\n        changeOrigin: true,\n        rewrite: (path) => path.replace(/^\\/api/, '')\n      }\n    }\n  },\n  build: {\n    outDir: 'dist',\n    assetsDir: 'assets',\n    sourcemap: false,\n    chunkSizeWarningLimit: 1500,\n    rollupOptions: {\n      output: {\n        manualChunks(id) {\n          if (id.includes('node_modules')) {\n            return 'vendor'\n          }\n        }\n      }\n    }\n  }\n})",
        "source_doc": "docs/系统UI设计方案文档.md"
      },
      {
        "filename": "frontend/package.json",
        "language": "plaintext",
        "code": "{\n  \"name\": \"edu-ai-frontend\",\n  \"private\": true,\n  \"version\": \"0.0.0\",\n  \"type\": \"module\",\n  \"scripts\": {\n    \"dev\": \"vite\",\n    \"build\": \"vite build\",\n    \"preview\": \"vite preview\",\n    \"lint\": \"eslint . --ext vue,js,jsx,cjs,mjs,ts,tsx,cts,mts --fix --ignore-path .gitignore\"\n  },\n  \"dependencies\": {\n    \"@element-plus/icons-vue\": \"^2.1.0\",\n    \"axios\": \"^1.4.0\",\n    \"element-plus\": \"^2.3.8\",\n    \"pinia\": \"^2.1.4\",\n    \"vue\": \"^3.3.4\",\n    \"vue-router\": \"^4.2.4\"\n  },\n  \"devDependencies\": {\n    \"@rushstack/eslint-patch\": \"^1.3.2\",\n    \"@vitejs/plugin-vue\": \"^4.2.3\",\n    \"@vue/eslint-config-prettier\": \"^8.0.0\",\n    \"eslint\": \"^8.45.0\",\n    \"eslint-plugin-vue\": \"^9.15.1\",\n    \"prettier\": \"^3.0.0\",\n    \"vite\": \"^4.4.5\"\n  }\n}",
        "source_doc": "docs/系统UI设计方案文档.md"
      }
    ],
    "file_references": [
      "/app/backend/main.py",
      "/docs/教育AI全栈设计方案.md",
      "k8s/frontend-deployment.yaml",
      "/path/to/backup-db.sh",
      "/App.vue",
      "frontend/src/components/HomeworkReview.vue",
      "/backup-models.sh",
      "/components/HomeworkList.vue",
      "scripts/cleanup_generated_files.py",
      "/docs/教育AI题库系统文档.md",
      "frontend/src/views/TeacherDashboard.vue",
      "scripts/sync_md_code_by_comment.py",
      "infra/k8s/backend-deployment_2.yaml",
      "frontend/src/components/QuestionTable.vue",
      "k8s/network-policy.yaml",
      "backend/models.py",
      "backend/auth.py",
      "frontend/src/components/CustomTable.vue",
      "/views/Login.vue",
      "/views/StudentDashboard.vue",
      "infra/k8s/frontend-deployment.yaml",
      "frontend/src/components/CustomButton.vue",
      "k8s/backend-deployment.yaml",
      "k8s/tls-secret.yaml",
      "frontend/src/components/CustomCard.vue",
      "frontend/package.js",
      "k8s/mariadb-configmap_2.yaml",
      "/backup-db.sh",
      "scripts/auto_review_md_vs_code.py",
      "/docs/系统UI设计方案文档.md",
      "详细表结构请参考backend/models.py",
      "/components/CustomCard.vue",
      "frontend/src/components/CustomNav.vue",
      "/CustomDialog.vue",
      "后端/database.py",
      "/CustomButton.vue",
      "backend/main.py",
      "scripts/sync_md_code_autoext.py",
      "scripts/split_md_code_advanced.py",
      "/restore-db.sh",
      "docs/系统UI设计方案文档.md",
      "/CustomTable.vue",
      "k8s/ingress_2.yaml",
      "infra/k8s/mariadb-configmap.yaml",
      "infra/k8s/network-policy.yaml",
      "k8s/redis-deployment.yaml",
      "k8s/mariadb-configmap.yaml",
      "docs/教育AI全栈设计方案.md",
      "src=\"https://cdn.example.com/js/app.js",
      "infra/k8s/tls-secret.yaml",
      "frontend/src/store/index.js",
      "frontend/src/App.vue",
      "infra/k8s/mariadb-configmap_2.yaml",
      "/rollback.sh",
      "scripts/repo_scanner.py",
      "k8s/edu-ai-backend-deployment.yaml",
      "scripts/md_code_progress_report.py",
      "k8s/backend-deployment_2.yaml",
      "/components/ExcelImport.vue",
      "k8s/rename_yaml_by_content.py",
      "backend/database.py",
      "infra/k8s/redis-deployment.yaml",
      "backend/utils/cache.py",
      "backend/utils/sanitizer.py",
      "scripts/sync_md_code.py",
      "/views/TeacherDashboard.vue",
      "/components/HomeworkReview.vue",
      "/components/QuestionTable.vue",
      "/mnt/nas/backups/edu_ai_db_20231001_020000.sql",
      "github/workflows/auto-review.yml",
      "k8s/backend-deployment_3.yaml",
      "k8s/edu-ai-ingress.yaml",
      "backend/controllers/question.py",
      "BACKUP_DIR/edu_ai_db_$DATE.sql",
      "backend/controllers/ai.py",
      "k8s/ingress.yaml",
      "frontend/vite.config.js",
      "frontend/src/components/ExcelImport.vue",
      "infra/k8s/backend-deployment_3.yaml",
      "infra/k8s/rename_yaml_by_content.py",
      "frontend/src/main.js",
      "/CustomCard.vue",
      "k8s/redis-persistent.yaml",
      "frontend/src/api/index.js",
      "修改backend/database.py",
      "/views/Home.vue",
      "media_type=\"application/vnd.openxmlformats-officedocument.spreadsheetml.sh",
      "backend/celery_worker.py",
      "docs/教育AI题库系统文档.md",
      "frontend/src/router/index.js",
      "frontend/src/components/CustomDialog.vue",
      "/views/AdminPanel.vue",
      "infra/k8s/ingress_2.yaml",
      "scripts/split_md_code_autosave.py",
      "infra/k8s/redis-persistent.yaml",
      "/components/CustomNav.vue",
      "/path/to/backup-models.sh",
      "infra/k8s/backend-deployment.yaml",
      "infra/k8s/ingress.yaml"
    ],
    "missing_files": [],
    "doc_summary": {
      "docs/教育AI题库系统文档.md": {
        "code_blocks": 2,
        "file_references": 50,
        "size": 77467
      },
      "docs/教育AI全栈设计方案.md": {
        "code_blocks": 67,
        "file_references": 63,
        "size": 119602
      },
      "docs/系统UI设计方案文档.md": {
        "code_blocks": 15,
        "file_references": 29,
        "size": 39625
      }
    }
  }
}
```


#### scripts/4.1.4 停止服务.sh

系统运维Shell脚本，用于服务管理、数据库操作和系统维护

```bash
docker-compose down
```


#### scripts/repo_inventory.json

scripts目录下的json文件，repo_inventory.json

```json
{
  "summary": {
    "total_files": 37,
    "categories": {
      "other": 2,
      "frontend": 2,
      "docs": 2,
      "scripts": 19,
      "backend": 3,
      "infrastructure": 9
    },
    "file_types": {
      "markdown": 5,
      "bash": 3,
      "python": 12,
      "sql": 1,
      "json": 3,
      "yaml": 13
    }
  },
  "files": [
    {
      "path": "auto_review_report.md",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/auto_review_report.md",
      "category": "other",
      "type": "markdown",
      "size": 46,
      "is_documented": false
    },
    {
      "path": "docs/系统UI设计方案文档.md",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/docs/系统UI设计方案文档.md",
      "category": "frontend",
      "type": "markdown",
      "size": 41763,
      "is_documented": false
    },
    {
      "path": "docs/教育AI全栈设计方案.md",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/docs/教育AI全栈设计方案.md",
      "category": "docs",
      "type": "markdown",
      "size": 144514,
      "is_documented": false
    },
    {
      "path": "docs/教育AI题库系统文档.md",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/docs/教育AI题库系统文档.md",
      "category": "docs",
      "type": "markdown",
      "size": 98299,
      "is_documented": false
    },
    {
      "path": "scripts/4.1.4 停止服务.sh",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/4.1.4 停止服务.sh",
      "category": "scripts",
      "type": "bash",
      "size": 20,
      "is_documented": false
    },
    {
      "path": "scripts/auto_review_report.md",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/auto_review_report.md",
      "category": "scripts",
      "type": "markdown",
      "size": 1145,
      "is_documented": false
    },
    {
      "path": "scripts/auto_doc_integration.py",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/auto_doc_integration.py",
      "category": "scripts",
      "type": "python",
      "size": 2610,
      "is_documented": false
    },
    {
      "path": "scripts/md_code_progress_report.py",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/md_code_progress_report.py",
      "category": "scripts",
      "type": "python",
      "size": 2879,
      "is_documented": false
    },
    {
      "path": "scripts/5.2.2 索引优化.sql",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/5.2.2 索引优化.sql",
      "category": "scripts",
      "type": "sql",
      "size": 604,
      "is_documented": false
    },
    {
      "path": "scripts/sync_md_code_autoext.py",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/sync_md_code_autoext.py",
      "category": "scripts",
      "type": "python",
      "size": 1437,
      "is_documented": false
    },
    {
      "path": "scripts/repo_inventory.json",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/repo_inventory.json",
      "category": "scripts",
      "type": "json",
      "size": 9077,
      "is_documented": false
    },
    {
      "path": "scripts/sync_md_code_by_comment.py",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/sync_md_code_by_comment.py",
      "category": "scripts",
      "type": "python",
      "size": 1559,
      "is_documented": false
    },
    {
      "path": "scripts/auto_completion_report.json",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/auto_completion_report.json",
      "category": "scripts",
      "type": "json",
      "size": 2161,
      "is_documented": false
    },
    {
      "path": "scripts/4.2.2 创建命名空间.sh",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/4.2.2 创建命名空间.sh",
      "category": "scripts",
      "type": "bash",
      "size": 39,
      "is_documented": false
    },
    {
      "path": "scripts/auto_review_md_vs_code.py",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/auto_review_md_vs_code.py",
      "category": "scripts",
      "type": "python",
      "size": 2686,
      "is_documented": false
    },
    {
      "path": "scripts/doc_parser.py",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/doc_parser.py",
      "category": "scripts",
      "type": "python",
      "size": 9104,
      "is_documented": false
    },
    {
      "path": "scripts/4.2.9 初始化数据库.sh",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/4.2.9 初始化数据库.sh",
      "category": "scripts",
      "type": "bash",
      "size": 519,
      "is_documented": false
    },
    {
      "path": "scripts/doc_analysis.json",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/doc_analysis.json",
      "category": "scripts",
      "type": "json",
      "size": 160299,
      "is_documented": false
    },
    {
      "path": "scripts/auto_doc_completion.py",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/auto_doc_completion.py",
      "category": "scripts",
      "type": "python",
      "size": 15009,
      "is_documented": false
    },
    {
      "path": "scripts/split_md_code_autosave.py",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/split_md_code_autosave.py",
      "category": "scripts",
      "type": "python",
      "size": 2348,
      "is_documented": false
    },
    {
      "path": "scripts/sync_md_code.py",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/sync_md_code.py",
      "category": "scripts",
      "type": "python",
      "size": 904,
      "is_documented": false
    },
    {
      "path": "scripts/repo_scanner.py",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/repo_scanner.py",
      "category": "scripts",
      "type": "python",
      "size": 6328,
      "is_documented": false
    },
    {
      "path": "scripts/split_md_code_advanced.py",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/scripts/split_md_code_advanced.py",
      "category": "scripts",
      "type": "python",
      "size": 629,
      "is_documented": false
    },
    {
      "path": "infra/k8s/backend-deployment_3.yaml",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/infra/k8s/backend-deployment_3.yaml",
      "category": "backend",
      "type": "yaml",
      "size": 987,
      "is_documented": false
    },
    {
      "path": "infra/k8s/mariadb-configmap_2.yaml",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/infra/k8s/mariadb-configmap_2.yaml",
      "category": "infrastructure",
      "type": "yaml",
      "size": 280,
      "is_documented": false
    },
    {
      "path": "infra/k8s/tls-secret.yaml",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/infra/k8s/tls-secret.yaml",
      "category": "infrastructure",
      "type": "yaml",
      "size": 260,
      "is_documented": false
    },
    {
      "path": "infra/k8s/network-policy.yaml",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/infra/k8s/network-policy.yaml",
      "category": "infrastructure",
      "type": "yaml",
      "size": 617,
      "is_documented": false
    },
    {
      "path": "infra/k8s/redis-persistent.yaml",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/infra/k8s/redis-persistent.yaml",
      "category": "infrastructure",
      "type": "yaml",
      "size": 416,
      "is_documented": false
    },
    {
      "path": "infra/k8s/mariadb-configmap.yaml",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/infra/k8s/mariadb-configmap.yaml",
      "category": "infrastructure",
      "type": "yaml",
      "size": 1236,
      "is_documented": false
    },
    {
      "path": "infra/k8s/backend-deployment.yaml",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/infra/k8s/backend-deployment.yaml",
      "category": "backend",
      "type": "yaml",
      "size": 288,
      "is_documented": false
    },
    {
      "path": "infra/k8s/frontend-deployment.yaml",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/infra/k8s/frontend-deployment.yaml",
      "category": "frontend",
      "type": "yaml",
      "size": 640,
      "is_documented": false
    },
    {
      "path": "infra/k8s/rename_yaml_by_content.py",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/infra/k8s/rename_yaml_by_content.py",
      "category": "infrastructure",
      "type": "python",
      "size": 1736,
      "is_documented": false
    },
    {
      "path": "infra/k8s/redis-deployment.yaml",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/infra/k8s/redis-deployment.yaml",
      "category": "infrastructure",
      "type": "yaml",
      "size": 678,
      "is_documented": false
    },
    {
      "path": "infra/k8s/ingress.yaml",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/infra/k8s/ingress.yaml",
      "category": "infrastructure",
      "type": "yaml",
      "size": 299,
      "is_documented": false
    },
    {
      "path": "infra/k8s/backend-deployment_2.yaml",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/infra/k8s/backend-deployment_2.yaml",
      "category": "backend",
      "type": "yaml",
      "size": 1218,
      "is_documented": false
    },
    {
      "path": "infra/k8s/ingress_2.yaml",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/infra/k8s/ingress_2.yaml",
      "category": "infrastructure",
      "type": "yaml",
      "size": 707,
      "is_documented": false
    },
    {
      "path": ".github/workflows/auto-review.yml",
      "absolute_path": "/home/runner/work/Edu-ai-question-bank/Edu-ai-question-bank/.github/workflows/auto-review.yml",
      "category": "other",
      "type": "yaml",
      "size": 622,
      "is_documented": false
    }
  ]
}
```
