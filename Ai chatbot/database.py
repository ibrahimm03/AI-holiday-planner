import sqlite3
import os # python talking to operating system to save database file

DATABASE = 'chat_history.db' # name of the database file

# create and set up the database
def init_db():
    conn = sqlite3.connect(DATABASE) # open connection to database file
    cursor = conn.cursor() # create a pen to write into the database
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    conn.commit() # saves everything added to database
    conn.close() # closes connection to database

# save a message to the database
def save_message(role, content):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (role, content) VALUES (?, ?)', (role, content))
    conn.commit()
    conn.close()
    # load all messages from the database
def load_messages():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT role, content FROM messages')
    messages = cursor.fetchall()
    conn.close()
    return [{'role': row[0], 'content': row[1]} for row in messages]