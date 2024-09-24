from django.shortcuts import render, redirect, get_object_or_404
from backendapp.models import BlogPost, Comment, Project, Portfolio, Card
from django.views import View
# Create your views here.
def Home(request):
    return render(request, 'pages/home.html')

def about(request):    
    return render(request, 'pages/about.html') 

def blogs(request): 
    posts = BlogPost.objects.all()   
    return render(request, 'pages/blogs.html', {'posts': posts})


def blog_post(request, slug): 
    print(f"Fetching post with slug: {slug}")  # Debug statement
    post = get_object_or_404(BlogPost, slug=slug)
    print(f"Post fetched: {post.title}")  # Debug statement
    comments = post.comments.all()

    if request.method == 'POST':
        # Process the comment form here
        author = request.POST.get('author')
        email = request.POST.get('email')
        content = request.POST.get('content')
        comments = Comment.objects.create(post=post, author=author, email=email, content=content)
        return redirect('blog_post', slug=post.slug)   

    return render(request, 'pages/blog_post.html', {'post': post, 'comments': comments})



class BlogPostView(View):
    def get(self, request, slug):
        post = get_object_or_404(BlogPost, slug=slug)
        comments = post.comments.all()
        return render(request, 'pages/blog_post.html', {'post': post, 'comments': comments})



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
    return render(request, 'pages/projects.html' , {'cards': cards})

    
def services(request):    
    return render(request, 'pages/services.html') 


def viewmore(request):  
    portfolio = Portfolio.objects.all()

   
    projects = Project.objects.all()  
    return render(request, 'pages/viewmore.html', {'projects': projects ,  'portfolio': portfolio,}) 


def dashboard(request):    
    return render(request, 'backend/pages/dashboard.html') 




