from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    registration_no = models.CharField(max_length=20,null=True)
    password = models.CharField(max_length=50)
    class_no = models.CharField(max_length=9,blank=True)

    def __str__(self):
        return self.name

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
