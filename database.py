import sqlite3

def init_db():
    conn = sqlite3.connect("secure.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS encrypted_data (keyword_hash TEXT, encrypted_text TEXT)")
    conn.commit()
    conn.close()

def store_data(encrypted_text, keyword_hash):
    conn = sqlite3.connect("secure.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO encrypted_data VALUES (?, ?)", (keyword_hash, encrypted_text))
    conn.commit()
    conn.close()

def retrieve_data(keyword_hash):
    conn = sqlite3.connect("secure.db")
    cursor = conn.cursor()
    cursor.execute("SELECT encrypted_text FROM encrypted_data WHERE keyword_hash = ?", (keyword_hash,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
