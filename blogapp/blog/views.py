from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog

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
        "blogs": Blog.objects.filter(is_active=True,is_home=True)
    }
    return render(request, "blog/index.html", context)






def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True)
    }
    return render(request, "blog/blogs.html", context)



def blog_details(request, slug):
    # blogs = data["blogs"]
    # selectedBlog = None

    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBlog = blog
    blog = Blog.objects.get(slug=slug)


    return render(request, "blog/blog-details.html", {
        "blog": blog
    })