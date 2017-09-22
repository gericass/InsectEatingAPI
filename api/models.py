from django.db import models

# Create your models here.

class restaurant(models.Model):
    name = models.CharField('店名',max_length=256)
    description = models.TextField('説明')
    address = models.CharField('住所',max_length=256)
    lat = models.FloatField('緯度')
    lng = models.FloatField('経度')

    def __str__(self):
        return self.name