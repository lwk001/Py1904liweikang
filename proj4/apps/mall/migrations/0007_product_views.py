# Generated by Django 2.2.3 on 2019-07-19 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0006_malluser'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.CharField(default=111, max_length=100),
        ),
    ]
