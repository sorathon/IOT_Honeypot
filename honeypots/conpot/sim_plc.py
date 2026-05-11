import asyncio
import logging
from pymodbus.server import StartAsyncTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext

# ตั้งค่า Log เพื่อให้เห็นว่ามีใครมาสั่งเขียนค่า (Write) หรือไม่
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

async def run_server():
    # จองพื้นที่ 100 ช่อง: [0]=Temp, [1]=Pump Status (0 หรือ 1)
    initial_values = [0] * 100
    initial_values[0] = 25  
    initial_values[1] = 1   

    # hr คือ Holding Register (อ่าน/เขียนได้)
    store = ModbusSlaveContext(
        hr=ModbusSequentialDataBlock(0, initial_values),
        zero_mode=True
    )
    context = ModbusServerContext(slaves=store, single=True)

    identity = ModbusDeviceIdentification()
    identity.VendorName = 'Siemens'
    identity.ProductCode = 'S7-200'
    identity.ProductName = 'Honeypot SCADA System'

    print("PLC Simulator (Modbus TCP) started on port 502...")
    await StartAsyncTcpServer(context, identity=identity, address=("0.0.0.0", 502))

if __name__ == "__main__":
    asyncio.run(run_server())
