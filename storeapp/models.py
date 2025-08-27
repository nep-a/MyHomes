from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contacts(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        subject = models.CharField(max_length=200)
        message = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)  # timestamp

        def __str__(self):
            return self.name
class Featured_houses(models.Model):
        title = models.CharField(max_length=100)
        image = models.ImageField(upload_to='featured_houses/')
        description = models.TextField()
        location = models.CharField(max_length=200)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        created_at = models.DateTimeField(auto_now_add=True)  # timestamp

        def __str__(self):
            return self.title
