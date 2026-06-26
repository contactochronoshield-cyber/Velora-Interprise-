import sqlite3
import socket
import platform
import psutil
from datetime import datetime

DB="database/velora.db"

conn=sqlite3.connect(DB)
c=conn.cursor()

hostname=socket.gethostname()

try:
    ip=socket.gethostbyname(hostname)
except:
    ip="0.0.0.0"

try:
    battery=psutil.sensors_battery().percent
except:
    battery=-1

cpu=psutil.cpu_percent(interval=1)
ram=psutil.virtual_memory().percent
disk=psutil.disk_usage("/").percent

c.execute("""
INSERT INTO devices(
hostname,
ip,
system,
release,
cpu,
ram,
disk,
battery,
status,
last_seen
)
VALUES(?,?,?,?,?,?,?,?,?,?)
""",
(
hostname,
ip,
platform.system(),
platform.release(),
cpu,
ram,
disk,
battery,
"ONLINE",
datetime.now().strftime("%Y-%m-%d %H:%M:%S")
))

conn.commit()
conn.close()

print("DEVICE REGISTERED")
