from msilib.schema import Class
from django.db import models

# Create your models here.
class sign(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    uname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    confirm_password = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='images/profiles', default='https://i.pinimg.com/originals/51/f6/fb/51f6fb256629fc755b8870c801092942.png')
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.CharField(max_length=10)
    role = models.CharField(max_length=20, default="null")