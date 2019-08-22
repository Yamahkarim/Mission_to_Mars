#################################################
# Import Dependencies
#################################################
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.web_scrape()
    mars.update({}, mars_data, upsert=True)
    return render_template("scrape.html", mars=mars)


if __name__ == "__main__":
    app.run(debug=True)
