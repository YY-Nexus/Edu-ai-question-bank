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
