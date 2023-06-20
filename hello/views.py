from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Movies

def index(request):
     return HttpResponse("<h1>Hello</h1>", content_type="text/plain",
                         charset="utf-8")

def about(request, name, age):
     return HttpResponse(f"""
         <h2>О пользователе</h2>
         <p>Имя: {name}</p>
         <p>Возраст: {age}</p>
     """)

def contact(request):
    return HttpResponse('<h2>Контакты</h2>')

def queries(request):
    return render(request, 'hello/queries.html')

def query1(request):
    query1 = Movies.objects.all()
    return render(request, 'hello/queries.html', {'query1':query1})

def query2(request):
    query2 = Movies.objects.filter(year__range=(1980, 1990))
    return render(request, 'hello/queries.html', {'query2':query2})

def query3(request):
    query3 = Movies.objects.filter(name__contains="o")
    return render(request, 'hello/queries.html', {'query3':query3})
