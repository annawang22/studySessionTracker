import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('study_sessions.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db()
    sessions = conn.execute('SELECT * FROM sessions').fetchall()
    conn.close()
    return render_template('index.html', sessions=sessions)

@app.route('/add', methods=['GET', 'POST'])
def add_session():
    if request.method == 'POST':
        session_date = request.form['session_date']
        duration = float(request.form['duration'])
        subject = request.form['subject']
        task_type = request.form['task_type']
        focus_rating = int(request.form['focus_rating'])

        conn = get_db()
        conn.execute('''
            INSERT INTO sessions (session_date, duration, subject, task_type, focus_rating)
            VALUES (?, ?, ?, ?, ?)
        ''', (session_date, duration, subject, task_type, focus_rating))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('add.html')

@app.route('/edit/<int:session_id>', methods=['GET', 'POST'])
def edit_session(session_id):
    conn = get_db()

    if request.method == 'POST':
        session_date = request.form['session_date']
        duration = float(request.form['duration'])
        subject = request.form['subject']
        task_type = request.form['task_type']
        focus_rating = int(request.form['focus_rating'])

        conn.execute('''
            UPDATE sessions
            SET session_date = ?, duration = ?, subject = ?, task_type = ?, focus_rating = ?
            WHERE id = ?
        ''', (session_date, duration, subject, task_type, focus_rating, session_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    session = conn.execute('SELECT * FROM sessions WHERE id = ?', (session_id,)).fetchone()
    conn.close()
    return render_template('edit.html', session=session)

@app.route('/delete/<int:session_id>')
def delete_session(session_id):
    conn = get_db()
    conn.execute('DELETE FROM sessions WHERE id = ?', (session_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)