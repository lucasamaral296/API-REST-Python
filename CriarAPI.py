from flask import Flask

app = Flask(__name__)

@app.route("/")   # decorator
def hello_world():  # função
    return "<p>Esta no Ar!</p>"

app.run(debug=True)