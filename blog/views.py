<<<<<<< HEAD
from django.shortcuts import render
=======
from django.shortcuts import render, get_object_or_404
>>>>>>> 21749ba0955398a32233616d838bd2c958c9e95d
from .models import Post
from django.utils import timezone

def post_list(request):
# <<<<<<< HEAD
#     # looks in templates 
#     posts = Post.object.filter(published_date__lte=timezone.now()).order_by("published_date")
#     return render(request, 'blog/post_list.html', {})
# =======
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
# >>>>>>> 21749ba0955398a32233616d838bd2c958c9e95d

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})
