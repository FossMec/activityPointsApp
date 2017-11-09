from django.db import models






class UserProfile(models.Model):
    student = models.CharField(max_length=30,blank=True,null=True,default='')
    registration_no = models.CharField(max_length=20,null=True)
    password = models.CharField(max_length=50)
    class_list = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.student


