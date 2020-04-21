from django.contrib import admin
from .models import t_data,t_register

class t_data_admin(admin.ModelAdmin):
    list_display=['d']
class t_register_admin(admin.ModelAdmin):
    list_display=['t_id','Name','Mo','Email']

admin.site.register(t_register,t_register_admin)
admin.site.register(t_data,t_data_admin)
