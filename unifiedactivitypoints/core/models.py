from django.db import models

# Create your models here.


# The main model that holds the activity points
class ActivityPoint(models.Model):
    student_id = models.IntegerField(null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    national_initiatives = models.BooleanField(default=False)  # Direct entry of points
    sports_games = models.BooleanField(default=False)  # Points to be added based on level
    cultural_activities = models.BooleanField(default=False)  # Points to be added based on level
    professional_initiatives = models.BooleanField(default=False)
    entrepreneurship_innovations = models.BooleanField(default=False)
    leadership_management = models.BooleanField(default=False)
    points = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, blank=True)
    approved = models.BooleanField(default=False)  # Will be True after staff adviser approves
    proof = models.FileField(upload_to="documents/")

