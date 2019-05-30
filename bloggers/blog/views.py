from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def post(request):
	posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
	return render(request, 'blog/post.html', {'posts': posts})

def detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/detail.html', {'post': post})

@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/edit_post.html', {'form': form})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})

@login_required
def draft_post(request):
	posts = Post.objects.filter(pub_date__isnull=True).order_by('create_date')
	return render(request, 'blog/draft_post.html', {'posts': posts})

@login_required
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('detail', pk=pk)

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post')