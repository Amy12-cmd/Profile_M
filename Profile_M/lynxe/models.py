from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    profile_pic = models.ImageField(null=True, blank=True, default="Amol_Sutar1.jpg", upload_to='images/')
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE)
