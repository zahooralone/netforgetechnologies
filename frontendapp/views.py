from django.shortcuts import render, redirect, get_object_or_404
from backendapp.models import Project, Blog, Tag, Comment, QuoteRequest, Category, Tag, Service
from django.views import View
# from backendapp.models import PostDetail
from django.db.models import Count
# import hashlib  

from django.contrib import messages  
# Create your views here.
# from django.http import JsonResponse
# import json
from .utils import send_quote_notification  # Import the notification function
from .utils import send_comment_notification  # Import the notification function
from django.core.mail import send_mail
from django.conf import settings


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



def COMMENT(request, slug):
    comments = Comment.objects.all()  # Fetch all comments
    comment_count = comments.count()  # Count the comments

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        content = request.POST.get('content')

        # Validate required fields
        if name and email and content:  # Add more validation as needed
            # Create and save the comment
            comment = Comment(
                name=name,
                email=email,
                website=website,
                content=content,
            )
            comment.save()  # Ensure save() is called as a method

            # Prepare comment details for notification
            comment_details = f"Name: {name}\nEmail: {email}\nWebsite: {website}\nContent: {content}"

            # Send the email notification
            send_comment_notification(name, email, website, comment_details, settings.TEAM_EMAIL)

            messages.success(request, 'Your comment has been posted successfully!')
            return redirect('blog_post', slug=slug)  # Adjust redirect as needed

        else:
            messages.error(request, 'Please fill out all required fields.')

    return render(request, 'pages/blog_post.html', {
        'comments': comments,
        'comment_count': comment_count,
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
    services = Service.objects.all() 
    return render(request, 'pages/services.html', {'services':services}) 


def data_strategy(request):  
    return render(request, 'pages/data_strategy.html') 




def request_quote(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company = request.POST.get('company')
        message = request.POST.get('message')



        quote_details = f"Name :{name}\nEmail :{email}\nPhone Number :{phone}\nCompany Name :{company}\nMessage :{message}"

        # Save the QuoteRequest
        quote = QuoteRequest(
            name=name,
            email=email,
            phone=phone,
            company=company,
            message=message,
        )
        quote.save

        # Send the email notification to both user and team
        send_quote_notification(name, email, company, settings.TEAM_EMAIL, quote_details)

        # Display success message and redirect
        messages.success(request, "Quote request submitted successfully! You will be contacted shortly.")
        return redirect('projects')  # Adjust this as needed

    return render(request, 'pages/home.html')




