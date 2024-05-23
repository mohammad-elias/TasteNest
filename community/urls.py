from django.urls import path
from .views import RecipeView,RecipeCreate,RecipeDetails,RecipeCategoryView,EventView,EventCreate,EventDetails,EventCategoryView

urlpatterns = [
    # recipe
    path('recipe/',RecipeView.as_view(),name='recipe'),
    path('recipe/create/',RecipeCreate.as_view(),name='recipe-create'),
    path('recipe/<int:pk>/',RecipeDetails.as_view(),name='recipe-details'),
    path('recipe/category/',RecipeCategoryView.as_view(),name='recipe-category'),
    # event
    path('event/',EventView.as_view(),name='event'),
    path('event/create/',EventCreate.as_view(),name='event-create'),
    path('event/<int:pk>/',EventDetails.as_view(),name='event-details'),
    path('event/category/',EventCategoryView.as_view(),name='event-category'),
]
