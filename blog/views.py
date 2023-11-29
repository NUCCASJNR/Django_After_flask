from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth import get_user


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # Get the fully resolved User object
            user = get_user(request)

            # commit=False means that we don’t want to save the Post model yet – we want to add the author first.
            post = form.save(commit=False)
            post.author = user
            # Finally, we call post.save() to save the post model with the author information.
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    # Get the post we want to edit
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # If we receive a POST request (meaning the user filled out the form and clicked Submit)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # If the form is valid, we can save it
            post = form.save(commit=False)
            # We set the author of the post to the current logged-in user
            post.author = get_user(request)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # If we receive a GET request (meaning the user wants to edit a post)
        # We create a form and populate it with the post data
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})