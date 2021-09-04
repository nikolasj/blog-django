from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'actions'

router = DefaultRouter()

urlpatterns = [
    path('like/', views.LikeDislikeView.as_view(), name='like')
]

urlpatterns += router.urls
