import os
import csv
import random
from django.utils import timezone
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .models import Company

# Create your views here.
def list_companies(request):
    #companies = Company.objects.all().filter(
    #    published_date__lte=timezone.now()).order_by('published_date')
    items = list(Company.objects.all())
    companies = random.sample(items, 5000)
    numero = Company.objects.all().count()
    print(numero)
    return render(request, 'directory/list_companies.amp.html', {'companies': companies,})

def compani(request, num):
    company = Company.objects.get(id=num)
    return render(request, 'directory/company.amp.html', {'company': company,})

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
    