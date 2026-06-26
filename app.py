from flask import Flask,render_template,jsonify
import sqlite3
import psutil
import platform

app=Flask(__name__)

DB="database/velora.db"

def query(sql):

    conn=sqlite3.connect(DB)
    conn.row_factory=sqlite3.Row

    rows=conn.execute(sql).fetchall()

    conn.close()

    return rows

@app.route("/")
def dashboard():

    return render_template(
        "dashboard.html",
        cpu=psutil.cpu_percent(),
        ram=psutil.virtual_memory().percent,
        disk=psutil.disk_usage("/").percent,
        system=platform.system(),
        devices=len(query("select * from devices")),
        customers=len(query("select * from customers")),
        alerts=len(query("select * from alerts"))
    )

@app.route("/customers")
def customers():
    return render_template(
        "customers.html",
        customers=query("select * from customers")
    )

@app.route("/devices")
def devices():
    return render_template(
        "devices.html",
        devices=query("select * from devices")
    )

@app.route("/monitoring")
def monitoring():
    return render_template("monitoring.html")

@app.route("/security")
def security():
    return render_template("security.html")

@app.route("/alerts")
def alerts():
    return render_template(
        "alerts.html",
        alerts=query("select * from alerts")
    )

@app.route("/api/status")
def api():

    return jsonify({

        "platform":"Velora Enterprise",

        "status":"ONLINE",

        "cpu":psutil.cpu_percent(),

        "ram":psutil.virtual_memory().percent,

        "disk":psutil.disk_usage("/").percent,

        "devices":len(query("select * from devices"))

    })

if __name__=="__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )

