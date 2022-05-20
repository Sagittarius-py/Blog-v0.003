# from django.views import generic
# from .models import Post, PostImage


# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'


# class PostDetail(generic.DetailView):
#     # model = Post
#     queryset = PostImage.images

#     template_name = 'post_detail.html'


from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login
from django.contrib import messages

from .models import Post, PostImage

from .forms import NewUserForm


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


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})
