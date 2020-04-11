from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    phone = models.IntegerField()
    userid = models.CharField(max_length=50,unique=True)
    pass1 = models.CharField(max_length=50)
    passconf = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Loginuser(models.Model):
    userid= models.CharField(max_length=50,unique=True)
    pass1 = models.CharField(max_length=50)