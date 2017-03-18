from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/shashank')
def index():
    return 'hi this is shashank'

@app.route('/profile/<username>')
def profile(username):
    return "hi i am %s" % username


if __name__ == "__main__":
    app.run()


