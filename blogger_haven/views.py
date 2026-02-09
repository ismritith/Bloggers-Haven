from django.shortcuts import redirect, render
from blogs.models import Blog, Category
from assignments.models import About
from django.contrib.auth import get_user_model
from .forms import RegistrationForm


# def home(request):
#     categories = Category.objects.all()
#     featured_posts = Blog.objects.filter(is_featured=True)
#     print(featured_posts)
#     context = {
#         'categories': categories,
#     }   
#     return render(request, 'home.html', context)


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status="Published").order_by('-created_at')
    posts = Blog.objects.filter(is_featured=False, status="Published").order_by('-created_at')

    #Feth about us
    try:
        about = About.objects.get()
    except:
        about = None

    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request, 'home.html',  context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)