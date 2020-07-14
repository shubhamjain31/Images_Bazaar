from django.http import HttpResponse
from django.shortcuts import render, redirect
from App.models import *


def show_about_page(request):
    return render(request, "aboutus.html")


def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    print(images)
    data = {'images': images, 'cats': cats}
    return render(request, "index.html", data)


def show_category_page(request, cid):
    print(cid)
    cats = Category.objects.all()
    category = Category.objects.get(pk=cid)
    images = Image.objects.filter(cat=category)
    data = {'images': images, 'cats': cats}
    return render(request, "index.html", data)

def home(request):
    return redirect('/home')