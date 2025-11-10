from flask import Flask, render_template
import random as rand
import datetime as dt
import requests

app = Flask(__name__)

@app.route("/")
def home_page():
    random_number = rand.randint(0,10)
    current_year = dt.datetime.now().year
    # need to pass a name for what we want to pass
    return render_template('index.html', num=random_number, year=current_year)

@app.route("/guess/<name>")
def challenge1(name):
    response1 = requests.get("https://api.genderize.io", params={'name': name})
    response1.raise_for_status()
    
    response2 = requests.get('https://api.agify.io', params={'name': name})
    response2.raise_for_status()

    theorized_gender = response1.json()["gender"]
    theorized_age = response2.json()["age"]

    return render_template('guess.html', name=name, age = theorized_age, gender = theorized_gender)

@app.route("/blog")
def get_blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blog.html", posts = all_posts)

if __name__ == '__main__':
    app.run(debug=True)