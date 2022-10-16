from score import getScores
from parse import parseIngredient
from parseHTML import get_ingredients, get_servings
from flask import Flask, request, jsonify
import os


app = Flask(__name__)


@app.route("/query", methods=['POST'])
def query():
    html = request.data.decode()
    # print(html)
    ingredients = get_ingredients(html)
    servings = int(get_servings(html))
    print(servings)

    (ingr_scores, totalCarbonScore, totalWaterScore) = getScores(
        ingredients, servings)

    print(f"total carbon: {totalCarbonScore} \ntotalWater: {totalWaterScore}")

    r = {"scores": ingr_scores, "total_carbon": totalCarbonScore,
         "total_water": totalWaterScore}

    return jsonify(r)
