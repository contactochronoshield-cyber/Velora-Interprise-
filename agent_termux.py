import os
import socket
import platform
import sqlite3
from datetime import datetime

DB="database/velora.db"

hostname=socket.gethostname()

try:
    ip=socket.gethostbyname(hostname)
except:
    ip="unknown"

system=platform.system()
release=platform.release()

conn=sqlite3.connect(DB)
cur=conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS devices(
id INTEGER PRIMARY KEY AUTOINCREMENT,
hostname TEXT,
ip TEXT,
system TEXT,
release TEXT,
status TEXT,
last_seen TEXT
)
""")

cur.execute("""
INSERT INTO devices
(hostname,ip,system,release,status,last_seen)
VALUES(?,?,?,?,?,?)
""",
(
hostname,
ip,
system,
release,
"ONLINE",
datetime.now().isoformat()
))

conn.commit()
conn.close()

print("DEVICE REGISTERED")
