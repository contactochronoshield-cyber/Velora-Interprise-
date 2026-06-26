import sqlite3

conn=sqlite3.connect("database/velora.db")
cur=conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS registrations(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
company TEXT,
ip TEXT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS audit_logs(
id INTEGER PRIMARY KEY AUTOINCREMENT,
action TEXT,
details TEXT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("REGISTRATION DATABASE READY")
