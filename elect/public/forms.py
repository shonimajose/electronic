from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields =["first_name","email","username","password1","password2"]
        