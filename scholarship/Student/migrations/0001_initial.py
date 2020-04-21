# Generated by Django 2.1.5 on 2019-07-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='s_app',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enrollment_No', models.IntegerField(default='', max_length=16, verbose_name='Enrollment No')),
                ('Name', models.CharField(max_length=25)),
                ('BirthDate', models.DateField(default='')),
                ('Branch', models.CharField(choices=[('c', 'Computer'), ('m', 'Mechanical'), ('e', 'Electrical'), ('ci', 'Civil'), ('ch', 'Chemical')], default='c', max_length=22)),
                ('Mobile_No', models.IntegerField(max_length=10, verbose_name='Mobile No')),
                ('Email', models.EmailField(max_length=254)),
                ('Annual_Income', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='s_re',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enrollment_No', models.IntegerField(default='', max_length=16, verbose_name='Enrollment No')),
                ('Name', models.CharField(max_length=25)),
                ('BirthDate', models.DateField(default='')),
                ('Branch', models.CharField(choices=[('c', 'Computer'), ('m', 'Mechanical'), ('e', 'Electrical'), ('ci', 'Civil'), ('ch', 'Chemical')], default='c', max_length=22)),
                ('Mobile_No', models.IntegerField(max_length=10, verbose_name='Mobile No')),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]