from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category


# Create your views here.


def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True,is_home=True),
        "categories":Category.objects.all()
    }
    return render(request, "blog/index.html", context)






def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories":Category.objects.all()
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