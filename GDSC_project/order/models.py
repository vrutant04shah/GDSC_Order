from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class Order(models.Model):
    order_no = models.CharField(max_length = 100)
    order = models.TextField()
    customer_name = models.CharField(max_length = 100)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    time_posted = models.DateTimeField(default = timezone.now)
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=None)
    is_favourite = models.BooleanField(default=False)
    tags = TaggableManager()
    
    def __str__(self):
    	return self.order_no
        
    def get_absolute_url(self):
        return reverse('order-home')
