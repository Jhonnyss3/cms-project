from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

# criar novo post
class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Editar post existente
class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Garante que só o autor pode editar (opcional, remova se não quiser essa regra)
        if self.request.user != serializer.instance.author:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You can only edit your own posts.")
        serializer.save()