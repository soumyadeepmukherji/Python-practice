from django.db import models
from django.contrib.auth.models import User  
from django.utils.text import slugify

# Create Post Model
class Post(models.Model):
    title = models.CharField(max_length=200)                   # --> Title of the Post
    slug = models.SlugField(unique=True, blank=True)           # --> Slug if requied
    content = models.TextField()                               # --> Content
    author = models.ForeignKey(User, on_delete=models.CASCADE) # --> Author on user created
    created_at = models.DateTimeField(auto_now_add=True)       # --> Created Time
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    # This Saves the Title as slug if slug field is empty
    def save(self, *args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
# Create Comments Model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"commented by {self.user.username}"


