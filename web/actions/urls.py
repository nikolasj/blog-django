from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'actions'

router = DefaultRouter()

urlpatterns = [
    path('like/', views.LikeDislikeView.as_view(), name='like'),
    path('follow/', views.FollowView.as_view(), name='follower'),
    path('followers/', views.FollowViewSet.as_view({'get': 'list_followers'}), name='followers'),
    path('following/', views.FollowViewSet.as_view({'get': 'list_following'}), name='following'),
    # path('follow/', views.FollowViewSet.as_view({'post': 'create'}), name='follow')
]

urlpatterns += router.urls
