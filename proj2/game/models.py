from django.db import models

# Create your models here.
class GameName(models.Model):
    name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Role(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=5, choices=(("man", "男"), ("woman", "女")))
    skill = models.CharField(max_length=20)
    game = models.ForeignKey(GameName, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
