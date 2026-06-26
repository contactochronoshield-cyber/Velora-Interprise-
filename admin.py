import sqlite3

DB="database/velora.db"

while True:

    print("")
    print("===== VELORA ADMIN =====")
    print("1. View Devices")
    print("2. View Registrations")
    print("3. View Audit Logs")
    print("4. Exit")

    op=input("> ")

    conn=sqlite3.connect(DB)
    cur=conn.cursor()

    if op=="1":

        rows=cur.execute(
        "SELECT id,hostname,ip,status,last_seen FROM devices"
        ).fetchall()

        for r in rows:
            print(r)

    elif op=="2":

        rows=cur.execute(
        "SELECT * FROM registrations"
        ).fetchall()

        for r in rows:
            print(r)

    elif op=="3":

        rows=cur.execute(
        "SELECT * FROM audit_logs ORDER BY id DESC"
        ).fetchall()

        for r in rows:
            print(r)

    elif op=="4":
        conn.close()
        break

    conn.close()
