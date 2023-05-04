from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello World </h1>"

@app.route('/<string:username>')
def user(username):
    return f'<h3>Profile for {username} </h3>'







if __name__ == "__main__":
    app.run(port=5555, debug=True)