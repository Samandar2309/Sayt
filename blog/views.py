from django.shortcuts import render, get_object_or_404
from .models import Post1, Home, Category, Tags, Contact


# Create your views here.
def index(request):
    posts = Post1.objects.all().order_by('id')[:3]
    home = Home.objects.all().order_by('-id')[:3]
    category = Category.objects.all().order_by('-id')[:10]
    tag = Tags.objects.all()
    context = {
        'posts': posts,
        'home': home,
        'category': category,
        'tags': tag,
    }
    return render(request, 'index.html', context)


def contact(request):
    posts = Contact.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'contact.html', context)


def detail(request, pk):
    post = get_object_or_404(Post1, id=pk)
    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)
