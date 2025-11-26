from flask import Flask, jsonify, request
import secrets
import sqlite3
import os

DB_PATH = os.environ.get("DB_PATH", "honeytokens.db")

#inicializar DB
if not os.path.exists(DB_PATH):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("CREATE TABLE issued_tokens (id TEXT PRIMARY KEY)")
    c.execute("CREATE TABLE access_logs (id INTEGER PRIMARY KEY AUTOINCREMENT, token TEXT)")
    conn.commit()
    conn.close()

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/new")
def new_token():
    token = secrets.token_urlsafe(8)

    conn = get_db()
    print(f"Token creado: {token}")
    conn.execute("INSERT INTO issued_tokens (id) VALUES (?)", (token,))
    conn.commit()
    conn.close()
    
    url = f"{request.host_url}resource/{token}"

    return jsonify({"id": token, "url": url})

@app.get("/resource/<token>")
def access_resource(token: str):
    # Extrae el prefijo del token asi que podes consultar por token.jpg o token.svg y solo se va a tomar en cuenta _token_ y no su file type (si es que lo tiene)
    if "." in token:
        token = token.split(".", 1)[0]

    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM issued_tokens WHERE id = ?", (token,))
    exists = cur.fetchone()

    if exists:
        print(f"Acceso de token: {token}")
        conn.execute("INSERT INTO access_logs (token) VALUES (?)", (token,))
        conn.commit()

    conn.close()
    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

