from flask import Flask, render_template, request
from weather import get_current_weather

app = Flask(__name__)


##define routes
@app.route("/")
@app.route("/index")
##define functions that will return sth for the routes
def index():
    return "Hello World"


## localhost port 8000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
