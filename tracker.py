import sqlite3

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