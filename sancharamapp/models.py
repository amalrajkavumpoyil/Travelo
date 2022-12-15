from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
class vlog(models.Model):
    date=models.CharField(max_length=100)
    image=models.ImageField(upload_to='picture')
    desc1=models.TextField()
    desc2=models.TextField()
    desc3=models.TextField()




