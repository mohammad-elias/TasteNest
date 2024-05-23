from rest_framework import serializers
from .models import Recipe,Event,RecipeCategory,EventCategory


class RecipeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeCategory
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    chef = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Recipe
        fields = '__all__'
        
        
class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = '__all__'
        
        
class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Event
        fields = '__all__'