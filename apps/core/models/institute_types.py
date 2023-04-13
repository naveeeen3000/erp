from django.db import models


class InstituteTypes(models.Model):

    education = models.CharField(max_length=20)
    school_level = models.CharField(max_length=50)
    from_grades = models.PositiveIntegerField()
    to_grade = models.PositiveBigIntegerField()
    from_age = models.PositiveIntegerField()
    to_age = models.PositiveIntegerField()
    years = models.PositiveIntegerField()

    def __str__(self):
        return self.education
    
    class Meta:
        ordering = ['education']
        db_table = 'institute_types'