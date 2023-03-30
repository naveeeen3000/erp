from django.db import models
from apps.accounts.models.users import Users

class Cities(models.Model):

    name = models.CharField(max_length=20,unique=True,null=False)
    pincode = models.CharField(max_length=6,null=False)
    state = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Users,on_delete=models.DO_NOTHING)
