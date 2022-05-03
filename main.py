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

@app.route("/gravity")
def gravity():
    gravity = request.args.get("range")
    lesser = gravity.split("-")[0]
    greater = gravity.split("-")[1]
    star_data = []
    for star in data:
        if star["gravity"] > lesser:
            if star["gravity"] < greater:
                star_data.append(star)
    return jsonify({
        "data": star_data,
    }), 200

@app.route("/mass")
def mass():
    mass = request.args.get("range")
    lesser = mass.split("-")[0]
    greater = mass.split("-")[1]
    star_data = []
    for star in data:
        if star["mass"] > lesser:
            if star["mass"] < greater:
                star_data.append(star)
    return jsonify({
        "data": star_data,
    }), 200

@app.route("/radius")
def radius():
    radius = request.args.get("range")
    lesser = radius.split("-")[0]
    greater = radius.split("-")[1]
    star_data = []
    for star in data:
        if star["radius"] > lesser:
            if star["radius"] < greater:
                star_data.append(star)
    return jsonify({
        "data": star_data,
    }), 200

if __name__ == "__main__":
    app.run()