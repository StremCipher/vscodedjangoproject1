from django.http import HttpResponse
from django.shortcuts import render
from home.models import Contact


def index(request):
    # return HttpResponse("this is index page")  # to send text
    return render(request, 'index.html')    # to render html file


# def add_data(request):
#     return render(request, 'add data.html')    # to render html file


def add_data(request):
    if request.method == "POST":
        print("ho")
        fname = request.POST['fname']
        lname = request.POST['lname']
        print(fname, lname)
        ins = Contact(fname=fname, lname=lname)
        ins.save()
    return render(request, 'add data.html')
