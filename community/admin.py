from django.contrib import admin
from .models import Recipe,Event,RecipeCategory,EventCategory
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Event)
admin.site.register(RecipeCategory)
admin.site.register(EventCategory)