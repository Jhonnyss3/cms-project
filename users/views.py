from rest_framework import generics, permissions
from .serializers import RegistrationSerializer
from .models import CustomUser
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import ActiveUserListSerializer

# Registra um novo usuário
class RegistrationAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]

# Autentica um usuário já criado
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

#Lista os usuários ativos
class ActiveUserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = ActiveUserListSerializer
    permission_classes = [permissions.IsAuthenticated]