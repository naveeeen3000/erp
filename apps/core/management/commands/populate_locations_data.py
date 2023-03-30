from django.core.management import BaseCommand
from decouple import config
from django.conf import settings
from apps.core.models import cities,zones
from apps.accounts.managers.user_manager import UserManager

class Command(BaseCommand):

    def __init__(self):
        self.city = cities.Cities
        self.zone = zones.Zones
        self.user_manager = UserManager()

    def handle(self, *args, **options):
        with open(str(settings.BASE_DIR)+"/IN.txt",'r') as file:
            data = file.readlines()
            states = []
            cities = ['ananthapur']
            user = self.user_manager.get_user_by_id(6)
            count=len(data)
            for d in data:
                split_data = d.split("\t")
                pincode = split_data[1]
                state = split_data[3].lower()
                city = split_data[5].lower()
                print("++++++++"+state)
                lat = split_data[9]
                lng = split_data[10]
                zone = split_data[2].lower()
                city_id = None
                if city not in cities:
                    cities.append(city)
                    city_id = self.city.objects.create(
                        name=city,
                        state=state,
                        created_by=user
                    )
                    
                if city_id is None:
                    city_id = self.city.objects.filter(name=city)
                    city_id = city_id[0]
                self.zone.objects.create(
                    city_id = city_id,
                    zone_name = zone,
                    zone_pincode = pincode,
                    lat=lat,
                    lng=lng,
                    created_by=user
                )
                print(zone+" inserted.")
                count=count-1
                print(str(count)+" remaining.")
                
        print("done")

