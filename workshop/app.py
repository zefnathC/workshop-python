from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Koneksi ke database
conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Membuat tabel jika belum ada
cur.execute('''CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL)''')
conn.commit()

@app.route('/')
def index():
    # Mengambil data dari database
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run()
