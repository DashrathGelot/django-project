# Generated by Django 2.1.5 on 2019-06-27 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stinfo',
            name='birth_date',
            field=models.DateField(default='2019-06-27'),
        ),
    ]