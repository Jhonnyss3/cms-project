from django.urls import path
from .views import PostCreateAPIView, PostUpdateAPIView, PostVisibilityAPIView

urlpatterns = [
    path('api/create/', PostCreateAPIView.as_view(), name='post-create'),
    path('api/<int:pk>/update/', PostUpdateAPIView.as_view(), name='post-update'),
    path('api/<int:pk>/visibility/', PostVisibilityAPIView.as_view(), name='post-visibility'),
]