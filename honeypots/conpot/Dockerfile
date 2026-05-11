FROM python:3.9-slim

# ติดตั้ง Library สำหรับคุย Modbus (ใช้ได้ทั้ง x86 และ ARM/Raspberry Pi)
RUN pip install pymodbus==3.5.4

WORKDIR /app

# Copy สคริปต์จำลอง PLC ที่เราจะเขียนในขั้นตอนถัดไป
COPY sim_plc.py .

# รันสคริปต์จำลองทันทีเมื่อ Container เริ่มทำงาน
CMD ["python", "sim_plc.py"]
