from django.core.management import BaseCommand
from decouple import config
from django.conf import settings
import requests
import pandas as pd

class Command(BaseCommand):


    def handle(self, *args, **options):
        csv_data = pd.read_csv(str(settings.BASE_DIR)+"/pincode_data.csv")
        # for data in csv_data:
        url = config("HOST") + "/api/v1/pincode/"
        headers = {
            "X-RapidAPI-Key": config("API_KEY"),
	        "X-RapidAPI-Host": config("API_HOST")
        }
        i=0
        for val in csv_data.get('pincode'):
            print(val)
            response = requests.get(url+str(val),headers=headers)
            
            if i==1000:
                break
            i=i+1

        print("done")