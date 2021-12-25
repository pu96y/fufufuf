from django.shortcuts import render
from django.http import HttpResponse

def glav(request):
    return render(request, 'main/glav.html')


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')