from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import csv

from django.views.decorators.http import require_http_methods


csv_filepath_name = '/home/annett/garage48/backend/data/raw_data/otsus.json'

@require_http_methods(["GET"])
def index(request):
    return HttpResponse("Hello, world. You're at the data index.")

def two(request):
    response = HttpResponse(content_type='text/json')
    #response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    file = open(csv_filepath_name)
    dataReader = csv.reader(file,  delimiter=" ")
    writer = csv.writer(response)
    for row in dataReader:
        writer.writerow(row)
    #for row in dataReader:
    #    writer.writerow(row)

    return response