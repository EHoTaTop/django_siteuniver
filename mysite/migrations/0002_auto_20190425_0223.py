# Generated by Django 2.1.7 on 2019-04-24 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='cabinet',
            field=models.IntegerField(),
        ),
    ]