from django.urls import path
from users.views import RegistrationAPIView, LoginAPIView, ActiveUserListAPIView

urlpatterns = [
    path('api/register/', RegistrationAPIView.as_view(), name='register'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('api/active/', ActiveUserListAPIView.as_view(), name='active-users'),
]