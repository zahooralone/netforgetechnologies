from django.contrib import admin
from .models import Project, Image, Portfolio, Card, PostDetail, Category, Tag, Blog , Comment



class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    prepopulated_fields = {'slug': ('title',)}  # Slug auto-population

class PostDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(PostDetail, PostDetailAdmin)
admin.site.register(Category)
admin.site.register(Tag)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'website', 'created_at')  # Display relevant fields
    list_filter = ('created_at',)  # Filter options for admin
    search_fields = ('name', 'email', 'content')  # Searchable fields

    def changelist_view(self, request, extra_context=None):
        total_comments = Comment.objects.count()
        extra_context = extra_context or {}
        extra_context['total_comments'] = total_comments
        return super().changelist_view(request, extra_context=extra_context)
    
admin.site.register(Comment, CommentAdmin)

admin.site.register(Portfolio)
admin.site.register(Card)

class ImageInline(admin.TabularInline):
    model = Project.image.through
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'client', 'project_date')
    search_fields = ('name', 'category', 'client')
    list_filter = ('category', 'project_date')
    inlines = [ImageInline]

    def delete_model(self, request, obj):
        for image in obj.image.all():
            image.delete()
        super().delete_model(request, obj)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
    search_fields = ('image',)

# Registering the models
admin.site.register(Project, ProjectAdmin)
admin.site.register(Image, ImageAdmin)
