from django.db import models 
from apps.accounts.models.users import Users
from .cities import Cities
class Zones(models.Model):

    city_id = models.ForeignKey(Cities,on_delete=models.DO_NOTHING)
    zone_name = models.CharField(max_length=20,null=False,db_index=True)
    bounds = models.JSONField()
    zone_pincode = models.CharField(max_length=6,null=False,db_index=True)
    lat = models.CharField(max_length=20,db_index=True,default=None)
    lng = models.CharField(max_length=20,db_index=True,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Users,on_delete=models.DO_NOTHING)