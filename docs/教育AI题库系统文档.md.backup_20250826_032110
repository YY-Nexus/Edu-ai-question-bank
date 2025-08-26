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