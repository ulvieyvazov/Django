from django.db import models

# Create your models here.
class Tələbə(models.Model):
    Adı = models.TextField(max_length=25)
    Yasi = models.IntegerField()
    Qrup_No = models.TextField()
    Sekli = models.ImageField(upload_to='photos/%Y/%m/%d/')
    Teqaud = models.BooleanField()
