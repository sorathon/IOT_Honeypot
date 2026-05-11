FROM python:3.9-slim

# 1. ติดตั้ง Dependencies
RUN apt-get update && apt-get install -y \
    git libssl-dev libffi-dev build-essential python3-dev \
    && rm -rf /var/lib/apt/lists/*

# 2. เตรียม User
RUN useradd -m -d /home/cowrie cowrie
USER cowrie
WORKDIR /home/cowrie

# 3. Clone ลงที่จุดนี้เลย (ใช้ . เพื่อไม่ให้โฟลเดอร์ซ้อน)
RUN git clone https://github.com/cowrie/cowrie.git .

# 4. ติดตั้ง Virtual Env
RUN python3 -m venv cowrie-env && \
    ./cowrie-env/bin/pip install --upgrade pip && \
    ./cowrie-env/bin/pip install -r requirements.txt

# 5. รันโดยระบุ PYTHONPATH ให้ครอบคลุม
ENV PYTHONPATH=/home/cowrie
EXPOSE 2222 2223

# ใช้ท่ามาตรฐานที่ Cowrie ออกแบบมาให้รันใน Docker
CMD ["./cowrie-env/bin/python3", "-m", "twisted", "--nodaemon", "-y", "cowrie.tac", "--pidfile", "var/run/cowrie.pid", "cowrie"]
