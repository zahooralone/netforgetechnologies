from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
# from .models import BlogPost, Comment, AuthorBio

@login_required
def dashboard(request):
    # your logic here
    return render(request, 'backend/pages/dashboard.html')



# Blog post detail view


# # Author bio view
# def author_bio(request, author_id):
#     authors = AuthorBio.objects.all()  # Fetch all authors
#     posts = BlogPost.objects.filter(authors=authors).order_by('-created_at')  # Fetch posts by this author
#     return render(request, 'pages/blog_post.html', {'authors': authors, 'posts': posts})



# def recent_posts(request):
#     # Fetch the latest 4 blog posts (or any number you want)
#     posts = BlogPost.objects.order_by('-created_at')[:4]
#     return render(request, 'pages/blogs.html', {'posts': posts})


