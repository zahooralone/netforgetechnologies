from django.shortcuts import render, redirect, get_object_or_404
from backendapp.models import Project, Portfolio, Card,Blog
from django.views import View
from backendapp.models import PostDetail
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
    return render(request, 'pages/blog_post.html', {'post': post})



# class BlogPostView(View):
#     def get(self, request, slug):
#         post = get_object_or_404(BlogPost, slug=slug)
#         comments = post.comments.all()
#         return render(request, 'pages/blog_post.html', {'post': post, 'comments': comments})



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




