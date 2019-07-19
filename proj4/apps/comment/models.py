from django.db import models
from mall.models import Product

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)





