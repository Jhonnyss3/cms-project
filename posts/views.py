from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
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

class PostVisibilityAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

        # (Opcional) Só o autor pode ocultar/exibir
        if post.author != request.user:
            return Response({'detail': 'You can only change visibility of your own posts.'}, status=status.HTTP_403_FORBIDDEN)

        is_visible = request.data.get('is_visible')
        if is_visible is None:
            return Response({'detail': 'is_visible field is required.'}, status=status.HTTP_400_BAD_REQUEST)

        post.is_visible = is_visible
        post.save()
        return Response({'detail': f'Post visibility set to {is_visible}.'})