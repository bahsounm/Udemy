from flask import Flask, render_template
import requests, datetime as dt

app = Flask(__name__)

response = requests.get('https://api.npoint.io/674f5423f73deab1e9a7')
all_posts = response.json()
current_date = "{}-{}-{}".format(dt.datetime.now().year,dt.datetime.now().month,dt.datetime.now().day)

@app.route('/')
def home_page():
    return render_template('index.html', posts = all_posts, name = "Bahsoun", date= current_date)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/post/<index>')
def post_page(index):
    requested_post = None
    for post in all_posts:
        print(post)
        if post['id'] == int(index):
            requested_post = post
    return render_template("post.html", post=requested_post, name = "Bahsoun", date= current_date)

@app.route('/contact')
def contact_page():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)