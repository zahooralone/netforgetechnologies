from django.contrib import admin
from .models import Project, Image, Category, Tag, Blog , Comment, QuoteRequest

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_deleted')
    list_filter = ('is_deleted', 'categories', 'tags', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}  # Auto-populate slug from title
    ordering = ('-created_at',)
    actions = ['mark_as_deleted', 'restore']

    def mark_as_deleted(self, request, queryset):
        queryset.update(is_deleted=True)

    def restore(self, request, queryset):
        queryset.update(is_deleted=False)

    mark_as_deleted.short_description = "Mark selected blogs as deleted"
    restore.short_description = "Restore selected blogs"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)

admin.site.register(Comment)



class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'company', 'message')  # Fields to display in the list view
    search_fields = ('name', 'email', 'phone', 'company')  # Fields to search
    list_filter = ('company',)  # Fields to filter by

admin.site.register(QuoteRequest, QuoteRequestAdmin)





class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'client', 'project_date', 'category', 'is_deleted')
    list_filter = ('category', 'client', 'project_date', 'is_deleted')
    search_fields = ('name', 'client', 'category', 'slug')  # Include slug in search
    filter_horizontal = ('images',)  # For ManyToMany relationships
    date_hierarchy = 'project_date'
    prepopulated_fields = {'slug': ('name',)}  # Automatically generate slug from name

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
    search_fields = ('image',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Image, ImageAdmin)

