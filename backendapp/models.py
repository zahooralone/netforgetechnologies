from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify


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
    image = models.ImageField(upload_to='blog_images/')
    content = models.TextField()  # Merged content field from PostDetail
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Added author field
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='blogs', blank=True)  # Changed to ManyToManyField
    tags = models.ManyToManyField(Tag, related_name='blogs', blank=True)
    is_deleted = models.BooleanField(default=False)  # New field for soft deletion

    def __str__(self):
        return self.title

# Automatic slug generation
def generate_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(generate_slug, sender=Blog)



class Comment(models.Model):
    name = models.CharField(max_length=100)  # Commenter's name
    email = models.EmailField()  # Using default email validation
    website = models.URLField(blank=True, null=True)  # New website field
    content = models.TextField()  # Comment content
    created_at = models.DateTimeField(default=timezone.now)  # Timestamp
    # post = models.ForeignKey(PostDetail, related_name='comments', on_delete=models.CASCADE)  # Link to PostDetail

    def __str__(self):
        return f'Comment by {self.name}'

    class Meta:
        ordering = ['-created_at']



class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=100)
    images = models.ManyToManyField('Image', related_name='projects', blank=True)  # Keep the ManyToMany relationship
    client = models.CharField(max_length=100)
    project_date = models.DateField()
    title = models.CharField(max_length=255, blank=True)  # Field from Portfolio
    is_deleted = models.BooleanField(default=False)  # Field from Card
    
    def save(self, *args, **kwargs):
        # Automatically generate a slug if it's not set
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='author_images/')

    def __str__(self):
        return self.image.name




class QuoteRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    company = models.CharField(max_length=200)
    message = models.TextField()
    is_deleted = models.BooleanField(default=False)  # Field for soft delete
    is_seen = models.BooleanField(default=False) 

    def __str__(self):
        return f"QuoteRequest from {self.name}"


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.title