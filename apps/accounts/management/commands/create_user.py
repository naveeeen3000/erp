from django.core.management import BaseCommand
from apps.accounts.models.users import Users
from erpsys.helpers.custom_exceptions import PasswordsDontMatchException
from getpass import getpass


class Command(BaseCommand):

    def handle(self, *args, **options):
        first_name = input("enter student name: ")
        email = input("email: ")
        password = getpass('password: ')
        password_2 = getpass('enter password again: ')
        if password != password_2:
            raise PasswordsDontMatchException("Passwords dont match")
        role  = input("enter role(STUDENT or TEACEHR): ")
        
        user = Users.objects.create(username=first_name,email=email,role=role)
        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.save()

        print("user created")