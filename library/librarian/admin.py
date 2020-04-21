from django.contrib import admin
from .models import Book,BookInfo,NewsPaper,B_Category
class Bookadmin(admin.ModelAdmin):
    list_display=['name','isbn','publish_date']
class BookInfoadmin(admin.ModelAdmin):
    list_display=['subject','chapter']
class NewsPaperadmin(admin.ModelAdmin):
    list_display=['Name','Date']
class B_Categoryadmin(admin.ModelAdmin):
    list_display=['Category']     

admin.site.register(Book,Bookadmin)
admin.site.register(BookInfo,BookInfoadmin)
admin.site.register(NewsPaper,NewsPaperadmin)
admin.site.register(B_Category,B_Categoryadmin)