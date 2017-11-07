from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver





class UserProfile(models.Model):
    student = models.CharField(max_length=30,blank=True,null=True,default='')
    registration_no = models.CharField(max_length=20,null=True)
    password = models.CharField(max_length=50,default='')
    class_list = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.student

# @receiver(post_save, sender=User)
# def create_user_profile(sender,instance,created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender,instance,**kwargs):
#     instance.profile.save()
