from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.forms import UserCreationForm

#register
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','first_name','last_name','password1','password2']


class Food(models.Model):
    name = models.CharField(max_length=100)    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.CharField(max_length=100)   
    hotFood = models.BooleanField(default=False)

    def __str__(self):
        return self.name  