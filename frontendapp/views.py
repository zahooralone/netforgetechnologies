from django.shortcuts import render, redirect, get_object_or_404
from backendapp.models import Project, Portfolio, Card,Blog, Tag, Comment
from django.views import View
from backendapp.models import PostDetail
from django.db.models import Count
# import hashlib  
from django.contrib import messages  
# Create your views here.
def Home(request):
    return render(request, 'pages/home.html')

def about(request):    
    return render(request, 'pages/about.html') 



def blogs(request):
    # Fetch all blog posts
    blogs = Blog.objects.all()
    return render(request, 'pages/blogs.html', {'blogs': blogs})

def blog_post(request, id):
    post = get_object_or_404(PostDetail, id=id) # or whatever filtering is necessary
    tags = post.tags.all() # or whatever filtering is necessary
    categories = post.categories.annotate(post_count=Count('post_details'))
    comments = Comment.objects.all()  # Fetch all comments
    context = {
        'post': post, 
        'tags':tags, 
        'categories': categories,
        'comments': comments,
    }
    return render(request, 'pages/blog_post.html', context)



def comment_detail(request, id):
    comments = Comment.objects.all()  # Fetch all comments
    comment_count = comments.count()  # Count the comments
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        content = request.POST.get('content')

        if name and email and content:  # Validate required fields
            comment = Comment(name=name, email=email, website=website, content=content)
            comment.save()  # Save comment to the database
            messages.success(request, 'Your comment has been posted successfully!')
            return redirect('blog_post', id=id)  # Adjust redirect as needed

        messages.error(request, 'Please fill out all required fields.')

    return render(request, 'pages/blog_post.html', {
        'comments': comments,'comment_count': comment_count, 
    })



# def blog_post(request, slug): 
#     post = get_object_or_404(BlogPost, slug=slug)
#     comments = post.comments.all()

#     if request.method == 'POST':
#         # Process the comment form here
#         author = request.POST.get('author')
#         email = request.POST.get('email')
#         content = request.POST.get('content')
#         comments = Comment.objects.create(post=post, author=author, email=email, content=content)
#         return redirect('blog_post', slug=post.slug)   
#     return render(request, 'pages/blog_post.html', {'post': post, 'comments': comments})

def contact(request):    
    return render(request, 'pages/contact.html')     
    
def projects(request):  
    cards = Card.objects.all()  
    return render(request, 'pages/projects.html', {'cards': cards})
   
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'pages/project_detail.html', {'project': project})
    
def services(request):    
    return render(request, 'pages/services.html') 


def viewmore(request):  
    portfolio = Portfolio.objects.all()
    project = Project.objects.all()
    return render(request, 'pages/viewmore.html', {'projects': project,  'portfolio': portfolio}) 


def dashboard(request):    
    return render(request, 'backend/pages/dashboard.html') 




