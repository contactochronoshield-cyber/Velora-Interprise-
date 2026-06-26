import sqlite3
from flask import request,session,redirect

DB="database/velora.db"

def login():

    email=request.form["email"]
    password=request.form["password"]

    conn=sqlite3.connect(DB)
    conn.row_factory=sqlite3.Row

    user=conn.execute(
    "SELECT * FROM users WHERE email=? AND password=?",
    (email,password)
    ).fetchone()

    conn.close()

    if user:

        session["user"]=user["id"]

        return redirect("/")

    return "Invalid credentials"

def register():

    company=request.form["company"]
    email=request.form["email"]
    password=request.form["password"]

    conn=sqlite3.connect(DB)

    conn.execute(
    "INSERT INTO users(name,email,password,role) VALUES(?,?,?,?)",
    (company,email,password,"customer")
    )

    conn.commit()

    conn.close()

    return redirect("/login")
