from sets_categories_data import (ALCOHOLS)
def clean_ingredients(dish_name, dish_ingredients):
    ingredientes=set(dish_ingredients)

    return (dish_name,ingredientes)

def check_drinks(drink_name, drink_ingredients):
    for drink_ingredient in drink_ingredients
        if drink_ingredients in ALCOHOLS
            return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"
