from dotenv import load_dotenv
from flask import Flask, request, jsonify
from helpers import scraper

load_dotenv()

app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False


@app.get("/weather")
def get_weather():
    location = request.args.get("location")
    lang = request.args.get("lang")

    if not location:
        return jsonify({"message": "invalid location"}), 400

    if not lang:
        data = scraper.scrape(location)
    else:
        data = scraper.scrape(location, lang)

    if not data:
        return jsonify({"message": "No results for the params submitted"}), 404

    return jsonify({"message": "success", "data": data}), 200
