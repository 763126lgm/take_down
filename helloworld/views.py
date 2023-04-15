# from django.http import HttpResponse  #这种方式数据和视图会混合在一起,不符合django模板用法
from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.cache import cache_page
import time
from django.core import mail

@cache_page(60)
def hello(reqest):
    t=time.time()
    return HttpResponse(t)


def hello_is(request):
    # from django.urls import reverse
    # url=reverse('tuen')
    # return redirect(url)
    HttpResponse('中间件测试')

def world(request):
    conten={}
    conten['hello']='Hello World'
    conten['name']='贝乐虎'
    return render(request,'runoob001.html',{"conten":conten})
def test01(request):
    name_lis=[]
    return render(request,'runoob002.html',{'name_lis':name_lis})
def test02(request):
    name_lis={
        '一班':'轻语',
        '二班':'俈古',
        '三班':'天咯',
        }
    return render(request,'runoob003.html',{'name_lis':name_lis})  #不知道为什么这个版本无法直接传入变量，必须以字典形式传参
def saitening(request):
    return render(request,'主模板.html')
def saitening001(request):
    return render(request,'test001.html')
def saitening002(request):
    return render(request,'test002.html')


'''数据分页测试'''
from django.core.paginator import Paginator
import csv
def test_mush(request):
    page_number=request.GET.get('pasg',1)  #获取页码
    toal_data=['历史','政治','地理','天文','数学','军事','物理']  #需要分页的数据内容
    pag=Paginator(toal_data, 2)  #分页初始化，每两条数据作为一页
    print('pag',pag.page_range)
    pag_page=pag.page(int(page_number))  #当前页管理器，page_number表示当前页的页码，并且必须是整型
    print('分页后的数据对象：',pag_page)
    print('分页后的数据对象类型：',type(pag_page))
    print('页码：',pag_page.number)
    return render(request,'数据分页测试.html',locals())

'''浏览器下载文件'''
def down_csv(request):
    page_number=request.GET.get('pasg',1)  #获取页码
    toal_data=['a','b','c','d','e','f','g']  #需要分页的数据内容
    pag=Paginator(toal_data, 2)  #分页初始化，每两条数据作为一页
    pag_page=pag.page(int(page_number))
    req=HttpResponse(content_type='text/csv')  #指定响应头content_type告诉浏览器为csv文件
    req['Content-Disposition']='attachment;filename="liter.csv"'  #告诉浏览器应该开启另存为
    for ad in pag_page:
        writer=csv.writer(req)  #执行可写
        writer.writerow(ad)  #执行按行写入文件内容
    return req


'''浏览器上传文件'''
from winshop.models import File_upl  #调用模型类
def file_upload(request):
    if request.method=='GET':
        return render(request,'file_upload.html')
    # title=request.POST['title']  #这种方式获取，如果字段不存在就会报错
    title=request.POST.get('title',110)  #最好的获取方式，如果字段不存在也不会报错，只是给个默认值110
    myfile=request.FILES['Myfile']  #获取文件对象
    File_upl.objects.create(title=title,upload=myfile)
    print(myfile.name)  #打印文件名
    return HttpResponse('上传文件 "%s" 成功'%(myfile.name))


'''邮件发送实例'''
def mail_tran(request):
    mail.send_mail(subject='linux配置文件',
    message='linux防火墙配置',  #邮件内容
    from_email='1976763852@qq.com',   #邮件发送者 ,注意这里的邮件发送者一定要和配置文件中一致
    recipient_list=['1976763852@qq.com']  #邮件接收者
    )
    return HttpResponse('邮件发送成功')
                
    