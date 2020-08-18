from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, FeaturesPageView, AnnouncementsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('contact/', ContactPageView.as_view(), name = 'contact'),
    path('features/', FeaturesPageView.as_view(), name = 'features'),
    path('announcements/', AnnouncementsPageView.as_view(), name = 'announcements')
]
