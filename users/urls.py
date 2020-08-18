from django.urls import path
from .views import SignUpView, ProfileView, ProfileUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup'),
    path('<str:slug>/profile/', ProfileView.as_view(), name = 'profile'),
    path('<str:slug>/profile/update', ProfileUpdateView.as_view(), name = 'profile_update'),
]