from score import getScores
from parse import parseIngredient
from parseHTML import get_ingredients, get_servings
from flask import Flask, request, jsonify
import os


app = Flask(__name__)


@app.route("/query", methods=['GET'])
def query():
    html = request.args.get['ingredients']

    ingredients = get_ingredients(html)
    servings = get_servings(html)

    (ingr_scores, totalCarbonScore, totalWaterScore) = getScores(
        ingredients, servings)

    r = {"scores": ingr_scores, "total_carbon": totalCarbonScore,
         "total_water": totalWaterScore}

    return jsonify(r)
