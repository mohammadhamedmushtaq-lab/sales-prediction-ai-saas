import sqlite3

DB_PATH = "users.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


def register(username, password):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        return "SUCCESS"

    except sqlite3.IntegrityError:
        return "USER_ALREADY_EXISTS"

    except Exception as e:
        return str(e)   # 🔥 important for debugging

    finally:
        conn.close()


def login(username, password):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cur.fetchone()
    conn.close()
    return user
