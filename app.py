from flask import request
import sqlite3
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database/velora.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT,
        status TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS nodes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hostname TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/clients")
def clients():
    return "<h1>Clients Portal</h1>"

@app.route("/nodes")
def nodes():
    return "<h1>Nodes Center</h1>"

@app.route("/security")
def security():
    return "<h1>Security Center</h1>"

@app.route("/monitoring")
def monitoring():
    return "<h1>Monitoring Center</h1>"
@app.route("/register",methods=["GET","POST"])
def register():

    if request.method=="POST":

        name=request.form["name"]
        email=request.form["email"]
        company=request.form["company"]

        conn=sqlite3.connect("database/velora.db")
        cur=conn.cursor()

        cur.execute(
        """
        INSERT INTO registrations
        (name,email,company,ip)
        VALUES(?,?,?,?)
        """,
        (
        name,
        email,
        company,
        request.remote_addr
        )
        )

        cur.execute(
        """
        INSERT INTO audit_logs
        (action,details)
        VALUES(?,?)
        """,
        (
        "NEW_REGISTRATION",
        email
        )
        )

        conn.commit()
        conn.close()

        return """
        <h1>Registration Complete</h1>
        """

    return render_template("register.html")
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0",port=5000,debug=True)
