import sqlite3
from flask import Flask, request, jsonify, g

app = Flask(__name__)
DB_PATH = "books.db"


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    db.execute(
        "CREATE TABLE IF NOT EXISTS books ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "title TEXT NOT NULL,"
        "author TEXT NOT NULL"
        ")"
    )
    db.commit()


@app.before_first_request
def setup():
    init_db()


@app.get("/books")
def list_books():
    db = get_db()
    rows = db.execute("SELECT id, title, author FROM books").fetchall()
    books = [dict(row) for row in rows]
    return jsonify(books)


@app.post("/books")
def create_book():
    data = request.get_json() or {}
    title = data.get("title")
    author = data.get("author")
    if not title or not author:
        return jsonify({"error": "title e author são obrigatórios"}), 400
    db = get_db()
    cur = db.execute(
        "INSERT INTO books (title, author) VALUES (?, ?)",
        (title, author),
    )
    db.commit()
    book_id = cur.lastrowid
    return jsonify({"id": book_id, "title": title, "author": author}), 201


@app.put("/books/<int:book_id>")
def update_book(book_id):
    data = request.get_json() or {}
    db = get_db()
    row = db.execute("SELECT id, title, author FROM books WHERE id = ?", (book_id,)).fetchone()
    if row is None:
        return jsonify({"error": "Livro não encontrado"}), 404

    title = data.get("title", row["title"])
    author = data.get("author", row["author"])
    db.execute(
        "UPDATE books SET title = ?, author = ? WHERE id = ?",
        (title, author, book_id),
    )
    db.commit()
    return jsonify({"id": book_id, "title": title, "author": author})


@app.delete("/books/<int:book_id>")
def delete_book(book_id):
    db = get_db()
    db.execute("DELETE FROM books WHERE id = ?", (book_id,))
    db.commit()
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
