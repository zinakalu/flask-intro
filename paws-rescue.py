from flask import Flask

app = Flask(__name__)


@app.route("/home")
def home():
    return "<p> Paws Rescue Center </p>"



@app.route("/about")
def about():
    return '<p>We are a non-profit organization working as an animal rescue. We aim to help you connect with the purrfect furbaby for you! The animals you find on our website are rescued and rehabilitated animals. Our mission is to promote the ideology </p>'




if __name__ == "__main__":
    app.run(port=5555, debug=True)