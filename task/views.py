from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "task/index.html")

def pokeball(request):
    return render(request, "landing/pokeball.html")

def lorem(request):
    return render(request, "landing/lorem.html")