from django.db import models

# Create your models here.
class Question(models.Model):
    desc = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.desc
class Choice(models.Model):
    desc = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.desc



class Account(models.Model):
    username = models.CharField(max_length=20, null=True, blank=True, verbose_name='用户名')
    password = models.CharField(max_length=40, null=True, blank=True, verbose_name='密码')
    register_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='注册时间')
    # def __str__(self):
    #     return self.username
class Content(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    address = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=20, null=True)
    mobile = models.CharField(max_length=20, null=True)
    # def __str__(self):
    #     return self.account
