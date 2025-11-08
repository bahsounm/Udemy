from flask import Flask

app = Flask(__name__) # calls the name of this file to run in by defualt its __main__

@app.route("/") # this is a python decorator, gives additional functionality to functions (see decorator.py), what this line is saying is the url that 
                # hosts our site is at home ie '/' if we add see bye below then if we go to /bye then it foes to another pagfew
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run()