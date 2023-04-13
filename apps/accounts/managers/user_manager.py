from apps.accounts.models.users import Users
from django.core.exceptions import ValidationError

class UserManager():

    def get_user_by_id(self,id=None):
        if id is None:
            raise ValidationError("Id not provided")
        user = Users.objects.get(id=id)
        if user:
            return user
        return None
    
    def get_user_by_email(self,email=None):
        if email is None:
            raise ValidationError("Email not provided")
        user = Users.objects.filter(email=email)
        if user.exists():
            return user
        return user
    
    