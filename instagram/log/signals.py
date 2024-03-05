from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import Signal
from user.models import MyUser
from .models import ProfileView, PostView, StoryView

post_viewed = Signal()


@receiver(post_save, sender=ProfileView)
def profile_view_handler(sender, instance, created, **kwargs):

    if created:
        instance.user_profile.view_count += 1
        instance.save()
        post_viewed.send(sender=sender, instance=instance, user=instance.user)


@receiver(post_save, sender=PostView)
def post_view_handler(sender, instance, created, **kwargs):
    if created:
        instance.post.view_count += 1
        instance.save()
        post_viewed.send(sender=sender, instance=instance, user=instance.user)


@receiver(post_save, sender=StoryView)
def story_view_handler(sender, instance, created, **kwargs):
    if created:
        instance.story.view_count += 1
        instance.save()
        post_viewed.send(sender=sender, instance=instance, user=instance.user)
