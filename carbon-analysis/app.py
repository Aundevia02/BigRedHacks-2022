from score import getScore
from parse import parseIngredient
from flask import Flask, request, jsonify
import os


app = Flask(__name__)


@app.route("/", methods=['GET'])
def query():
    ingList = request.args.get['ingredients']
    servings = request.args.get['servings']

    ingredients = [parseIngredient(line) for line in ingList.split("\n")]

    carbon_scores = getCarbonScores(ingredients, servings)
    water_scores = getWaterScores(ingredients, servings)
    total_carbon = sum(carbon_scores)
    total_water = sum(water_scores)

    r = {"carbon_scores": carbon_scores, "total_carbon": total_carbon,
         "water_scores": water_scores, "total_water": total_water}

    return jsonify(r)
