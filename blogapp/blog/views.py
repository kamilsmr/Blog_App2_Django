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
            "is_home":False,
            "description":"Çok iyi bir kurs",
        },
        {
            "id":2,
            "title":"Python Kursu",
            "image":"2.jpg",
            "is_active":True,
            "is_home":True,
            "description":"Çok iyi bir kurs",
        },
        {
            "id":3,
            "title":"Django Kursu",
            "image":"3.jpg",
            "is_active":False,
            "is_home":True,
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
    context = {
        "blogs": data["blogs"]
    }
    return render(request, "blog/blogs.html", context)



def blog_details(request, id):
    # blogs = data["blogs"]
    # selectedBlog = None

    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBlog = blog
    blogs = data["blogs"]

    selectedBlog = [blog for blog in blogs if blog["id"]==id][0]


    return render(request, "blog/blog-details.html", {
        "blog": selectedBlog
    })