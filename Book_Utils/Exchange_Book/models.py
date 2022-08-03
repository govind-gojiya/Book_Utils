from django.db import models

# Create your models here.
class UserDetails(models.Model):
    Fname=models.CharField(max_length=25)
    Lname=models.CharField(max_length=25)
    Email=models.EmailField(max_length=255)
    City=models.CharField(max_length=255)
    College=models.CharField(max_length=255)
    Branch=models.CharField(max_length=25)
    Password=models.CharField(max_length=50)

    def __str__(self):
        return self.Fname