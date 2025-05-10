from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from netforge import settings

app_name = 'backendapp'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('comments/', views.comment_list, name='comments'),  # Add this line
    path('comments/<int:comment_id>/', views.comment_detail, name='comment_detail'),
    path('comments/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('delete-selected-comments/', views.delete_selected_comments, name='delete_selected_comments'),
    path('add-blog/', views.add_blog, name='add_blog'),  # Add this line
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('edit-project/<int:project_id>/', views.edit_project, name='edit_project'), 
    path('add_category/', views.add_category, name='add_category'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('delete_tag/<int:tag_id>/', views.delete_tag, name='delete_tag'),
    path('add-project/', views.add_project, name='add_project'),
    path('delete-project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('delete-project/', views.deleted_projects, name='deleted_projects'),
    path('restore-project/<int:project_id>/', views.restore_project, name='restore_project'),
    path('permanently-delete-project/<slug:slug>/', views.permanently_delete_project, name='permanently_delete_project'),
    path('view-blog/', views.view_blog, name='view_blog'),
    path('authenticated/view-blog/<slug:slug>/', views.view_blog_detail, name='view_blog_detail'),
    path('view-project/', views.view_project, name='view_project'),
    path('authenticated/view-project/<int:project_id>/', views.view_project_detail, name='view_project_detail'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('deleted/', views.deleted_blogs, name='deleted_blogs'),  # New URL
    path('restore/<int:blog_id>/', views.restore_blog, name='restore_blog'),
    path('permanently-delete/<slug:slug>/', views.permanently_delete_blog, name='permanently_delete_blog'),
    path('quote-requests/', views.view_quote_requests, name='view_quote_requests'),
    path('delete_request/<int:quote_request_id>/', views.delete_request, name='delete_request'),
    path('deleted_requests/', views.deleted_requests, name='deleted_requests'),  # New URL
    path('delete-selected-requests/', views.delete_selected_requests, name='delete_selected_requests'),
    path('restore_request/<int:quote_request_id>/', views.restore_request, name='restore_request'),
    path('permanently-delete-request/<int:quote_request_id>/', views.permanently_delete_request, name='permanently_delete_request'),
    path('add-service/', views.add_service, name='add_service'),
    path('view-services/', views.view_service, name='view_service'),  
    path('service/<slug:slug>/', views.service_detail_view, name='service_detail'),
    path('edit-service/<int:service_id>/', views.edit_service, name='edit_service'),
    path('services/deleted/', views.deleted_services, name='deleted_services'),
    path('service/delete/<slug:slug>/', views.delete_service, name='delete_service'),
    path('service/restore/<slug:slug>/', views.restore_service, name='restore_service'),
    path('service/permanently-delete/<slug:slug>/', views.permanently_delete_service, name='permanently_delete_service'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

