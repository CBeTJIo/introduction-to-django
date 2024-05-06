from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


file_name = # ссылка на файл data-398-2018-08-30.csv

list_of_street = []
with open(f'{file_name}', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        d = {'Name': row.get('Name'), 'Street': row.get('Street'), 'District': row.get('District')}
        list_of_street.append(d)


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(list_of_street, 10)
    page = paginator.get_page(page_number)
    station_list = paginator.page(page_number)
    context = {
        'bus_stations': station_list,
        'page': page
    }

    return render(request, 'stations/index.html', context)
