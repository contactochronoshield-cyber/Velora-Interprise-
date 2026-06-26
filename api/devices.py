import sqlite3

DB="database/velora.db"

def all():

    conn=sqlite3.connect(DB)

    conn.row_factory=sqlite3.Row

    rows=conn.execute(
    "SELECT * FROM devices ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return rows
