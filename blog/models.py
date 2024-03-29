from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def upload_location(instance, filename):
    return f"post_images/{instance.author.username}/{filename}"

class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_location)  
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published_at']
