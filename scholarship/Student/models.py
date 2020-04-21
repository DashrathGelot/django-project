from django.db import models

class s_re(models.Model):
    Enrollment_No=models.IntegerField(max_length=16,default='',verbose_name='Enrollment No')
    Name=models.CharField(max_length=25)
    BirthDate=models.DateField(default='')
    ch=[
        ('c','Computer'),
        ('m','Mechanical'),
        ('e','Electrical'),
        ('ci','Civil'),
        ('ch','Chemical')
    ]
    Branch=models.CharField(max_length=22,default='c',choices=ch) 
    Mobile_No=models.IntegerField(max_length=10,verbose_name='Mobile No')
    Email=models.EmailField()
class s_app(models.Model):
    Enrollment_No=models.IntegerField(max_length=16,default='',verbose_name='Enrollment No')
    Name=models.CharField(max_length=25)
    BirthDate=models.DateField(default='')
    ch=[
        ('c','Computer'),
        ('m','Mechanical'),
        ('e','Electrical'),
        ('ci','Civil'),
        ('ch','Chemical')
    ]
    Branch=models.CharField(max_length=22   ,choices=ch) 
    Mobile_No=models.IntegerField(max_length=10,verbose_name='Mobile No')
    Email=models.EmailField()
    City=models.CharField(max_length=22,verbose_name='City',default='')
    Annual_Income=models.IntegerField()

    def __str__(self):
        return str(self.Enrollment_No)