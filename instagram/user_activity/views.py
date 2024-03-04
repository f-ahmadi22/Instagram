from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import Comment, LikeComment, LikePost, LikeStory
from .serializers import CommentSerializer, LikeCommentSerializer, LikePostSerializer, LikeStorySerializer
from rest_framework.response import Response


class CommentAPIView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            comment = Comment.objects.get(id=request.data['comment_id'], author=request.user)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return Response({'detail': 'Comment not found or you are not the author.'},
                            status=status.HTTP_404_NOT_FOUND)


class LikePostAPIView(APIView):
    pass


class LikeCommentAPIView(APIView):
    pass


class LikeStoryAPIView(APIView):
    pass
