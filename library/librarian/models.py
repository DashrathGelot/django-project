from django.db import models
from student.models import Stinfo

class Book(models.Model):
    name=models.CharField(max_length=50)
    isbn=models.IntegerField()
    publish_date=models.DateField()
    re=models.ForeignKey(Stinfo,on_delete=models.CASCADE)

class BookInfo(models.Model):
    subject=models.CharField(max_length=25)
    chapter=models.IntegerField()

class NewsPaper(models.Model):
    Name=models.CharField(max_length=19)
    Date=models.DateField()

class B_Category(models.Model):
    ch=[
        ('n','Novel'),
        ('p','Programming'),
        ('l','Language')
    ]
    Category=models.CharField(max_length=19,default='n',choices=ch)
    