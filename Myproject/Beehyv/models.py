from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
  
    name=models.CharField(max_length=200)
    email=models.EmailField( max_length=254)
    subject=models.CharField(max_length=200)
    msg=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.subject
