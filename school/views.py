from django.shortcuts import render

def index(request):
    return render(request, "school/index.html")

def home(request):
    return render(request, "school/home.html")

# Create your views here.
