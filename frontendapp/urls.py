from django.urls import path
from . import views
from netforge import settings
from django.conf.urls.static import static
# from backendapp.models import BlogPost


urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<int:id>/', views.blog_post, name='blog_post'),  # Ensure this matches
    path('comment_detail/<int:id>/', views.comment_detail, name='comment_detail'),  # Ensure this matches

    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('services/', views.services, name='services'),
    path('viewmore/', views.viewmore, name='viewmore'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    
