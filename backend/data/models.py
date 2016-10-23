from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Otsus(models.Model):
    url = models.CharField(max_length=200)
    id_custom = models.IntegerField()
    teema = models.CharField(max_length=200)
    reg_num = models.CharField(max_length=200)
    vastuvotmise_kp = models.CharField(max_length=200)
    seisund = models.CharField(max_length=200)
    akti_kehtivus = models.CharField(max_length=200)
    pub_date = models.CharField(max_length=200)
    valjandja = models.CharField(max_length=200)
    eelnou_pealkiri = models.CharField(max_length=200)
    #eelnou = models.OneToOneField(SuurEelnou, blank=True)