from score import getScores
from parse import parseIngredient
from parseHTML import get_ingredients, get_servings
from flask import Flask, request, jsonify
import os
import openai


app = Flask(__name__)


@app.route("/query", methods=['POST'])
def query():
    html = request.data.decode()
    print(html)
    ingredients = get_ingredients(html)
    servings = int(get_servings(html))

    (ingr_scores, totalCarbonScore, totalWaterScore) = getScores(
        ingredients, servings)

    print(f"total carbon: {totalCarbonScore} \ntotalWater: {totalWaterScore}")

    r = {"scores": ingr_scores, "total_carbon": totalCarbonScore,
         "total_water": totalWaterScore}

    print(r)

    return jsonify(r)


openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL = "text-davinci-002"


@app.route("/gpt", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        line = request.form["recipe-line"]
        response = openai.Completion.create(
            model=MODEL,
            prompt=generate_prompt(line),
            temperature=0.6,
        )
        return response.choices[0]

    result = request.args.get("result")
    return result


def generate_prompt(line):
    return """Provide the amount of an ingredient from a recipe line

Line: 6 teaspoons baking powder (33g)
Amount: 33g
Line: 3/4 cup sugar (150g)
Amount: 150g
Line: 1 1/4 cups milk
Amount: 1 1/4 cups

Line: {}
Amount:""".format(
        line.capitalize()
    )
