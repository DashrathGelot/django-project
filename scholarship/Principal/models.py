from django.db import models
from Student.models import s_app

class t_register(models.Model):
    t_id=models.IntegerField(verbose_name='Id')
    Name=models.CharField(max_length=26)
    Mo=models.IntegerField(verbose_name='Mobile No')
    Email=models.EmailField()

    def __str__(self):
        return self.Name
     
class t_data(models.Model):
    d=models.ForeignKey(s_app,on_delete=models.CASCADE)
