from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    jsonify
)

import sqlite3
import platform
import socket
import psutil
from datetime import datetime

app = Flask(__name__)
app.secret_key = "VELORA_ENTERPRISE"

DATABASE = "database/velora.db"


# -------------------------
# DATABASE
# -------------------------

def db():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn


# -------------------------
# DASHBOARD
# -------------------------

@app.route("/")
def dashboard():

    conn = db()

    customers = conn.execute(
        "SELECT COUNT(*) total FROM customers"
    ).fetchone()["total"]

    devices = conn.execute(
        "SELECT COUNT(*) total FROM devices"
    ).fetchone()["total"]

    alerts = conn.execute(
        "SELECT COUNT(*) total FROM alerts"
    ).fetchone()["total"]

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    disk = psutil.disk_usage("/").percent

    hostname = socket.gethostname()

    conn.close()

    return render_template(

        "dashboard.html",

        customers=customers,

        devices=devices,

        alerts=alerts,

        cpu=cpu,

        ram=ram,

        disk=disk,

        hostname=hostname,

        system=platform.system(),

        date=datetime.now()

    )


# -------------------------
# LOGIN
# -------------------------

@app.route("/login",methods=["GET","POST"])
def login():

    if request.method=="POST":

        email=request.form["email"]

        password=request.form["password"]

        conn=db()

        user=conn.execute(

            "SELECT * FROM users WHERE email=? AND password=?",

            (email,password)

        ).fetchone()

        conn.close()

        if user:

            session["user"]=user["email"]

            return redirect("/")

    return render_template("login.html")


# -------------------------
# LOGOUT
# -------------------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


# -------------------------
# REGISTER
# -------------------------

@app.route("/register",methods=["GET","POST"])
def register():

    if request.method=="POST":

        conn=db()

        conn.execute(

            """
            INSERT INTO customers(

            company,

            email,

            phone,

            country

            )

            VALUES(

            ?,?,?,?

            )
            """,

            (

            request.form["company"],

            request.form["email"],

            request.form["phone"],

            request.form["country"]

            )

        )

        conn.commit()

        conn.close()

        return redirect("/customers")

    return render_template("register.html")


# -------------------------
# CUSTOMERS
# -------------------------

@app.route("/customers")
def customers():

    conn=db()

    rows=conn.execute(

        "SELECT * FROM customers ORDER BY id DESC"

    ).fetchall()

    conn.close()

    return render_template(

        "customers.html",

        customers=rows

    )


# -------------------------
# DEVICES
# -------------------------

@app.route("/devices")
def devices():

    conn=db()

    rows=conn.execute(

        "SELECT * FROM devices ORDER BY id DESC"

    ).fetchall()

    conn.close()

    return render_template(

        "devices.html",

        devices=rows

    )


# -------------------------
# SECURITY
# -------------------------

@app.route("/security")
def security():

    return render_template("security.html")


# -------------------------
# ALERTS
# -------------------------

@app.route("/alerts")
def alerts():

    conn=db()

    rows=conn.execute(

        "SELECT * FROM alerts"

    ).fetchall()

    conn.close()

    return render_template(

        "alerts.html",

        alerts=rows

    )


# -------------------------
# MONITORING
# -------------------------

@app.route("/monitoring")
def monitoring():

    return render_template(

        "monitoring.html"

    )


# -------------------------
# STATUS API
# -------------------------

@app.route("/api/status")
def api_status():

    return jsonify({

        "hostname":socket.gethostname(),

        "system":platform.system(),

        "cpu":psutil.cpu_percent(),

        "ram":psutil.virtual_memory().percent,

        "disk":psutil.disk_usage("/").percent,

        "time":str(datetime.now())

    })


# -------------------------
# START
# -------------------------

if __name__=="__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )

