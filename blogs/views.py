# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Blog

# # Create your views here.

# def posts_by_category(request, category_id):
#     # FETCH THE POSTS THAT BELONGS TO THE CATEGORY WITH THE GIVEN ID
#     posts = Blog.objects.filter(status='Published', category=category_id)
#     context = {
#         'posts': posts,

#     }
#     return render(request, 'posts_by_category.html', context)

from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category

def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='Published', category_id=category_id) 

    # Use try except when you want to do custom action when the category does not exist, for example redirecting the users to homepage.
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except :
        # redirect the users to homepage
        # return redirect('home')
    # Use get_object_or_404 when you want to show 404 error page if the category does not exist, instead of redirecting to homepage.
    category = get_object_or_404(Category, pk=category_id)


    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'single_blog': single_blog,
    }
    return render(request, 'blogs.html', context)