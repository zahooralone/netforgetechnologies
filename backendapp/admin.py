from django.contrib import admin
from .models import Project, Image, Portfolio, Card, PostDetail, Category, Tag, Blog 



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
