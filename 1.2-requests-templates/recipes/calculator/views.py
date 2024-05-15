from django.shortcuts import render, reverse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def food_view(request, food):
    qty = int(request.GET.get('servings', 1))
    dict_product = {}
    for dish in DATA:
        if food == dish:
            Ingredients = DATA[dish]
            for product in Ingredients:
                qty_product = Ingredients[product]
                dict_product[product] = qty_product * qty

    context = {'recipe': dict_product}

    return render(request, 'calculator/index.html', context)
