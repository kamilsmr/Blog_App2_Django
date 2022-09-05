from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

data = {
    "blogs": [
        {
            "id":1,
            "title":"komple web geliştirme",
            "image":"1.jpg",
            "is_active":True,
            "description":"Çok iyi bir kurs",
        },
        {
            "id":2,
            "title":"Python Kursu",
            "image":"2.jpg",
            "is_active":True,
            "description":"Çok iyi bir kurs",
        },
        {
            "id":3,
            "title":"Django Kursu",
            "image":"3.jpg",
            "is_active":True,
            "description":"Çok iyi bir kurs",
        },
        {
            "id":4,
            "title":"Java",
            "image":"4.jpg",
            "is_active":False,
            "description":"Çok iyi bir kurs",
        },

    ]
}

def index(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, "blog/index.html", context)






def blogs(request):
    return render(request, "blog/blogs.html")



def blog_details(request, id):
    return render(request, "blog/blog-details.html", {
        "id":id
    })