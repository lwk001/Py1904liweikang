# Generated by Django 2.2.3 on 2019-07-02 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]
