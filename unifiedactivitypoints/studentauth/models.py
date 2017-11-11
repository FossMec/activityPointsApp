from django.db import models


class UserProfile(models.Model):
    student = models.CharField(max_length=30, blank=True, null=True, default='')
    registration_no = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=50)
    class_list = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.student


# Main model for authentication
class User(models.Model):
    staff_adviser = models.BooleanField(default=False)
    username = models.CharField(max_length=30, blank=True, null=True)  # Only for staff advisers
    password = models.CharField(max_length=50)
    student_class = models.CharField(max_length=30, blank=True, null=True)
    student_roll_no = models.IntegerField(blank=True, null=True)



