from .models import Recipe,Event,RecipeCategory,EventCategory
from .serializers import RecipeSerializer,EventSerializer,RecipeCategorySerializer,EventCategorySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from django_filters import rest_framework as filters
# Create your views here.

class RecipeFilter(filters.FilterSet):
    class Meta:
        model = Recipe
        fields = ['category']

class RecipeView(generics.ListAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RecipeFilter


class RecipeCreate(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        try:
            user.total_recipe += 1
            user.save()
            serializer.save(chef=user)
        except Exception as e:
            raise ValidationError({"detail": str(e)})


class RecipeDetails(generics.RetrieveAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    

class RecipeCategoryView(generics.ListAPIView):
    serializer_class = RecipeCategorySerializer
    queryset = RecipeCategory.objects.all()
    

class EventFilter(filters.FilterSet):
    class Meta:
        model = Event
        fields = ['category']
    
    
class EventView(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventFilter


class EventCreate(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        try:
            user.total_event += 1
            user.save()
            serializer.save(organizer=user)
        except Exception as e:
            raise ValidationError({"detail": str(e)})


class EventDetails(generics.RetrieveAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    

class EventCategoryView(generics.ListAPIView):
    serializer_class = EventCategorySerializer
    queryset = EventCategory.objects.all()


    
    
    
        
