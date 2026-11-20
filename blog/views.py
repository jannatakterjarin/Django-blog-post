from django.shortcuts import render, redirect
from .models import BlogPost


def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        BlogPost.objects.create(
            title=title,
            description=description
        )

        return redirect('create_post')

    return render(request, 'blog/create_post.html')

# Create your views here.
def post_list(request):
    posts = BlogPost.objects.all()

    return render(request, 'blog/post_list.html', {
        'posts': posts
    })
