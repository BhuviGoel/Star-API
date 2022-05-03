from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
    }), 200

@app.route("/star")
def name():
    name = request.args.get("name")
    star_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": star_data,
    }), 200

# @app.route("/type")
# def star_type():
#     star_type = request.args.get("star_type")
#     star_data = []
#     for star in data:
#         if star["star_type"] == star_type:
#             star_data.append(star)
#     return jsonify({
#         "data": star_data,
#         "message": "success"
#     }), 200

if __name__ == "__main__":
    app.run()