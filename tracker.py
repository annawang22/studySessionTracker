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

def view_sessions(conn, subject=None):
    cursor = conn.cursor()
    if subject:
        cursor.execute('SELECT * FROM sessions WHERE subject = ?', (subject,))
    else:
        cursor.execute('SELECT * FROM sessions')
    
    rows = cursor.fetchall()

    if not rows:
        print("No sessions logged yet.")
        return

    print("\n--- Your Study Sessions ---")
    for row in rows:
        print(f"ID: {row[0]} | Date: {row[1]} | Duration: {row[2]}hrs | Subject: {row[3]} | Task: {row[4]} | Focus: {row[5]}/5")

def get_record(conn, session_id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sessions WHERE id = ?', (session_id,))
    row = cursor.fetchone()

    if not row:
        print(f"No session found with ID {session_id}.")
        return None

    print(f"\nID: {row[0]} | Date: {row[1]} | Duration: {row[2]}hrs | Subject: {row[3]} | Task: {row[4]} | Focus: {row[5]}/10")
    return row

def update_session(conn):
    view_sessions(conn)
    session_id = int(input("\nEnter the ID of the session you want to update: "))
    
    row = get_record(conn, session_id)
    if row is None:
        return

    fields = ['session_date', 'duration', 'subject', 'task_type', 'focus_rating']
    print("\nWhich fields do you want to update?")
    for i, field in enumerate(fields, start=1):
        print(f"{i}. {field}")
    
    choices = input("\nEnter the numbers of the fields you want to change (e.g. 1 3): ").split()
    choices = [int(c) for c in choices]

    updates = []
    values = []
    for choice in choices:
        field = fields[choice - 1]
        new_value = input(f"New value for {field}: ")
        updates.append(f"{field} = ?")
        values.append(new_value)

    values.append(session_id)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE sessions SET {', '.join(updates)} WHERE id = ?", values)
    conn.commit()
    print("Session updated successfully!")

def delete_session(conn):
    view_sessions(conn)
    session_id = int(input("\nEnter the ID of the session you want to delete: "))

    row = get_record(conn, session_id)
    if row is None:
        return

    confirm = input("\nAre you sure you want to delete this session? (y/n): ")
    if confirm.lower() == 'y':
        cursor = conn.cursor()
        cursor.execute('DELETE FROM sessions WHERE id = ?', (session_id,))
        conn.commit()
        print("Session deleted successfully!")
    else:
        print("Deletion cancelled.")

conn = init_db()

while True:
    print("\n--- Study Session Tracker ---")
    print("1. Log a session")
    print("2. View all sessions")
    print("3. Filter by subject")
    print("4. Update a session")
    print("5. Delete a session")
    print("6. Quit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        log_session(conn)
    elif choice == '2':
        view_sessions(conn)
    elif choice == '3':
        subject = input("Enter subject to filter by: ")
        view_sessions(conn, subject)
    elif choice == '4':
        update_session(conn)
    elif choice == '5':
        delete_session(conn)
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")

conn.close()  