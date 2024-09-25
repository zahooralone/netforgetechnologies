from django.contrib import admin
from .models import Project, Image, Portfolio, Card, PostDetail, Category, Tag, Comment

class PostDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('category', 'tags')
    search_fields = ('title', 'content', 'author__username')
    prepopulated_fields = {'slug': ('title',)}  # Keeping this if slug is added

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author_name', 'created_at')
    search_fields = ('author_name', 'content')

admin.site.register(PostDetail, PostDetailAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
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
