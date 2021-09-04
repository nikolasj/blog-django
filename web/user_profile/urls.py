from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'user_profile'

router = DefaultRouter()

urlpatterns = [
    path('profile/', views.ProfileView.as_view({'get': 'retrieve'}), name='profile')
]

urlpatterns += router.urls
