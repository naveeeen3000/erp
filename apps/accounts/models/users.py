from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    user_roles = {
        "student": "STUDENT",
        "teacher": "TEACHER"
    }
    role = models.CharField(max_length=20,choices=user_roles,default=user_roles["student"])
    profile_image = models.ImageField()
    student_id = models.CharField(max_length=20)
    standard = models.CharField(max_length=20)
    college_id = models.IntegerField()
    address = models.TextField()
    summary = models.TextField()

    def __str__(self) :
        return self.user.first_name
