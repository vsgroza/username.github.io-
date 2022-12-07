from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Feeback


# Create your views here.



def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


def feedback(request: HttpRequest) -> HttpResponse:
    name = request.GET.get('name')
    email = request.GET.get('email')
    message = request.GET.get('message')

    Feeback.objects.create(name=name, email=email, message=message)

    return render(request, 'index.html')