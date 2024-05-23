from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class RecipeCategory(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    chef = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/recipe')
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=255)
    ingredients = models.TextField(max_length=550)
    instructions = models.TextField(max_length=550)
    prepare_time = models.IntegerField(default=0)
    cooking_time = models.IntegerField(default=0)
    serving = models.IntegerField(default=0)
    category = models.ManyToManyField(RecipeCategory,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/event')
    description = models.TextField(max_length=550)
    location = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    category = models.ManyToManyField(EventCategory,blank=True)
    organizer = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
