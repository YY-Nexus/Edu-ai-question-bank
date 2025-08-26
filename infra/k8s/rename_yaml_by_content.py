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