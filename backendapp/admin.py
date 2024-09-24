from django.contrib import admin
from .models import BlogPost, Comment, Category, Tag, AuthorBio, Project, Image, Portfolio, Card

admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(AuthorBio)
admin.site.register(Portfolio)
admin.site.register(Card)




class ImageInline(admin.TabularInline):
    model = Project.image.through  # Allows many-to-many images to be managed within the Project admin
    extra = 1  # Number of empty image fields shown in the admin

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'client', 'project_date')
    search_fields = ('name', 'category', 'client')
    list_filter = ('category', 'project_date')
   

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
    search_fields = ('image',)

# Registering the models
admin.site.register(Project, ProjectAdmin)
admin.site.register(Image, ImageAdmin)
# admin.site.register(PortfolioDetail)





