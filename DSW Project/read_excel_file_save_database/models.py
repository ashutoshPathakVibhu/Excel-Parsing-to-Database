from django.db import models

# Create your models here.
class student(models.Model):   
        reg = models.CharField(max_length=20)
        ses = models.CharField(max_length=20)
        sem= models.DecimalField(max_digits=12, decimal_places=2)
        sem_type = models.CharField(max_length=20)
        prog = models.CharField(max_length=20)
        bran = models.CharField(max_length=20)
        spi = models.DecimalField(max_digits=12, decimal_places=2)
        p_cpi = models.DecimalField(max_digits=12, decimal_places=2)
        cpi = models.DecimalField(max_digits=12, decimal_places=2)
        result = models.CharField(max_length=20)