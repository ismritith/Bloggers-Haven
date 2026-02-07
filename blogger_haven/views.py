from django.shortcuts import render
from blogs.models import Blog, Category

# def home(request):
#     categories = Category.objects.all()
#     featured_posts = Blog.objects.filter(is_featured=True)
#     print(featured_posts)
#     context = {
#         'categories': categories,
#     }   
#     return render(request, 'home.html', context)


def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status="Published").order_by('-created_at')
    posts = Blog.objects.filter(is_featured=False, status="Published").order_by('-created_at')
    print(posts)

    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request, 'home.html', context)
