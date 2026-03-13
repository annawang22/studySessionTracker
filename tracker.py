import sqlite3

def init_db():
    conn = sqlite3.connect('study_sessions.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_date TEXT,
        duration REAL,
        subject TEXT,
        task_type TEXT,
        focus_rating INTEGER    )''')

    conn.commit()
    return conn

def log_session(conn):
    print("\n--- Log a Study Session ---")
    session_date = input("Date (YYYY-MM-DD): ")
    duration = float(input("Duration (hours): "))
    subject = input("Subject: ")
    task_type = input("Task type: ")
    focus_rating = int(input("Focus rating (1-5): "))

    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sessions (session_date, duration, subject, task_type, focus_rating)
        VALUES (?, ?, ?, ?, ?)
    ''', (session_date, duration, subject, task_type, focus_rating))
    conn.commit()
    print("Session logged successfully!")

conn = init_db()
log_session(conn)
conn.close()    