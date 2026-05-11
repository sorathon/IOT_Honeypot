## Presentation : https://canva.link/t0xxfzz8pekncoo


Internet / Attacker (แฮกเกอร์, บอทเน็ต)
        │
        ▼ (ตั้งค่า Router: Forward Port 80, 2222, 445 มาที่ Pi)
┌────────────────────────────────────────────────────────┐
│ 🍓 Raspberry Pi (โซน DMZ / Level 3.5 - กับดัก)            
│                                      
│                                                        
│ 🪤 ระบบลวงตา (สร้าง Log):                                 
│  ├─ Port 8081   -> 🐍 Python Flask (เว็บ SCADA ปลอม)     
│  ├─ Port 2222/2223 -> 🐚 Cowrie (ดักการเจาะ SSH)            
│  └─opencanary  
      - "8080"
      - "21"
      - "1433" # เพิ่ม port mssql ตาม config ของคุณด้วย
│                                                        
│ 📤 ตัวส่งข้อมูล (Log Shipper):                            
│  └─ 📦 Filebeat (คอยอ่านไฟล์ Log จาก 3 ตัวบน)             
└───────┬────────────────────────────────────────────────┘
        │
        │ 🔒 Firewall (จำลองด้วย Windows Firewall บน Notebook)
        │ ✅ อนุญาต: Pi ส่งข้อมูลเข้า Port 5044 (Logstash) ได้
        │ ❌ บล็อก: ห้าม Pi เข้าถึง Port 8082 (เว็บจริง) เด็ดขาด
        ▼
┌────────────────────────────────────────────────────────┐
│ 💻 Notebook (โซน IT & OT / Level 4 & Level 3)           
│                                    
│                                                        
│ 🚦 โซน IT / SOC (Level 4 - วิเคราะห์ข้อมูล):              
│  └─ 🔀 Logstash (Port 5044) รับ Log จาก Pi แล้วแยกส่ง     
│         ├─ ขาที่ 1 ──> 🟡 Elastic & Kibana (Port 5601)   
│      
│                                                        
│ 🏭 โซน OT (Level 3 - ระบบจริง):                          
│  └─ 🌐 Python Web Server (Port 8082) -> เว็บ SCADA จริง 
└────────────────────────────────────────────────────────┘
