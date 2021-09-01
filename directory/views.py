import os
import csv
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .models import Company

# Create your views here.
def procesar(request):
    print('funciona aqui')
    filepath = os.path.join(settings.BASE_DIR, 'limpiasindupli2.csv')
    #return HttpResponse(value)
    
    with open(filepath, newline='') as f:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            name_company = row[0]
            rfc = row[1]
            manager_fname = row[2]
            email = row[3]
            web = ''
            if row[4].startswith('www'):
                web = 'http://' + row[4]
            elif row[4].startswith('http'):
                web = row[4]

            address = row[5]
            scope = row[6]
            city = ''
            state = ''
            s = row[7]
            if s != '':
                if s.find(",")!=-1:
                    parts = s.split(',', 1)
                    city = s.split(',', 1)[0]
                    state = s.split(',', 1)[1]
                else:
                    city = s
            description = row[8]
            products = row[9]
            c = Company(
                name_company=name_company, 
                manager_fname=manager_fname, 
                address=address, 
                city=city, 
                state=state, 
                rfc=rfc, 
                scope=scope, 
                email=email, 
                web=web, 
                description=description,
                products=products
            )
            c.save()
            count += 1
            countotal = str(count)
        return HttpResponse("Se agregaron " + countotal + " comañias")
    