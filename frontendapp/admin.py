from django.contrib import admin


# from .models import Service, PortfolioProject, Testimonial, ContactMessage, TeamMember

# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')
#     search_fields = ('name', 'description')
#     list_filter = ('name',)

# @admin.register(PortfolioProject)
# class PortfolioProjectAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'link')
#     search_fields = ('title', 'description', 'link')
#     list_filter = ('title',)

# @admin.register(Testimonial)
# class TestimonialAdmin(admin.ModelAdmin):
#     list_display = ('client_name', 'content')
#     search_fields = ('client_name', 'content')

# @admin.register(ContactMessage)
# class ContactMessageAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'subject', 'timestamp')
#     search_fields = ('name', 'email', 'subject', 'message')
#     list_filter = ('timestamp',)

# @admin.register(TeamMember)
# class TeamMemberAdmin(admin.ModelAdmin):
#     list_display = ('name', 'role')
#     search_fields = ('name', 'role', 'bio')
