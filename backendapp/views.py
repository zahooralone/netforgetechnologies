from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages
from .models import Blog, Category, Tag, Comment,  Project, Image, QuoteRequest, Service
from django.http import JsonResponse
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.dateparse import parse_date
from django.core.paginator import Paginator

@login_required
def dashboard(request):
    comments = Comment.objects.all()  # Fetch all comments
   
    comment_count = comments.count()  # Get the total number of comments
    active_tab = request.GET.get('active_tab', 'blogs')  # Default to 'blogs' tab if not set
    # Your existing code to fetch data for each tab here...

      

    # Pagination for blogs
    blogs = Blog.objects.all()
    blog_paginator = Paginator(blogs, 5)  # Show 5 blogs per page
    blog_page_number = request.GET.get('blog_page')
    blog_page_obj = blog_paginator.get_page(blog_page_number)

    # Pagination for requests
    requests = QuoteRequest.objects.all()
    request_paginator = Paginator(requests, 5)  # Show 5 requests per page
    request_page_number = request.GET.get('request_page')
    request_page_obj = request_paginator.get_page(request_page_number)

    # Count requests and new requests
    total_requests = requests.count()
    new_requests = requests.filter(is_seen=False).count()  # Assuming `is_seen` indicates if the request is new

    # Pagination for projects
    projects = Project.objects.all()
    project_paginator = Paginator(projects, 5)  # Show 5 projects per page
    project_page_number = request.GET.get('project_page')
    project_page_obj = project_paginator.get_page(project_page_number)

    # Pagination for services
    services = Service.objects.all()  # Fetch all services
    service_paginator = Paginator(services, 5)  # Show 5 services per page
    service_page_number = request.GET.get('service_page')
    service_page_obj = service_paginator.get_page(service_page_number)

    blog_count = blogs.count()
    total_comments = comments.count()
    total_projects = projects.count()

    context = {
        'comments': comments,
        'comment_count': comment_count,  # Pass comment count to the context   
        'requests': request_page_obj,  # Use paginated requests
        'projects': project_page_obj,  # Use paginated projects
        'blogs': blog_page_obj,  # Use paginated blogs
        'services': service_page_obj,  # Use paginated services
        'blog_count': blog_count,
        'total_comments': total_comments,
        'total_projects': total_projects,
        'total_requests': total_requests,  # Pass total requests to context
        'new_requests': new_requests,  # Pass new requests count to context
        'active_tab': active_tab,
    }
    return render(request, 'backend/pages/dashboard.html', context)


def dashboard_view(request):
    # Fetch data from each model
    total_blogs = Blog.objects.count()
    deleted_blogs = Blog.objects.filter(is_deleted=True).count()
    
    total_projects = Project.objects.count()
    deleted_projects = Project.objects.filter(is_deleted=True).count()

    total_quote_requests = QuoteRequest.objects.count()
    deleted_quote_requests = QuoteRequest.objects.filter(is_deleted=True).count()

    total_services = Service.objects.count()
    deleted_services = Service.objects.filter(deleted=True).count()

    context = {
        'total_blogs': total_blogs,
        'deleted_blogs': deleted_blogs,
        'total_projects': total_projects,
        'deleted_projects': deleted_projects,
        'total_quote_requests': total_quote_requests,
        'deleted_quote_requests': deleted_quote_requests,
        'total_services': total_services,
        'deleted_services': deleted_services,
    }
    return render(request, 'backend/pages/dashboard.html', context)





def comment_list(request):
    comments = Comment.objects.all()  # Fetch all comments
    comment_count = comments.count()
    context = {
        'comments': comments,
        'comment_count': comment_count,  # Pass comment count to the context   

    }
    return render(request, 'backend/pages/comments.html', context)  # Ensure the template path is correct


def comment_detail(request, comment_id):
    print(f"Fetching comment details for ID: {comment_id}")  # Debugging
    comment = get_object_or_404(Comment, id=comment_id) 
    context = {
        'comment': comment,
    }
    return render(request, 'backend/pages/comment_detail.html', context)  # Create this template

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()  # Delete the comment
    messages.success(request, "Comment deleted successfully.")
    return redirect('backendapp:comments')  # Redirect to the comments list


