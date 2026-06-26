from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3
import socket
import platform
from datetime import datetime

try:
    import psutil
except:
    psutil = None

app = Flask(__name__)
app.secret_key = "VELORA_ENTERPRISE"

DATABASE = "database/velora.db"

def db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def cpu():
    try:
        return psutil.cpu_percent()
    except:
        return 0

def ram():
    try:
        return psutil.virtual_memory().percent
    except:
        return 0

def disk():
    try:
        return psutil.disk_usage("/").percent
    except:
        return 0

@app.route("/")
def dashboard():

    conn = db()

    try:
        customers = conn.execute("SELECT COUNT(*) total FROM customers").fetchone()["total"]
    except:
        customers = 0

    try:
        devices = conn.execute("SELECT COUNT(*) total FROM devices").fetchone()["total"]
    except:
        devices = 0

    try:
        alerts = conn.execute("SELECT COUNT(*) total FROM alerts").fetchone()["total"]
    except:
        alerts = 0

    conn.close()

    return render_template(
        "dashboard.html",
        customers=customers,
        devices=devices,
        alerts=alerts,
        cpu=cpu(),
        ram=ram(),
        disk=disk(),
        hostname=socket.gethostname(),
        system=platform.system(),
        date=datetime.now()
    )

# =====================================
# LOGIN
# =====================================

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        conn = db()

        try:
            user = conn.execute(
                "SELECT * FROM users WHERE email=? AND password=?",
                (email,password)
            ).fetchone()
        except:
            user = None

        conn.close()

        if user:
            session["user"] = email
            return redirect("/")

        return render_template(
            "login.html",
            error="Credenciales incorrectas"
        )

    return render_template("login.html")


# =====================================
# LOGOUT
# =====================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


# =====================================
# REGISTER CUSTOMER
# =====================================

@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        company = request.form.get("company")
        email = request.form.get("email")
        phone = request.form.get("phone")
        country = request.form.get("country")

        conn = db()

        try:

            conn.execute("""

            INSERT INTO customers
            (
            company,
            email,
            phone,
            country
            )

            VALUES
            (
            ?,?,?,?
            )

            """,(company,email,phone,country))

            conn.commit()

        except Exception as e:

            print(e)

        conn.close()

        return redirect("/customers")

    return render_template("register.html")


# =====================================
# CUSTOMERS
# =====================================

@app.route("/customers")
def customers():

    conn=db()

    try:
        rows=conn.execute(
            "SELECT * FROM customers ORDER BY id DESC"
        ).fetchall()
    except:
        rows=[]

    conn.close()

    return render_template(
        "customers.html",
        customers=rows
    )



# =====================================
# DEVICES
# =====================================

@app.route("/devices")
def devices():

    conn = db()

    try:

        rows = conn.execute("""

        SELECT *

        FROM devices

        ORDER BY id DESC

        """).fetchall()

    except:

        rows = []

    conn.close()

    return render_template(

        "devices.html",

        devices=rows

    )


# =====================================
# MONITORING
# =====================================

@app.route("/monitoring")
def monitoring():

    return render_template(

        "monitoring.html"

    )


# =====================================
# SECURITY
# =====================================

@app.route("/security")
def security():

    return render_template(

        "security.html"

    )


# =====================================
# ALERTS
# =====================================

@app.route("/alerts")
def alerts():

    conn = db()

    try:

        rows = conn.execute("""

        SELECT *

        FROM alerts

        ORDER BY id DESC

        """).fetchall()

    except:

        rows=[]

    conn.close()

    return render_template(

        "alerts.html",

        alerts=rows

    )



# =====================================
# API STATUS
# =====================================

@app.route("/api/status")
def api_status():

    return jsonify({

        "hostname": socket.gethostname(),

        "system": platform.system(),

        "cpu": cpu(),

        "ram": ram(),

        "disk": disk(),

        "time": str(datetime.now()),

        "status": "ONLINE"

    })


# =====================================
# HEALTH
# =====================================

@app.route("/health")
def health():

    return jsonify({

        "service": "Velora Enterprise",

        "version": "1.0",

        "status": "ONLINE"

    })


# =====================================
# VCH777
# =====================================

@app.route("/api/vch777")
def api_vch777():

    return jsonify({

        "engine": "VCH777 CYBER",

        "firewall": "ACTIVE",

        "ids": "ACTIVE",

        "ips": "ACTIVE",

        "monitor": "ACTIVE",

        "threats": 0,

        "status": "SECURE"

    })


# =====================================
# SERVER INFO
# =====================================

@app.route("/api/server")
def api_server():

    return jsonify({

        "hostname": socket.gethostname(),

        "system": platform.system(),

        "python": platform.python_version(),

        "database": DATABASE

    })


# =====================================
# START SERVER
# =====================================

if __name__ == "__main__":

    print("=" * 60)
    print("VELORA ENTERPRISE")
    print("Chrono Shield Networks")
    print("=" * 60)
    print("Dashboard  : http://127.0.0.1:5000")
    print("API Status : /api/status")
    print("VCH777     : /api/vch777")
    print("=" * 60)

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

