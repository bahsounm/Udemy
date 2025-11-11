from flask import Flask, render_template, request, flash, redirect, url_for
import requests, datetime as dt, os
from dotenv import load_dotenv
load_dotenv()
import smtplib

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASS = os.environ.get("MY_PASS")


app = Flask(__name__)

response = requests.get('https://api.npoint.io/674f5423f73deab1e9a7')
all_posts = response.json()
current_date = "{}-{}-{}".format(dt.datetime.now().year,dt.datetime.now().month,dt.datetime.now().day)

app.secret_key = os.environ.get("SECRET")

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


@app.route('/form-entry', methods=["POST"])
def recieve_data():
    name = request.form['name']
    email = request.form['email']
    number = request.form['number']
    msg = request.form['msg']
    if request.method == 'POST':
        if name and email and number and msg:
            print(name, email, number, msg)
            flash("Message sent successfully!")
            send_email(name, email, msg)
            return redirect(url_for('contact_page'))
        else:
            return render_template('contact.html', error="Please fill all details")


def send_email(name, email, msg):
    subject = "Message Sent to Bahsoun's Blog"
    body = f"DO NOT REPLY: Hello {name}, this is just a message to let you know your message was successfully recived to \"Bahsoun's Blog\"\nYour message was \"{msg}\""
    msg = f"Subject:{subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(
                from_addr=email,
                to_addrs=MY_EMAIL,
                msg=msg.encode('utf-8')
            )
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == '__main__':
    app.run(debug=True)