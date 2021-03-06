from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ads(models.Model):
    img = models.ImageField(upload_to="ads")
    desc = models.CharField(max_length=20)
    index = models.IntegerField(default=0)
    def __str__(self):
        return self.desc

class Category(models.Model):
    img = models.ImageField(upload_to="picture", default="picture/img.jpg", blank=True, null=True)
    title = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.title
class Tag(models.Model):
    title = models.CharField(max_length=10)
    def __str__(self):
        return self.title
class Product(models.Model):
    img = models.ImageField(upload_to="img", default="img/img.jpg", blank=True, null=True)
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=20)
    price = models.IntegerField()
    update_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.name
class mallUser(User):
    telephone = models.CharField(max_length=11, default="110")