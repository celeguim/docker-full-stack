import json
import os
import requests

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# landing page that will display all the books in our database
# This function operate on the Read operation.
@app.route('/')
@app.route('/books')
def show_books():
    print('show_books')
    response = requests.get(url="http://0.0.0.0:8081/api/books",)
    # return render_template("books.html", books=books)
    books = json.loads(response.content)
    return render_template("books.html", books=books)


# This will let us Create a new book and save it in our database
@app.route('/books/new/', methods=['GET', 'POST'])
def new_book():
    if request.method == 'POST':
        # new_book = Book(title=request.form['name'], author=request.form['author'], genre=request.form['genre'])
        return redirect(url_for('show_books'))
    else:
        return render_template('newBook.html')


# This will let us Update our books and save it in our database
@app.route("/books/<int:book_id>/edit/", methods=['GET', 'POST'])
def edit_book(book_id):
    # editedBook = session.query(Book).filter_by(id=book_id).one()
    editedBook = None

    if request.method == 'POST':
        if request.form['name']:
            # editedBook.title = request.form['name']
            return redirect(url_for('showBooks'))
    else:
        return render_template('editBook.html', book=editedBook)


# This will let us Delete our book
@app.route('/books/<int:book_id>/delete/', methods=['GET', 'POST'])
def delete_book(book_id):
    if request.method == 'POST' and request.form.get('submit') == "submit":
        response = requests.delete(url=os.path.join("http://0.0.0.0:8081/api/books/delete/", str(book_id)))
        return redirect(url_for('show_books'))
    elif request.method == 'GET':
        response = requests.get(url=os.path.join("http://0.0.0.0:8081/api/books/find", str(book_id)))
        book_to_delete = json.loads(response.content)
        return render_template('deleteBook.html', book=book_to_delete)
    elif request.form.get('cancel') == "cancel":
        return redirect(url_for('show_books'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4996)
