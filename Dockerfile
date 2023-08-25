# 使用官方的 Python 镜像作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 将当前目录中的 requirements.txt 复制到容器的 /app 目录中
COPY requirements.txt requirements.txt

# 安装项目依赖项
RUN pip install -r requirements.txt

# 将当前目录中的文件夹复制到容器的 /app 目录中
COPY . .

# 设置环境变量
ENV FLASK_APP=app.py

# 暴露应用程序运行的端口
EXPOSE 5000

# 启动应用程序
CMD ["gunicorn", "app:app", "-c", "gunicorn_config.py"]