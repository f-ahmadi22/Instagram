from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import Signal
from user.models import MyUser
from content.models import Post, Story

post_viewed = Signal()


@receiver(post_save, sender=MyUser)
def profile_view_handler(sender, instance, created, **kwargs):
    if created:
        instance.view_count += 1
        instance.save()
        post_viewed.send(sender=sender, instance=instance, user=instance.user)


@receiver(post_save, sender=Post)
def post_view_handler(sender, instance, created, **kwargs):
    if created:
        instance.view_count += 1
        instance.save()
        post_viewed.send(sender=sender, instance=instance, user=instance.author)


@receiver(post_save, sender=Story)
def story_view_handler(sender, instance, created, **kwargs):
    if created:
        instance.view_count += 1
        instance.save()
        post_viewed.send(sender=sender, instance=instance, user=instance.author)
