import sqlite3
DB_PATH = "../../db/users.db"

def create_table(conn):
    conn.cursor().execute('''CREATE TABLE IF NOT EXISTS users
              (id UNIQUE, username text, firstname text , lastname text)''')
    
    
def insert_id(info):
#    conn = set_connection()
    with set_connection() as conn:
        conn.cursor().execute('INSERT OR IGNORE INTO users VALUES (:id, :username, :first, :last)',
                  {'id':info.chat.id,'username':info.from_user.username,
                   'first':info.from_user.first_name,'last':info.from_user.last_name})
    
    
def search_id(chat_id):
    conn = set_connection()
    result = conn.cursor().execute('''SELECT * FROM users WHERE id = :id''', {"id":chat_id}).fetchone()
    conn.close()
    return result


def set_connection(db_path = DB_PATH):
    db_conn = sqlite3.connect(db_path)
    return db_conn
