from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter
from main.views import TemplateAPIView

from . import views

app_name = 'contact_us'

router = DefaultRouter()

# router.register(r'upload', views.UploadViewSet, basename="upload")

urlpatterns = [
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    # path('', include(router.urls)),
]

urlpatterns += router.urls

if settings.ENABLE_RENDERING:
    urlpatterns += [
        path('contact/', TemplateAPIView.as_view(template_name='contact_us/index.html'), name='index'),
        path('contact-success/', TemplateAPIView.as_view(template_name='contact_us/contact_success.html'),
             name='contact_success'),
    ]
