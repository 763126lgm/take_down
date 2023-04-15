from django.contrib import admin
from .models import Nmobes
# Register your models here.

'''如下定义一个模型管理器类'''
class NmobesManager(admin.ModelAdmin):  #类名是自定义的
    #列表页面显示的字段名
    list_display=['id','ask','answer']
    #设置可编辑（超链接）的列，默认只可编辑id字段，如下换成ask字段
    list_display_links=['ask']
    #添加过滤器
    list_filter=['ask']
    #添加搜索框，可进行关键字模糊查询,如下设置只能以id字段进行模糊查询
    search_fields=['id'] 
    #添加可在列表页面编辑的字段,注意不能和list_display_links列表内的值一样
    list_editable=['answer']  
admin.site.register(Nmobes,NmobesManager)  #绑定模型管理器类