
from django.shortcuts import render
from django.utils import timezone

from .forms import PostForm

from .models import Post


# Create your views here.

def post_list(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        print(request.method)
        if form.is_valid():
            print(2)
            post = form.save(commit=False)
            post.post_date = timezone.now()
            post.save()

    print(0)
    posts = Post.objects.order_by('post_date')
    return render(request, 'web/index.html', {'posts': posts})


def post_new(request):
    form = PostForm()
    return render(request, 'web/index.html', {'form': form})
