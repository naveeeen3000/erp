from django.core.management import BaseCommand
from apps.leetcode.managers.leetcode_manager import LeetCodeManager
from django.conf import settings
import csv


class Command(BaseCommand):

    def __init__(self):
        self.leet_manager = LeetCodeManager()

    def handle(self,*args,**options):
        with open(str(settings.BASE_DIR)+"/leetcode.csv") as file:
            csv_data = csv.reader(file)
            next(csv_data) ## to skip the header 
            count = 0
            for data in csv_data:
                inserted = self.leet_manager.add_leet_code_problem(
                    topic= data[1],
                    leetcode_question_link=data[2],
                    difficulty=data[3]
                )
                if inserted:
                    count+=1
                else:
                    print("insert failed")
            print("inserted {}.".format(count))