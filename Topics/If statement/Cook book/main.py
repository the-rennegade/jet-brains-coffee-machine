ingredients = {
    "tomato": ["pasta", "ratatouille", "omelette"],
    "basil": ["pasta"],
    "garlic": ["pasta", "ratatouille"],
    "salt": ["pasta", "apple pie", "ratatouille", "chocolate cake", "omelette"],
    "pasta": ["pasta"],
    "olive oil": ["pasta", "ratatouille"],
    "apple": ["apple pie"],
    "sugar": ["apple pie", "chocolate cake"],
    "cinnamon": ["apple pie"],
    "flour": ["apple pie", "chocolate cake"],
    "egg": ["apple pie", "omelette"],
    "butter": ["apple pie", "chocolate cake"],
    "aubergine": ["ratatouille"],
    "carrot": ["ratatouille"],
    "onion": ["ratatouille"],
    "pepper": ["ratatouille", "omelette"],
    "chocolate": ["chocolate cake"],
    "coffee": ["chocolate cake"],
    "milk": ["omelette"],
    "bacon": ["omelette"],
}



ingredient = input()

recipes = ingredients[ingredient]

for recipe in recipes:
    print(f'{recipe} time!')
