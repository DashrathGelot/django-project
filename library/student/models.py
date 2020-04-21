from django.db import models

class Stinfo(models.Model):
    name=models.CharField(max_length=50)
    enroll_n=models.IntegerField()
    birth_date=models.DateField(default='2019-06-27')

    def __str__(self):
        return self.name

class BookIssueInfo(models.Model):
    B_name=models.CharField(max_length=25,default='')
    Date=models.DateField()
    report=models.ForeignKey(Stinfo,on_delete=models.CASCADE,verbose_name="Book Info")

class Choice_fill(models.Model):
    ch=[
        ('n','Novel'),
        ('p','Programming'),
        ('l','Language')
    ]
    Category=models.CharField(max_length=19,default='n',choices=ch)