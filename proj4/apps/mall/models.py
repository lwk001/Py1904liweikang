from django.db import models

# Create your models here.
class Ads(models.Model):
    img = models.ImageField(upload_to="ads")
    desc = models.CharField(max_length=20)
    index = models.IntegerField(default=0)
class Category(models.Model):
    img = models.ImageField(upload_to="picture", default="picture/img.jpg", blank=True, null=True)
    title = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
class Tag(models.Model):
    title = models.CharField(max_length=10)
class Product(models.Model):
    img = models.ImageField(upload_to="img", default="img/img.jpg", blank=True, null=True)
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=20)
    price = models.IntegerField()
    update_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)