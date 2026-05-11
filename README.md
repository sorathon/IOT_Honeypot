## Presentation : https://canva.link/t0xxfzz8pekncoo


🌐 Level 5 – Internet / Attacker
( Hacker / Botnet / Scanner )
            │
            │  (Port Forward: 80, 2222)
            ▼
┌──────────────────────────────────────────────┐
│ 🍓 Level 3.5 – DMZ (Raspberry Pi)            │
│                                              │
│  🔥 Nginx (Reverse Proxy) ⭐                  │
│  - ตรวจ IP (Tailscale 100.x.x.x)             │
│  - Route Traffic                             │
│      ├─ Internet → Fake SCADA                │
│      └─ VPN → Real SCADA                     │
│                                              │
│  🎭 Fake Login + Fake SCADA (8081)           │
│  - Flask                                     │
│  - Sensor ปลอม                               │
│  - เก็บ credential                           │
│                                              │
│  🐚 Cowrie (SSH Honeypot - 2222)             │
│  🐤 OpenCanary (21, 445, 1433)               │
│                                              │
│  📦 Filebeat                                 │
│  - ส่ง log → Notebook                        │
└───────────────┬──────────────────────────────┘
                │
                │ 🔒 Firewall (Block ไป SCADA จริง)
                ▼
┌──────────────────────────────────────────────┐
│ 💻 Level 4 – IT / SOC (Notebook)             │
│                                              │
│  🔀 Logstash (5044)                          │
│  📊 Elasticsearch                            │
│  📈 Kibana                                   │
│                                              │
│  🔐 Tailscale VPN ⭐                          │
│  - ใช้เข้า SCADA จริง                        │
└───────────────┬──────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────┐
│ 🏭 Level 3 – SCADA REAL                      │
│                                              │
│  🌐 Real Login + SCADA (8082)                │
│  - เข้าผ่าน VPN เท่านั้น                   │
│                                              │
└───────────────┬──────────────────────────────┘
                ▼
┌──────────────────────────────────────────────┐
│ ⚙️ Level 2 – Control Network                │
│  • ESP32 (PLC จำลอง)                        │
└──────────────────────────────────────────────┘
