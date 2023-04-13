from django.db import models
from apps.core.models.zones import Zones
from apps.accounts.models.users import Users
from datetime import datetime

class Colleges(models.Model):
    institute_id = models.BigAutoField(primary_key=True,auto_created=True)
    institute_name = models.CharField(null=False,db_index=True,max_length=255)
    description = models.TextField(null=True)
    address_lane_1 = models.TextField(null=True)
    address_lane_2 = models.TextField(null=True)
    city = models.CharField(max_length=100,null=True)
    pincode = models.CharField(max_length=6)
    website = models.URLField(null=True)
    year_of_establishment = models.CharField(max_length=4,null=True)
    affiliat_university = models.CharField(max_length=100,null=True)
    year_of_affiliation = models.CharField(max_length=10,null=True)
    location = models.CharField(max_length=1)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)
    college_type = models.CharField(max_length=100,null=True)
    is_autonomous = models.BooleanField(default=False)
    has_diploma_courses = models.BooleanField(default=False)
    management = models.CharField(max_length=50,db_index=True)
    is_specialized = models.BooleanField(default=False)
    is_evening_college = models.BooleanField(default=False)
    speciality = models.CharField(max_length=100,db_index=True,null=True)
    is_girl_exclusive = models.BooleanField(default=False)
    student_hostel_available = models.BooleanField(default=False)
    hostel_count = models.PositiveIntegerField(null=True)
    zone = models.ForeignKey(Zones,on_delete=models.DO_NOTHING)
    logo = models.ImageField(null=True)
    affiliated_board = models.CharField(choices=(),max_length=200,null=True)
    created_by = models.ForeignKey(Users,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True)


    def __str__(self):
        return self.institute_name


    # def save(self, *args, **kwargs):
    #     now = datetime.now()
    #     self.modified_at = now.strftime("%-/%m-%d, %H:%M:%S")
    #     super(Colleges,self).save(*args,**kwargs)

    class Meta:
        db_table = 'colleges'
        ordering = ['institute_name']
