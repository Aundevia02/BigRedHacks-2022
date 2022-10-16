import re


def test_get_ingredients():
    with open("data/test.txt", "r") as text_file:
        data = text_file.read()

        print(get_ingredients(data))
        print(get_servings(data))


def get_servings(html):

    idx = html.find('Servings')

    cur_char = html[idx]
    while not cur_char.isdigit():
        idx += 1
        cur_char = html[idx]
    next_char = html[idx + 1]
    if next_char.isdigit():
        return int(cur_char + next_char)
    return cur_char


def get_ingredients(html):
    match = '<span data-ingredient-quantity="true">(.*)<\/span>.*<span data-ingredient-unit="true">(.*)<\/span>.*<span data-ingredient-name="true">(.*)<\/span>'

    matches = re.findall(match, html)
    return matches


test_get_ingredients()
