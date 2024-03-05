from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import Comment, LikeComment, LikePost, LikeStory
from .serializers import CommentSerializer, LikeCommentSerializer, LikePostSerializer, LikeStorySerializer
from rest_framework.response import Response
from content.models import Post, Story


class CommentAPIView(APIView):
    def post(self, request):
        post = Post.objects.get(id=request.data['post'])
        comment = Comment.objects.create(author=request.user, post=post, text=request.data['text'])
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        try:
            comment = Comment.objects.get(id=request.data['comment_id'], author=request.user)
            comment.delete()
            return Response({'detail': 'Comment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return Response({'detail': 'Comment not found or you are not the author.'},
                            status=status.HTTP_404_NOT_FOUND)


class LikePostAPIView(APIView):
    def post(self, request):
        try:
            post = Post.objects.get(id=request.data['post_id'])
        except Post.DoesNotExist:
            return Response({'detail': 'post not found.'},
                            status=status.HTTP_404_NOT_FOUND)

        if LikePost.objects.filter(post=post, author=request.user).exists():
            like = LikePost.objects.get(post=post, author=request.user)
            like.delete()
            return Response({'success': True, 'message': 'deleted successfully'}, status=status.HTTP_200_OK)

        else:
            like = LikePost.objects.create(post=post, author=request.user)
            like.save()
            return Response({'success': True, 'message': 'Post liked successfully'}, status=status.HTTP_200_OK)


class LikeCommentAPIView(APIView):
    def post(self, request):
        try:
            comment = Comment.objects.get(id=request.data['comment_id'])
        except Comment.DoesNotExist:
            return Response({'detail': 'comment not found.'},
                            status=status.HTTP_404_NOT_FOUND)
        if LikeComment.objects.filter(comment=comment, author=request.user).exists():
            like = LikeComment.objects.get(comment=comment, author=request.user)
            like.delete()
            return Response({'success': True, 'message': 'deleted successfully'}, status=status.HTTP_200_OK)

        else:
            like = LikeComment.objects.create(comment=comment, author=request.user)
            like.save()
            return Response({'success': True, 'message': 'Comment liked successfully'}, status=status.HTTP_200_OK)


class LikeStoryAPIView(APIView):
    def post(self, request):
        try:
            story = Story.objects.get(id=request.data['story_id'])
        except Story.DoesNotExist:
            return Response({'detail': 'story not found.'},
                            status=status.HTTP_404_NOT_FOUND)
        if LikeStory.objects.filter(story=story, author=request.user).exists():
            like = LikeStory.objects.get(story=story, author=request.user)
            like.delete()
            return Response({'success': True, 'message': 'deleted successfully'}, status=status.HTTP_200_OK)

        else:
            like = LikeStory.objects.create(story=story, author=request.user)
            like.save()
            return Response({'success': True, 'message': 'Story liked successfully'}, status=status.HTTP_200_OK)
