from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static


app_name = 'backendapp'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),

   
    path('author/<int:author_id>/', views.author_bio, name='author_bio'),
    path('', views.recent_posts, name='recent_posts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


