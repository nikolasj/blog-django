from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'actions'

router = DefaultRouter()

urlpatterns = [
    path('like/', views.LikeDislikeView.as_view(), name='like'),
    path('follow/', views.FollowViewSet.as_view({'post': 'create'}), name='follow')
]

urlpatterns += router.urls
