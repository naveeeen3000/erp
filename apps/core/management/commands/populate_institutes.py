from django.core.management import BaseCommand
from django.conf import settings
from apps.core.managers.zones_manager import ZonesManager
from apps.accounts.managers.user_manager import UserManager
from apps.core.models.colleges import Colleges
import pandas as pd
import math
import progressbar


class Command(BaseCommand):

    def __init__(self):
        self.z_manager = ZonesManager()
        self.user_manager = UserManager()

    def handle(self,*args,**options):
        csv_data = pd.read_csv(str(settings.BASE_DIR)+"/college_data.csv")
        # print(type(csv_data))
        count = len(csv_data)   
        bar = progressbar.ProgressBar(count).start()
        x = 0
        i = 0
        for index, row in csv_data.iterrows():
            college_name = row['college_institution']
            address_1 = row['address_line1']
            address_2 = row['address_line2'] 
            city = row['city'] 
            pincode = str(row['pin_code'])
            zone = self.z_manager.get_zones_by_pincode_and_city_or_district(pincode,[city,row['district']])
            if zone is None:
                
                x+=1
                continue
            zone = zone[0]
            website = row['website']
            yoe = str(int(row['year_of_establishment'])) if not math.isnan(row['year_of_establishment'])  else None
            aff_uni = row['affiliat_university']
            aff_year = str(int(row['year_of_affiliation'])) if not math.isnan(row['year_of_affiliation'])  else None
            location = row['location']
            lat = str(row['latitude'])
            lng = str(row['longitude'])
            coll_type = row['type']
            autonomous = row['autonomous']
            has_diploma_courses = row['has_diploma_courses']
            management = row['management']
            specialized = row['specialized']
            evening = row['evening']
            speciality = row['speciality'] if row['speciality'] != 'Others' else row['other_speciality']
            girl_exclusive = row['girl_exclusive']
            student_hostel_available = row['student_hostel_available']
            hostel_count = row['hostel_count']
            inserted = Colleges.objects.create(
                institute_name=college_name,
                address_lane_1=address_1,
                address_lane_2=address_2,
                city=city,
                pincode=pincode,
                zone=zone,
                website=website,
                year_of_establishment=yoe,
                affiliat_university=aff_uni,
                year_of_affiliation=aff_year,
                location=location,
                lat=lat,
                lng=lng,
                college_type=coll_type,
                is_autonomous=autonomous,
                has_diploma_courses=has_diploma_courses,
                management=management,
                is_specialized=specialized,
                is_evening_college=evening,
                speciality=speciality,
                is_girl_exclusive=girl_exclusive,
                student_hostel_available=student_hostel_available,
                hostel_count=hostel_count,
                created_by = self.user_manager.get_user_by_id(6)
            )
            if inserted:
                i+=1
                bar.update(index)
        print("isnserted = " + str(i))
        print("Failed due to zone not found = " + str(x))
            