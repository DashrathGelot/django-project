# Generated by Django 2.1.5 on 2019-07-06 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_s_app_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s_app',
            name='Branch',
            field=models.CharField(choices=[('c', 'Computer'), ('m', 'Mechanical'), ('e', 'Electrical'), ('ci', 'Civil'), ('ch', 'Chemical')], max_length=22),
        ),
    ]