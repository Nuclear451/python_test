from django.shortcuts import render

from .models import Post


# Create your views here.

def post_list(request):
    posts = Post.objects.order_by('post_date')
    return render(request, 'web/index.html', {'posts': posts})


