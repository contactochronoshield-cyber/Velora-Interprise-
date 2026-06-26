from flask import jsonify
import sqlite3

DB="database/velora.db"

def devices():

    conn=sqlite3.connect(DB)
    conn.row_factory=sqlite3.Row

    rows=conn.execute(
    "SELECT * FROM devices"
    ).fetchall()

    conn.close()

    return jsonify([dict(r) for r in rows])

def customers():

    conn=sqlite3.connect(DB)
    conn.row_factory=sqlite3.Row

    rows=conn.execute(
    "SELECT * FROM customers"
    ).fetchall()

    conn.close()

    return jsonify([dict(r) for r in rows])
