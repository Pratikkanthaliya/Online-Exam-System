from django.shortcuts import render

def index(request):
    res = render(request, "index.html")
    return res