from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def recieve_data():
    error = None
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            return "You have logged in"
        else:
            error = 'Invalid username/password'
    return render_template('index.html', error = error)

if __name__ == '__main__':
    app.run(debug=True)