from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    # return HttpResponse("Hello, world. This is index() in trader-app/views.py.")
    return render(request, "index.html", {"tmp": 12})