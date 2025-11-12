from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import requests

# CREATE DB
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    ranking: Mapped[int] = mapped_column(nullable=False)
    review: Mapped[str] = mapped_column(nullable=False)
    img_url: Mapped[str] = mapped_column(nullable=False)

class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    year = StringField('Year of Release', validators=[DataRequired()])
    description = StringField('Description of the Movie', validators=[DataRequired()])
    rating = StringField('Movie Rating', validators=[DataRequired()])
    ranking = StringField('Movie Ranking', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    img_url = StringField('Submit Movie Poster URL', validators=[DataRequired(), URL()])
    submit = SubmitField('Submit')

class RateMovieForm(FlaskForm):
    rating = StringField('Movie Rating', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit')

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    all_books = result.scalars().all()
    return render_template("index.html", books = all_books)

@app.route("/add-movie", methods=['GET','POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie = Movie(title=form.title.data, year=form.year.data, description=form.description.data, rating=form.rating.data, ranking=form.ranking.data, review=form.review.data, img_url=form.img_url.data)
        db.session.add(movie)
        db.session.commit()
        recompute_rankings()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar_one_or_none()
    db.session.delete(movie_to_delete)
    db.session.commit()
    recompute_rankings()
    return redirect(url_for('home'))

@app.route('/update/<id>', methods=['GET','POST'])
def update(id):
    movie_id = id
    form = RateMovieForm()
    if form.validate_on_submit():
        movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar_one_or_none()
        if form.rating.data:
            movie_to_update.rating = form.rating.data
        if form.review.data:
            if form.review.data != 'same':
                movie_to_update.review = form.review.data
        db.session.commit()
        recompute_rankings()
        return redirect(url_for('home'))
    return render_template('edit.html', form = form)

def recompute_rankings():
    # Order by rating DESC, then title ASC for stable ordering
    movies = db.session.execute(
        db.select(Movie).order_by(Movie.rating.desc(), Movie.title.asc())
    ).scalars().all()

    for idx, m in enumerate(movies, start=1):
        m.ranking = idx


    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
