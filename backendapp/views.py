from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment, AuthorBio

@login_required
def dashboard(request):
    # your logic here
    return render(request, 'backend/pages/dashboard.html')



# Blog post detail view


# Author bio view
def author_bio(request, author_id):
    author = get_object_or_404(AuthorBio, user_id=author_id)
    return render(request, 'blog/author_bio.html', {'author': author})



def recent_posts(request):
    # Fetch the latest 4 blog posts (or any number you want)
    posts = BlogPost.objects.order_by('-created_at')[:4]
    return render(request, 'your_template.html', {'posts': posts})


