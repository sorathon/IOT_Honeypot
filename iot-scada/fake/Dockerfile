FROM python:3.9-slim

WORKDIR /app

# ติดตั้ง Library ที่จำเป็น
RUN pip install flask flask-cors

# Copy ไฟล์ทั้งหมด (app.py และโฟลเดอร์ templates) เข้าไป
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
