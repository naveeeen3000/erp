from django.db import models



class Institute(models.Model):
    pass
    # institute_id = models.BigAutoField(primary_key=True)
    # institute_name = models.CharField(20,null=False,db_index=True)
    # description_id = models.TextField()
    # zone_id = models.ForeignKey("zones",on_delete=models.DO_NOTHING)
    # logo = models.ImageField()
    # tagline = models.TextField()
    # institute_type = models.CharField(choices=())
    # affiliated_board = models.CharField(choices=())
    # def __str__(self):
    #     return self.institute_name

    # class Meta:
    #     db_table = 'institutes'
    #     ordering = ['institue_name']
