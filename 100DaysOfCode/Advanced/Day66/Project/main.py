from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random as rand

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

TopSecretAPIKey = 'Love'

# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random')
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = rand.choice(all_cafes)

    return jsonify(cafe = random_cafe.to_dict())

@app.route('/all')
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes_obj = result.scalars().all()

    all_cafes = []
    for cafe in all_cafes_obj:
        all_cafes.append(cafe.to_dict())
    return jsonify(cafes = all_cafes)

@app.route('/search')
def find_cafe():
    location = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    all_cafes_by_location_obj = result.scalars().all()

    all_cafes_by_location = []
    for cafe in all_cafes_by_location_obj:
        all_cafes_by_location.append(cafe.to_dict())
    if all_cafes_by_location:
        return jsonify(cafes = all_cafes_by_location)
    else:
        return jsonify(error = {"Not Found":'Sorry, we don\'t have a cafe at that location'})

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify({"Success":'Successfully updated the price'})
    else:
        return jsonify(error = {"Not Found":'Sorry, we don\'t have a cafe with that id'})

# HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get('api-key')
    cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe:
        if api_key == TopSecretAPIKey:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify({"Success":'Successfully deleted the cafe'})
        else:
            return jsonify(error = {"Not Found":'Incorrect API Key'})
        
    else:
        return jsonify(error = {"Not Found":'Sorry, we don\'t have a cafe with that id'})


if __name__ == '__main__':
    app.run(debug=True)
