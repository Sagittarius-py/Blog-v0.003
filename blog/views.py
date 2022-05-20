# from django.views import generic
# from .models import Post, PostImage


# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'


# class PostDetail(generic.DetailView):
#     # model = Post
#     queryset = PostImage.images

#     template_name = 'post_detail.html'


from django.shortcuts import render, get_object_or_404

from .models import Post, PostImage


def PostList(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def PostDetail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'post_detail.html', {
        'post': post,
        'photos': photos
    })
