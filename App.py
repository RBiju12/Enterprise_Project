from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the Weather App"


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)

