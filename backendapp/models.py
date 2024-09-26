from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify


from django.core.validators import EmailValidator


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)  # Will be filled automatically
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='blogs')
    tags = models.ManyToManyField(Tag, related_name='blogs', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

# Automatic slug generation
def generate_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(generate_slug, sender=Blog)

class PostDetail(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='post_images/')
    categories = models.ManyToManyField(Category, related_name='post_details', blank=True)  # Changed to ManyToManyField
    tags = models.ManyToManyField(Tag, related_name='post_details', blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Automatic slug generation for PostDetail
def generate_post_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(generate_post_slug, sender=PostDetail)



# Blog Category Model
# class Category(models.Model):
#     name = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.name

# Blog Tag Model
# class Tag(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# # Blog Post Model
# class BlogPost(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True, blank=True)  # Allow blank, will be filled automatically before save
#     image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
#     content = models.TextField()
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(auto_now=True)
#     category = models.ManyToManyField(Category, related_name='posts')
#     tags = models.ManyToManyField(Tag, related_name='posts')
    
#     def __str__(self):
#         return self.title

#     class Meta:
#         ordering = ['-created_at']

# # Automatically generate slug from title if not provided
# def generate_slug(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.title)

# Connect signal to pre_save for BlogPost model
# pre_save.connect(generate_slug, sender=BlogPost)

# Comment Model


class Comment(models.Model):
    name = models.CharField(max_length=100)  # Commenter's name
    email = models.EmailField()  # Using default email validation
    website = models.URLField(blank=True, null=True)  # New website field
    content = models.TextField()  # Comment content
    created_at = models.DateTimeField(default=timezone.now)  # Timestamp

    def __str__(self):
        return f'Comment by {self.name}'

    class Meta:
        ordering = ['-created_at']

# Blog Author Bio Model
# class AuthorBio(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField()
#     profile_image = models.ImageField(upload_to='author_images/', null=True, blank=True)

#     def __str__(self):
#         return self.user.username

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ManyToManyField('Image', related_name='projects', blank=True) 
    client = models.CharField(max_length=100)
    project_date = models.DateField()
    # project_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name
    

class Image(models.Model):
    image = models.ImageField(upload_to='author_images/')
    
    def __str__(self):
        return self.image.name
    

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # projects = models.ManyToManyField(Project, related_name='portfolios', blank=True)

    def __str__(self):
        return self.title
    

class Card(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='card_images/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='cards', blank=True, null=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='cards', blank=True, null=True)
    # project_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

