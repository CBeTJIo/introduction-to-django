from django.shortcuts import render, reverse


def omlet(request):
    qty = int(request.GET.get('servings', 1))

    context = {
        'recipe': {
            'яйца, шт': f'{qty * 2}',
            'молоко, л': f'{qty * 0.1}',
            'соль, ч.л.': f'{qty * 0.5}',
        },
    }

    return render(request, 'calculator/index.html', context)

def pasta(request):
    qty = int(request.GET.get('servings', 1))

    context = {
        'recipe': {
            'макароны, г': f'{qty * 0.3}',
            'сыр, г': f'{qty * 0.05}',
        },
    }

    return render(request, 'calculator/index.html', context)

def buter(request):
    qty = int(request.GET.get('servings', 1))

    context = {
        'recipe': {
            'хлеб, ломтик': f'{qty * 1}',
            'колбаса, ломтик': f'{qty * 1}',
            'сыр, ломтик': f'{qty * 1}',
            'помидор, ломтик': f'{qty * 1}',
        },
    }

    return render(request, 'calculator/index.html', context)



def home_view(request):
    pages = {
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('buter')
    }

    context = {
        'pages': pages
    }
    return render(request, 'calculator/index.html', context)