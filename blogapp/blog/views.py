from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("home page")


def blogs(request):
    return HttpResponse("blog page")



def blog_details(request):
    return HttpResponse("blog details" + str(id))