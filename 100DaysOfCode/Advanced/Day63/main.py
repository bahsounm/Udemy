from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my-library.db"
db.init_app(app)

class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        if request.form['title'] and request.form['author'] and request.form['rating']:
            book = Books(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
            db.session.add(book)
            db.session.commit()
    # retrieve all the books we have and display them
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars().all()
    return render_template('index.html', books =all_books)


@app.route("/add")
def add():
    return render_template('add.html')

@app.route('/edit/<id>', methods=['GET','POST'])
def edit_rating(id):
    book_id = id 
    book_to_update = db.session.execute(
        db.select(Books).where(Books.id == book_id)
    ).scalar_one_or_none()

    if request.method == 'POST':
        print("Hello")
        book_to_update.rating = request.form['new_rating']
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('edit.html', book = book_to_update)

@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    
    book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar_one_or_none()
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

