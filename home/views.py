"""
Views file implements the render function to render templates and return HTTP responses.
Index returns a rendered template for a welcome message.
About returns a rendered template for the about page.
"""
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')
def about(request):
    return render(request, 'home/about.html')
