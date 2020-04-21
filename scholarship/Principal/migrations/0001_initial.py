# Generated by Django 2.1.5 on 2019-07-04 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='t_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.s_app')),
            ],
        ),
        migrations.CreateModel(
            name='t_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_id', models.IntegerField(verbose_name='Id')),
                ('Name', models.CharField(max_length=26)),
                ('Mo', models.IntegerField(verbose_name='Mobile No')),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]