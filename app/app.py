from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = mysql.connector.connect(
            host="mysql",
            user="root",
            password="root123",
            database="mydb"
        )

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS visits(
            id INT AUTO_INCREMENT PRIMARY KEY,
            visit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("INSERT INTO visits() VALUES()")
        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM visits")
        count = cursor.fetchone()[0]

        conn.close()

        return f"<h1>CCS3308 Assignment</h1><h2>Total Visits: {count}</h2>"

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
