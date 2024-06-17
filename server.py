from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)


##define routes
@app.route("/")
@app.route("/index")
##define functions that will return sth for the routes
def index():
    return render_template("index.html")


@app.route("/weather")
def get_weather():
    city = request.args.get("city")
    weather_data = get_current_weather(city)
    ## now we want to send the data to the template; these will be used in the weather.html template
    ## title, status, etc. we fetch the data from the json obj returned from get API call, then return them to weather.html
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
    )


## localhost port 8000
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
