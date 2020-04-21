from django.contrib import admin
from .models import s_re,s_app
 
class s_re_admin(admin.ModelAdmin):
    list_display=['Enrollment_No','Name','BirthDate','Branch','Mobile_No','Email']
class s_app_admin(admin.ModelAdmin):
    list_display=['Enrollment_No','Name','BirthDate','Branch','Mobile_No','Email','City','Annual_Income']
admin.site.register(s_re,s_re_admin)
admin.site.register(s_app,s_app_admin)