def delete_selected_comments(request):
    if request.method == "POST":
        print("Delete selected comments triggered.")  # Debugging
        comment_ids = request.POST.getlist('comment_ids')
        Comment.objects.filter(id__in=comment_ids).delete()
        messages.success(request, "Selected comments have been deleted successfully.")
        return redirect('backendapp:comments')

    return redirect('backendapp:comments')



def add_blog(request):
    if request.method == 'POST':
        # Handle blog creation
        title = request.POST.get('title')
        image = request.FILES.get('image')
        content = request.POST.get('content')
        post_categories = request.POST.getlist('post_categories')
        post_tags = request.POST.getlist('post_tags')

        # Create Blog instance
        blog = Blog(
            title=title,
            image=image,
            content=content,
            author=request.user,
        )
        blog.save()

        # Assign selected categories and tags
        if post_categories:
            blog.categories.set(post_categories)
        if post_tags:
            blog.tags.set(post_tags)

        messages.success(request, 'Blog added successfully!')
        return redirect('backendapp:dashboard')  # Adjust this to your success URL

    return render(request, 'backend/add/add_blog.html', {
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
    })


def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    
    if request.method == 'POST':
        # Handle blog update
        title = request.POST.get('title')
        image = request.FILES.get('image') or blog.image  # Keep existing image if not updated
        content = request.POST.get('content')
        post_categories = request.POST.getlist('post_categories')
        post_tags = request.POST.getlist('post_tags')

        # Update Blog instance
        blog.title = title
        blog.image = image
        blog.content = content
        blog.save()

        # Assign selected categories and tags
        blog.categories.set(post_categories)
        blog.tags.set(post_tags)

        messages.success(request, 'Blog updated successfully!')
        return redirect('backendapp:dashboard')  # Adjust this to your success URL

    return render(request, 'backend/edit/edit_blog.html', {
        'blog': blog,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
    })


def view_blog_detail(request, slug):
    # Fetch the blog post by id
    blog = get_object_or_404(Blog, slug=slug)

    # Render the blog details page
    return render(request, 'backend/display/view_blog_detail.html', {'blog': blog})

def view_blog(request):
    # Fetch all blogs that are not marked as deleted
    blogs = Blog.objects.filter(is_deleted=False) 
    return render(request, 'backend/display/view_blog.html', {'blogs': blogs})

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    
    # Mark as deleted
    blog.is_deleted = True
    blog.save()  # Save the change to the database
    messages.success(request, "Blog post marked as deleted.")
    
    return redirect('backendapp:view_blog')


def deleted_blogs(request):
    # Retrieve blogs marked as deleted
    blogs = Blog.objects.filter(is_deleted=True)
    
    return render(request, 'backend/pages/deleted_blogs.html', {'blogs': blogs})

def restore_blog(request, blog_id):
    blog_to_restore = get_object_or_404(Blog, id=blog_id)
    
    if blog_to_restore.is_deleted:
        blog_to_restore.is_deleted = False  # Restore the blog
        blog_to_restore.save()
        messages.success(request, "Blog post restored.")
    else:
        messages.error(request, "Blog post not found in deleted blogs.")
    
    return redirect('backendapp:deleted_blogs')

def permanently_delete_blog(request, slug):
    blog_to_delete = get_object_or_404(Blog, slug=slug)
    
    if blog_to_delete.is_deleted:
        blog_to_delete.delete()  # Permanently delete from the database
        messages.success(request, "Blog post permanently deleted.")
    else:
        messages.error(request, "Blog post not found in deleted blogs.")
    
    return redirect('backendapp:deleted_blogs')




def add_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        if category_name:
            Category.objects.get_or_create(name=category_name)
            messages.success(request, f'Category "{category_name}" added successfully!')
    return HttpResponseRedirect(f"{reverse('backendapp:add_blog')}#category")


def add_tag(request):
    if request.method == 'POST':
        tag_name = request.POST.get('tag_name')
        if tag_name:
            Tag.objects.get_or_create(name=tag_name)
            messages.success(request, f'Tag "{tag_name}" added successfully!')
            return redirect(f"{reverse('backendapp:add_blog')}#tag")  # Redirect to the tag tab
    return redirect(f"{reverse('backendapp:add_blog')}#tag")  # Fallback in case of GET request

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    messages.success(request, f'Category "{category.name}" deleted successfully!')
    return redirect('backendapp:add_blog')  # Redirect back to the add blog page


