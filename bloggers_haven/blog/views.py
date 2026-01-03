
from django.shortcuts import render, redirect
from .models import Article, Category
from django.contrib.auth.decorators import login_required

def home(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/home.html', {
        'articles': articles,
        'categories': categories
    })

@login_required
def create_blog(request):
    if request.method == 'POST':
        Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            author=request.user
        )
        return redirect('home')
    return render(request, 'blog/create.html')
