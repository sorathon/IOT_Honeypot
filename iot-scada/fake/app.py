from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS
from datetime import datetime
import json  # <--- เพิ่มเข้ามา
import os    # <--- เพิ่มเข้ามา

app = Flask(__name__, template_folder='templates')
CORS(app)

scada_data = {
    "temp": 0,
    "pump": 0
}

# ==========================================
# ส่วนที่ 1: หน้า Login ดักแฮกเกอร์ (Honeypot)
# ==========================================
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        ip = request.headers.get('X-Real-IP', request.remote_addr)
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 1. ปริ้นท์ Log ประจาน (สำหรับ Node-RED เหมือนเดิม)
        print(f"[HONEYPOT ALERT] Time:{time_now} | IP:{ip} | User:{user} | Pass:{pwd}", flush=True)

        # 2. สร้างก้อนข้อมูล JSON สำหรับ Filebeat
        log_entry = {
            "@timestamp": datetime.utcnow().isoformat() + "Z", # Format เวลามาตรฐานให้ Filebeat รู้จัก
            "src_ip": ip,
            "username": user,
            "password": pwd,
            "event_action": "scada_web_login"
        }

        # 3. เขียนลงไฟล์ scada_auth.json (ให้ Filebeat มาอ่าน)
        os.makedirs('/var/log/scada', exist_ok=True) # สร้างโฟลเดอร์ถ้ายังไม่มี
        with open('/var/log/scada/scada_auth.json', 'a') as f:
            f.write(json.dumps(log_entry) + '\n')

        return redirect(url_for('dashboard'))

    return render_template('login.html')

# (ส่วนอื่นๆ ของโค้ดปล่อยไว้เหมือนเดิมครับ)
# ==========================================

# ส่วนที่ 2: หน้าเว็บแสดงผล SCADA ปลอม

# ==========================================

@app.route('/dashboard')

def dashboard():

    # เปลี่ยนจากเดิมที่เคยอยู่หน้า '/' ย้ายมานี่แทน

    return render_template('index.html')



# ==========================================

# ส่วนที่ 3: รับ-ส่งข้อมูลกับ Node-RED (ของเดิม)

# ==========================================

@app.route('/update_data', methods=['POST'])

def update_data():

    global scada_data

    data = request.json

    if data:

        scada_data["temp"] = data.get("temp", scada_data["temp"])

        scada_data["pump"] = data.get("pump", scada_data["pump"])

        # print(f"Current State: {scada_data}") # ปิด/เปิดเพื่อเช็กค่าจาก Node-RED

    return jsonify({"status": "success"})



@app.route('/get_status')

def get_status():

    return jsonify(scada_data)



if __name__ == '__main__':

    # รันบน Port 5000

    app.run(host='0.0.0.0', port=5000)