def delete_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    tag.delete()
    messages.success(request, f'Tag "{tag.name}" deleted successfully!')
    return redirect(f"{reverse('backendapp:add_blog')}#tag")





def add_project(request):
    if request.method == 'POST':
        # Get data from the POST request
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        client = request.POST.get('client')
        project_date = request.POST.get('project_date')
        title = request.POST.get('title')
        is_deleted = request.POST.get('is_deleted') == 'on'

        # Convert project_date to date format
        try:
            project_date = parse_date(project_date)
        except ValueError:
            messages.error(request, 'Invalid date format.')
            return redirect('backendapp:add_project')

        # Generate slug from name and ensure uniqueness
        slug = slugify(name)  # Create a slug from the name
        original_slug = slug
        counter = 1
        while Project.objects.filter(slug=slug).exists():
            slug = f"{original_slug}-{counter}"
            counter += 1

        # Create the project instance
        project = Project.objects.create(
            name=name,
            slug=slug,  # Use the unique slug
            description=description,
            category=category,
            client=client,
            project_date=project_date,
            title=title,
            is_deleted=is_deleted
        )

        # Handle multiple images upload
        images = request.FILES.getlist('images')
        if images:
            for img in images:
                image_instance = Image.objects.create(image=img)
                project.images.add(image_instance)

        messages.success(request, 'Project added successfully!')
        return redirect('backendapp:dashboard')

    return render(request, 'backend/add/add_project.html')


def view_project_detail(request, project_id):
    # Fetch the project by id
    project = get_object_or_404(Project, id=project_id)

    # Render the project details page
    return render(request, 'backend/display/view_project_detail.html', {'project': project})



def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        # Get updated project details
        project.name = request.POST.get('name')
        project.description = request.POST.get('description')
        project.category = request.POST.get('category')
        project.client = request.POST.get('client')
        project.project_date = request.POST.get('project_date')

        # Update the project instance
        project.save()

        # Handle image updates
        if request.FILES.getlist('images'):
            # Clear existing images if any new images are uploaded
            project.images.clear()

            # Save new images and associate them with the project
            images = request.FILES.getlist('images')  # Get the list of uploaded images
            for img in images:
                image_instance = Image.objects.create(image=img)
                project.images.add(image_instance)

        messages.success(request, 'Project updated successfully!')
        return redirect('backendapp:dashboard')  # Change to your success URL

    return render(request, 'backend/edit/edit_project.html', {'project': project})


def view_project(request):
    projects = Project.objects.all()
    return render(request, 'backend/display/view_project.html', {'projects': projects})



def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    # Mark as deleted
    project.is_deleted = True
    project.save()  # Save the change to the database
    messages.success(request, "Project marked as deleted.")
    
    return redirect('backendapp:view_project')

def deleted_projects(request):
    # Retrieve projects marked as deleted
    projects = Project.objects.filter(is_deleted=True)
    
    return render(request, 'backend/pages/deleted_projects.html', {'projects': projects})

def restore_project(request, project_id):
    project_to_restore = get_object_or_404(Project, id=project_id)
    
    if project_to_restore.is_deleted:
        project_to_restore.is_deleted = False  # Restore the project
        project_to_restore.save()
        messages.success(request, "Project restored.")
    else:
        messages.error(request, "Project not found in deleted projects.")
    
    return redirect('backendapp:deleted_projects')

def permanently_delete_project(request, slug):
    project_to_delete = get_object_or_404(Project, slug=slug)
    
    if project_to_delete.is_deleted:
        project_to_delete.delete()  # Permanently delete from the database
        messages.success(request, "Project permanently deleted.")
    else:
        messages.error(request, "Project not found in deleted projects.")
    
    return redirect('backendapp:deleted_projects')







