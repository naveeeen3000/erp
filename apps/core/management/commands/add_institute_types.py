from django.core.management import BaseCommand
from apps.core.models.institute_types import InstituteTypes

class Command(BaseCommand):

    def handle(self,*args,**options):
        data = [
            [
                "Primary","Elementary School",
                1,8,6,14,8
            ],
            [
                "Secondary","Secondary School",
                9,12,14,18,4
            ],
            [
                "Tertiary","First University Degree (Bachelor's)",
                12,15,0,0,3
            ],
            [
                "Tertiary","First University Degree (Engineering & Technology)",
                12,16,0,0,4
            ],
            [
                "Tertiary","Second University Degree (Master's)",
                15,17,0,0,2
            ],
            [
                "Tertiary","Doctoral Degree",17,22,0,0,5
            ]
        ]

        for d in data:
            row = InstituteTypes.objects.create(
                education=d[0],
                school_level=d[1],
                from_grades=d[2],
                to_grade=d[3],
                from_age=d[4],
                to_age=d[5],
                years=d[6]
            )
            if row:
                print("inserted")
        print("inserted everything :)))")
