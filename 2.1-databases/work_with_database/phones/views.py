from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):

    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    # template = 'catalog.html'
    # filter = request.GET.get("sort")
    # if filter == "name":
    #     catalog_objects = Phone.objects.order_by("name")
    # elif filter == "min_price":
    #     catalog_objects = Phone.objects.order_by("price")
    # if filter == "max_price":
    #     catalog_objects = Phone.objects.order_by("price", reversed) # check 'reversed' mb need 'reverse()'
    # else:
    #     catalog_objects = Phone.objects.all()

    catalog_objects = Phone.objects.all()

    list_obj = []
    for lc in catalog_objects:
        new_dict = {
            'name': lc.name, 'price': lc.price, 'image': lc.image,
            'release_date': lc.release_date, 'lte_exists': lc.lte_exists, 'slug': lc.slug
        }
        list_obj.append(new_dict)

    filter = request.GET.get('sort')
    if filter == 'name':
        sorted_list = sorted(list_obj, key=lambda x: x['name'])
    elif filter == 'min_price':
        sorted_list = sorted(list_obj, key=lambda x: x['price'])
    elif filter == 'max_price':
        sorted_list = sorted(list_obj, key=lambda x: x['price'], reverse=True)
    else:
        sorted_list = list_obj

    context = {
        'phones': sorted_list
    }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_objects = Phone.objects.filter(slug=slug)
    for phone in phone_objects:
        context = {
            'phone': {
                'name': phone.name, 'price': phone.price, 'image': phone.image,
                'release_date': phone.release_date, 'lte_exists': phone.lte_exists, 'slug': phone.slug
            }

        }

    return render(request, template, context)
