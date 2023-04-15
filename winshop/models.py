from django.db import models

# Create your models here.
'''创建数据库表'''
class Tap(models.Model):
    clase=models.CharField('班级',max_length=20,default='')
    names=models.CharField('姓名',max_length=20,default='')
    stud_number=models.IntegerField('学号',default='20180000')
    is_active=models.BooleanField('伪删除',default=True)
    class Meta:
        db_table='tap'   #修改表名为“tap"
    def __str__(self):
        return '%s_%s_%s'%(self.clase,self.names,self.stud_number)
class Nmobes(models.Model):
    ask=models.CharField('姓名',max_length=100,default=None)
    answer=models.IntegerField('年龄',default=None)
    def __str__(self):  #使类对象转换成详细的信息描述
        return '%s__%s'%(self.ask,self.answer)
    class Meta:
        db_table='nmobes'
class Mouth(models.Model):
    ddr=models.OneToOneField(Nmobes,on_delete=models.CASCADE) #一对一关系映射,设置成级联删除
    adk=models.CharField('姓名',max_length=100,default=None)
    anbbr=models.IntegerField('年龄',default=None)
    class Meta:
        db_table = 'Mouth'
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
    def __str__(self):
        return '%s__%s'%(self.adk,self.anbbr)
    




'''创建存储文件路径数据表'''
class File_upl(models.Model):
    title=models.CharField('文件标题',max_length=12)
    upload=models.FileField(upload_to='file_upload')  # upload_to='file_upload'表示文件存储子目录,根目录根据配置文件里的设置目录    
