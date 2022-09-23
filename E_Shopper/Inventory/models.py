from django.core import validators
from django.db import models
from django.db.models import CASCADE
from Vendor.models import Vendor


# Create your models here.
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True, verbose_name='ID')
    cat_name = models.CharField(max_length=100, unique=True, verbose_name='Name')
    cat_desc = models.CharField(max_length=255, verbose_name='Description')
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return f"{self.cat_name}"


class GST(models.Model):
    gst_id = models.AutoField(primary_key=True, verbose_name='ID')
    category = models.ForeignKey(Category, on_delete=CASCADE, unique=True, verbose_name='category')
    igst = models.IntegerField(verbose_name='IGST(%)', validators=[validators.MinValueValidator(1),validators.MaxValueValidator(100)])
    hsn_code = models.IntegerField(unique=True, verbose_name='HSN Code(Unique GST code)')
    def __str__(self):
        return f"{self.hsn_code} --> {self.igst}% --> {self.category}"
    class Meta:
        verbose_name_plural = 'GST'


class Discount(models.Model):
    discount_id = models.AutoField(primary_key=True, verbose_name='ID')
    product_name = models.CharField(max_length=100, verbose_name='Product Name')
    desc = models.CharField(max_length=255, verbose_name='Description')
    discount = models.FloatField(verbose_name='Discount(Rs)')
    start_date = models.DateTimeField(verbose_name='Start Date')
    end_date = models.DateTimeField(verbose_name='End Date')
    def __str__(self):
        return f"{self.product_name} -->{self.discount}"


class Product(models.Model):
    p_id = models.AutoField(primary_key=True, verbose_name='ID')
    p_name = models.CharField(max_length=100, unique=True, verbose_name='Name')
    category = models.ForeignKey(Category, on_delete=CASCADE, verbose_name='Category')
    p_img = models.ImageField(upload_to='product', verbose_name='Image')
    p_price = models.FloatField(verbose_name='Price')
    vendor = models.ForeignKey(Vendor, on_delete=CASCADE, verbose_name='Vendor')
    product_stock = models.FloatField(verbose_name='Quantity(total)')
    unit = models.CharField(max_length=100, verbose_name='Unit(each)')
    reorder_level = models.FloatField(verbose_name='Stock(qty)')
    discount = models.ForeignKey(Discount, on_delete=CASCADE, verbose_name='Discount(Rs)', null=True, blank=True)
    gst = models.ForeignKey(GST, on_delete=CASCADE, verbose_name='GST(hsn code --> igst(%))')
    def __str__(self):
        return f"{self.p_name}"



