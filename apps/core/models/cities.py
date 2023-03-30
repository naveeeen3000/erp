from django.db import models
from apps.accounts.models.users import Users

class Cities(models.Model):

    name = models.CharField(max_length=50,unique=True,null=False)
    state = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Users,on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'cities'
        ordering = ['name']