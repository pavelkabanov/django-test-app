from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from django.contrib.auth.models import User
from .forms import PostForm, UserForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def main(request):
    return render(request, 'blog/main.html')

def posts(request):
    post_list = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    paginator = Paginator(post_list, 2)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/posts.html', {'posts': posts})

def users(request):
    user_list = User.objects.all()
    paginator = Paginator(user_list, 2)

    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'blog/users.html', {'users': users})

def comments(request):
    comment_list = Comment.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    paginator = Paginator(comment_list, 2)

    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    return render(request, 'blog/comments.html', {'comments': comments})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.updated_date = timezone.now()
            post.save()
            messages.success(request, "Пост  \'" + post.title + "\' успешно отредактирован.")
            return redirect('posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Юзер  \'" + user.username + "\' успешно отредактирован.")
            return redirect('users')
    else:
        form = UserForm(instance=user)
    return render(request, 'blog/user_edit.html', {'form': form})

def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.updated_date = timezone.now()
            comment.save()
            messages.success(request, "Коммент  \'" + comment.text + "\' успешно отредактирован.")
            return redirect('comments')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    title = post.title
    post.delete()
    messages.success(request, "Пост  \'" + title + "\' успешно удален.")
    return redirect('posts')

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    title = user.username
    user.delete()
    messages.success(request, "Юзер  \'" + title + "\' успешно удален.")
    return redirect('users')

def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    title = comment.text
    comment.delete()
    messages.success(request, "Коммент  \'" + title + "\' успешно удален.")
    return redirect('comments')

