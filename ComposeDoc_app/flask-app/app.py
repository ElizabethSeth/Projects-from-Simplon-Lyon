import os
from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(mongo_uri)
db = client.db_listing
listings_collection = db.listing_sql


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search_amenities', methods=['POST'])
def search_amenities():
    data = request.get_json()
    amenities = data.get('amenities')

    if not amenities:
        return jsonify({"error": "Amenities are required"}), 400

    query = {"amenities": {"$in": amenities}}
    matching_listings = listings_collection.find(
        query, {"listing_url": 1, "address.market": 1, "_id": 0})
    result = [{"market": listing["address"]["market"],
               "listing_url": listing["listing_url"]} for listing in matching_listings]

    return jsonify({"matching_listings": result})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
