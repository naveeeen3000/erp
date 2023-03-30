from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint
class Users(AbstractUser):
    
    
    def __init__(self, *args: any, **kwargs: any) -> None:
        super().__init__(*args, **kwargs)

    user_roles = [
        ("student","STUDENT"),
        ("teacher", "TEACHER")
    ]
    email = models.EmailField(db_index=True)
    role = models.CharField(max_length=20,choices=user_roles,default="STUDENT")
    profile_image = models.ImageField(null=True)
    student_id = models.CharField(max_length=20,null=True)
    standard = models.CharField(max_length=20,null=True)
    phone = models.CharField(max_length=13,null=True)
    college_id = models.IntegerField(null=True)
    address = models.TextField(null=True)
    summary = models.TextField(null=True)

    def __str__(self) :
        return self.first_name

    class Meta:
        db_table = 'users'
        ordering = ['first_name']
        verbose_name = 'An Institutes member'
        constraints = [
            UniqueConstraint(fields=['email','student_id','phone'],name='unique_student_constraint')
        ]