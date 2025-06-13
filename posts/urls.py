from django.urls import path
from .views import PostCreateAPIView

urlpatterns = [
    path('api/create/', PostCreateAPIView.as_view(), name='post-create'),
]