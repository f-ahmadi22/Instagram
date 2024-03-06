from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import Comment, LikeComment, LikePost, LikeStory
from .serializers import CommentSerializer, LikeCommentSerializer, LikePostSerializer, LikeStorySerializer
from rest_framework.response import Response
from content.models import Post, Story


class CommentAPIView(APIView):
    def post(self, request):
        # Find given post by id
        post = Post.objects.get(id=request.data['post'])
        # Create comment with data input
        comment = Comment.objects.create(author=request.user, post=post, text=request.data['text'])
        # Serialize comment created
        serializer = CommentSerializer(comment)
        # Return serialized data
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        try:
            # Find Comment by id if existed
            comment = Comment.objects.get(id=request.data['comment_id'], author=request.user)
            # Delete comment
            comment.delete()
            # Return success response
            return Response({'detail': 'Comment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        # Comment not existed exception
        except Comment.DoesNotExist:
            # Return comment not found error
            return Response({'detail': 'Comment not found or you are not the author.'},
                            status=status.HTTP_404_NOT_FOUND)


class LikePostAPIView(APIView):
    def post(self, request):
        try:  # Find Post by id if existed
            post = Post.objects.get(id=request.data['post_id'])
        except Post.DoesNotExist:  # Post not existed exception
            return Response({'detail': 'post not found.'},
                            status=status.HTTP_404_NOT_FOUND)

        if LikePost.objects.filter(post=post, author=request.user).exists():  # If user liked it before, delete like
            like = LikePost.objects.get(post=post, author=request.user)
            like.delete()
            # Deleted like successfully
            return Response({'success': True, 'message': 'deleted successfully'}, status=status.HTTP_200_OK)

        else:  # If is not liked before, so like the post
            like = LikePost.objects.create(post=post, author=request.user)
            like.save()
            # Liked successfully
            return Response({'success': True, 'message': 'Post liked successfully'}, status=status.HTTP_200_OK)


class LikeCommentAPIView(APIView):
    def post(self, request):
        try:  # Find Post by id if existed
            comment = Comment.objects.get(id=request.data['comment_id'])
        except Comment.DoesNotExist:  # Comment not existed exception
            return Response({'detail': 'comment not found.'},
                            status=status.HTTP_404_NOT_FOUND)
        # If user liked it before, delete like
        if LikeComment.objects.filter(comment=comment, author=request.user).exists():
            like = LikeComment.objects.get(comment=comment, author=request.user)
            like.delete()
            # Deleted like successfully
            return Response({'success': True, 'message': 'deleted successfully'}, status=status.HTTP_200_OK)

        else:  # If is not liked before, so like the comment
            like = LikeComment.objects.create(comment=comment, author=request.user)
            like.save()
            # Liked successfully
            return Response({'success': True, 'message': 'Comment liked successfully'}, status=status.HTTP_200_OK)


class LikeStoryAPIView(APIView):
    def post(self, request):
        try:  # Find story by id if existed
            story = Story.objects.get(id=request.data['story_id'])
        except Story.DoesNotExist:  # Story not existed exception
            return Response({'detail': 'story not found.'},
                            status=status.HTTP_404_NOT_FOUND)
        # If user liked it before, delete like
        if LikeStory.objects.filter(story=story, author=request.user).exists():
            like = LikeStory.objects.get(story=story, author=request.user)
            like.delete()
            # Deleted like successfully
            return Response({'success': True, 'message': 'deleted successfully'}, status=status.HTTP_200_OK)

        else:  # If is not liked before, so like the story
            like = LikeStory.objects.create(story=story, author=request.user)
            like.save()
            # Liked successfully
            return Response({'success': True, 'message': 'Story liked successfully'}, status=status.HTTP_200_OK)
