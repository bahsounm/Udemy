# import sqlite3

# # this is how we establish a connection to our database, if it doesnt exist then one will be created
# db = sqlite3.connect("books-collection.db")

# # now we ned a cursor which will control our database
# cursor = db.cursor()

# # craeting our table
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# # adding items to our table
# # cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# # db.commit()

# # there is a better python way we can add to our database 

# #===================================================================================================================

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)

with app.app_context():
    # Create tables if missing
    db.create_all()

    # Add a new book record
    # book = Books(title="Harry Potter", author="J. K. Rowling", rating=9.3)
    # db.session.add(book)
    # db.session.commit()  # 'book.id' is now available

    # ---- READ ALL RECORDS ----
    # result = db.session.execute(db.select(Books).order_by(Books.title))
    # all_books = result.scalars().all()
    # print(all_books)

    # ---- READ ONE RECORD ----
    # hp = db.session.execute(
    #     db.select(Books).where(Books.title == "Harry Potter")
    # ).scalar_one_or_none()
    # print(hp)

    # ---- UPDATE BY QUERY (e.g., by title) ----
    # book_to_update = db.session.execute(
    #     db.select(Books).where(Books.title == "Harry Potter")
    # ).scalar_one_or_none()

    # if book_to_update:
    #     book_to_update.title = "Harry Potter and the Chamber of Secrets"
    #     db.session.commit()

    # ---- UPDATE BY PRIMARY KEY ----
    # book_id = book.id  # or set any valid id you want to update
    # book_to_update = db.session.execute(
    #     db.select(Books).where(Books.id == book_id)
    # ).scalar_one_or_none()
    # # Alternatively (inside a request context): book_to_update = db.get_or_404(Books, book_id)

    # if book_to_update:
    #     book_to_update.title = "Harry Potter and the Goblet of Fire"
    #     db.session.commit()

    # ---- DELETE BY PRIMARY KEY ----
    # book_to_delete = db.session.execute(
    #     db.select(Books).where(Books.id == book_id)
    # ).scalar_one_or_none()
    # # Alternatively (inside a request context): book_to_delete = db.get_or_404(Books, book_id)

    # if book_to_delete:
    #     db.session.delete(book_to_delete)
    #     db.session.commit()



