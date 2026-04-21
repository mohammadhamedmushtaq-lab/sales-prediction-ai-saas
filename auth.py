import sqlite3

def register(username, password):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, password))
    conn.commit()
    conn.close()

def login(username, password):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cur.fetchone()
    conn.close()
    return user