from flask import Flask, render_template, request, redirect, url_for, flash
import uuid, json
from config import get_redis_connection

app = Flask(__name__)
app.secret_key = "supersecretkey"  # cambia por algo seguro
db = get_redis_connection()

# ---------- Helpers ----------
def get_books():
    books = []
    for key in db.scan_iter("libro:*"):
        book = json.loads(db.get(key))
        book["id"] = key.split(":")[1]
        books.append(book)
    return books

def get_book(book_id):
    data = db.get(f"libro:{book_id}")
    return json.loads(data) if data else None

# ---------- Rutas ----------
@app.route("/")
def index():
    return render_template("index.html", books=get_books())

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        genre = request.form["genre"].strip()
        status = request.form["status"].strip()

        if not title or not author:
            flash("El título y autor son obligatorios", "danger")
            return redirect(url_for("add"))

        book_id = str(uuid.uuid4())
        db.set(f"libro:{book_id}", json.dumps({
            "title": title,
            "author": author,
            "genre": genre,
            "status": status
        }))
        flash("Libro agregado con éxito", "success")
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/edit/<book_id>", methods=["GET", "POST"])
def edit(book_id):
    book = get_book(book_id)
    if not book:
        flash("Libro no encontrado", "danger")
        return redirect(url_for("index"))

    if request.method == "POST":
        book["title"] = request.form["title"].strip()
        book["author"] = request.form["author"].strip()
        book["genre"] = request.form["genre"].strip()
        book["status"] = request.form["status"].strip()

        db.set(f"libro:{book_id}", json.dumps(book))
        flash("Libro actualizado con éxito", "success")
        return redirect(url_for("index"))

    return render_template("edit.html", book=book, book_id=book_id)

@app.route("/delete/<book_id>")
def delete(book_id):
    db.delete(f"libro:{book_id}")
    flash("Libro eliminado", "warning")
    return redirect(url_for("index"))

@app.route("/search", methods=["GET", "POST"])
def search():
    results = []
    if request.method == "POST":
        query = request.form["query"].lower()
        books = get_books()
        results = [b for b in books if query in b["title"].lower() 
                                  or query in b["author"].lower() 
                                  or query in b["genre"].lower()]
    return render_template("search.html", results=results)
