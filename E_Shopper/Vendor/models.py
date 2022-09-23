from django.db import models


# Create your models here.
class Vendor(models.Model):
    v_id = models.AutoField(primary_key=True, verbose_name='ID')
    v_name = models.CharField(max_length=100, verbose_name='Name')
    v_phone = models.IntegerField(unique=True, verbose_name='Phone no.')
    v_email = models.EmailField(unique=True, verbose_name='Email')
    v_address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Address')
    v_gst_no = models.CharField(max_length=50, verbose_name='GST No', unique=True)
    def __str__(self):
        return f"{self.v_name}"