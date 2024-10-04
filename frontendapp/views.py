from django.shortcuts import render, redirect, get_object_or_404
from backendapp.models import Project, Blog, Tag, Comment, QuoteRequest, Category, Tag
from django.views import View
# from backendapp.models import PostDetail
from django.db.models import Count
# import hashlib  
from django.contrib import messages  
# Create your views here.
# from django.http import JsonResponse
# import json
def Home(request):
    projects = Project.objects.all()  
    context = {
        'projects':projects
    }
    return render(request, 'pages/home.html', context)

def about(request):    
    return render(request, 'pages/about.html') 



def blogs(request):
    # Fetch all blog posts that are not deleted
    blogs = Blog.objects.filter(is_deleted=False)  # Only fetch non-deleted blogs
    return render(request, 'pages/blogs.html', {'blogs': blogs})

def blog_post(request, slug):
    blog = get_object_or_404(Blog, slug=slug)  # Adjusted to fetch from Blog model
    categories = Category.objects.all()  # Adjusted for categories
    tags = Tag.objects.all()  # Adjusted for categories
    comments = Comment.objects.all()  # Adjusted for categories

    
    context = {
        'blog': blog,
        'tags': tags,
        'categories': categories,
        'comments': comments,
    }
    return render(request, 'pages/blog_post.html', context)



def comment_detail(request, slug):
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
            return redirect('blog_post', slug=slug)  # Adjust redirect as needed

        messages.error(request, 'Please fill out all required fields.')

    return render(request, 'pages/blog_post.html', {
        'comments': comments,'comment_count': comment_count, 
    })







def contact(request):    
    return render(request, 'pages/contact.html')     
    
def projects(request):  
    projects = Project.objects.all()  
    return render(request, 'pages/projects.html', {'projects': projects})
   
def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'pages/project_detail.html', {'project': project})
    
def services(request):    
    return render(request, 'pages/services.html') 



def request_quote(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company = request.POST.get('company')  # Ensure this matches the field name
        message = request.POST.get('message')

        # Create the QuoteRequest
        QuoteRequest.objects.create(
            name=name,
            email=email,
            phone=phone,
            company=company,  # Ensure this matches the field name
            message=message,
        )

        messages.success(request, "Quote request submitted successfully!")
        return redirect('projects')  # Change to your desired redirect URL

    return render(request, 'pages/home.html')  # Ensure you have the correct template