def view_quote_requests(request):
    # Retrieve all quote requests
    quote_requests = QuoteRequest.objects.all()

    # Mark all unseen requests as seen when they are accessed
    QuoteRequest.objects.filter(is_seen=False).update(is_seen=True)

    return render(request, 'backend/display/view_requests.html', {'quote_requests': quote_requests})


def delete_request(request, quote_request_id):
    quote_request = get_object_or_404(QuoteRequest, id=quote_request_id)
    
    # Mark as deleted
    quote_request.is_deleted = True
    quote_request.save()  # Save the change to the database
    messages.success(request, "Quote Request marked as deleted.")
    
    return redirect('backendapp:dashboard')

def deleted_requests(request):
    # Get the quote request to delete
    quote_request = QuoteRequest.objects.filter(is_deleted=True)

    return render(request, 'backend/pages/deleted_requests.html',{'quote_request':quote_request})


def delete_selected_requests(request):
    if request.method == "POST":
        print("Delete selected requests triggered.")  # Debugging
        request_ids = request.POST.getlist('request_ids')
        QuoteRequest.objects.filter(id__in=request_ids).delete()
        messages.success(request, "Selected quote requests have been deleted successfully.")
        return redirect('backendapp:deleted_requests')  # Redirect to deleted requests page or list

    return redirect('backendapp:deleted_requests')


def restore_request(request, quote_request_id):
    quote_request = get_object_or_404(QuoteRequest, id=quote_request_id)
    
    if quote_request.is_deleted:
        quote_request.is_deleted = False  # Restore the request
        quote_request.save()
        messages.success(request, "Quote Request restored.")
    else:
        messages.error(request, "Quote request not found in deleted requests.")
    
    return redirect('backendapp:deleted_requests')


def permanently_delete_request(request, quote_request_id):
    # Fetch the QuoteRequest object to permanently delete
    quote_request = get_object_or_404(QuoteRequest, id=quote_request_id)
    
    if quote_request.is_deleted:
        quote_request.delete()  # Permanently delete from the database
        messages.success(request, "Quote Request permanently deleted.")
    else:
        messages.error(request, "Quote Request not found in deleted requests.")
    
    return redirect('backendapp:deleted_requests')







def add_service(request):
    if request.method == 'POST':
        # Get the submitted form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        # Create a new service instance
        service = Service(
            title=title,
            description=description,
            slug=slugify(title)  # Slugify the title
        )
        
        # Save the new service to the database
        service.save()
        
        # Show a success message and redirect to the service list or home page
        messages.success(request, 'Service added successfully!')
        return redirect('backendapp:add_service')  # Change this to the appropriate URL

    # Render the template with an empty form
    return render(request, 'backend/add/add_service.html')


def view_service(request):
    services = Service.objects.all()  # Fetch all services from the database
    return render(request, 'backend/display/view_service.html', {'services': services})   
 
def service_detail_view(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'backend/display/service_detail.html', {'service': service})

def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    if request.method == 'POST':
        # Update the service with the submitted data
        service.title = request.POST.get('title')
        service.description = request.POST.get('description')
        service.save()
        
        # Show success message and redirect to the service list page
        messages.success(request, 'Service updated successfully!')
        return redirect('backendapp:view_service')

    return render(request, 'backend/edit/edit_service.html', {'service': service})


def delete_service(request, slug):
    service = get_object_or_404(Service, slug=slug)
    service.deleted = True  # Mark service as deleted
    service.save()
    messages.success(request, f"Service '{service.title}' has been marked as deleted.")
    return redirect('backendapp:view_service')

def deleted_services(request):
    deleted_services = Service.objects.filter(deleted=True)  # Fetch only soft-deleted services
    return render(request, 'backend/pages/deleted_services.html', {'deleted_services': deleted_services})


def restore_service(request, slug):
    service = get_object_or_404(Service, slug=slug, deleted=True)
    service.deleted = False  # Restore service
    service.save()
    messages.success(request, f"Service '{service.title}' has been restored.")
    return redirect('backendapp:deleted_services')

def permanently_delete_service(request, slug):
    service = get_object_or_404(Service, slug=slug, deleted=True)
    service.delete()  # Permanently remove service from database
    messages.success(request, f"Service '{service.title}' has been permanently deleted.")
    return redirect('backendapp:deleted_services')
