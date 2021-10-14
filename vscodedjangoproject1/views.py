from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("this is index page")  # to send text
    return render(request, 'index.html')    # to render html file


def about(request):
    return HttpResponse("this is about page")
