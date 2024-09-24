from django.db import models
import datetime

# Create your models here.

# class Service(models.Model):
#     SERVICE_CHOICES = [
#         ('data_strategy', 'Data Strategy'),
#         ('machine_learning', 'Machine Learning'),
#         ('software_solutions', 'Software Solutions'),
#         ('business_mind', 'Business Mind'),
#         ('financial_services', 'Financial Services'),
#         ('data_security', 'Data Security'),
#     ]
#     name = models.CharField(max_length=100, choices=SERVICE_CHOICES)
#     description = models.TextField()
#     icon = models.ImageField(upload_to='services/icons/', blank=True, null=True)
    
#     def _str_(self):
#         return self.get_name_display()

# class PortfolioProject(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
#     link = models.URLField(blank=True, null=True)
    
#     def _str_(self):
#         return self.title

# class Testimonial(models.Model):
#     client_name = models.CharField(max_length=100)
#     content = models.TextField()
#     client_photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    
#     def _str_(self):
#         return f'Testimonial from {self.client_name}'

# class ContactMessage(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     subject = models.CharField(max_length=200)
#     message = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
    
#     def _str_(self):
#         return f'Message from {self.name}'

# class TeamMember(models.Model):
    # name = models.CharField(max_length=100)
    # role = models.CharField(max_length=100)
    # bio = models.TextField()
    # photo = models.ImageField(upload_to='team/', blank=True, null=True)
    
    # def _str_(self):
    #     return self.name