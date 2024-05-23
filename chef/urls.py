from django.urls import path
from .views import RegistrationView,LoginView,LogoutView,Profile,UpdateProfile,ProfileRecipe,RecipeUpdate,ProfileEvent,EventUpdate
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    # Auth
    path('registration/',RegistrationView.as_view(),name='registration'),
    # path('login/',LoginView.as_view(),name='login'),
    # path('logout/',LogoutView.as_view(),name='logout'),
    # Jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Profile
    path('profile/',Profile.as_view(),name='profile'),
    path('profile/update/',UpdateProfile.as_view(),name='profile-update'),
    # Recipe-Event
    path('profile/recipe/',ProfileRecipe.as_view(),name='profile-recipe'),
    path('profile/recipe/<int:pk>/',RecipeUpdate.as_view(),name='update-recipe'),
    path('profile/event/',ProfileEvent.as_view(),name='profile-event'),
    path('profile/event/<int:pk>/',EventUpdate.as_view(),name='update-event'),
]
