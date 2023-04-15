from django.shortcuts import render,HttpResponse,redirect
from.models import Tap
# Create your views here.
def test_app01(request):
    return HttpResponse('酒店首页')
def test_app02(request):  #班级信息登录页面,首页访问网址：http://127.0.0.1:8000/winshops/test_001
    if request.method=='GET':
        user=request.COOKIES.get('user')   #检查cookies是否存在
        if user:
            return redirect('/winshops/stud_datasheet')
        return render(request,'shougo/temnib001.html')
    user=request.POST.get('user')
    password=request.POST.get('password')
    print('user:',user)
    print('user的类型',type(user))
    print('password',password)
    if user=='9900' and password=='0000':
        request.session['userid']='user'
        request.session['passwordid']='password'
        rep=redirect('/winshops/stud_datasheet')
        rep.set_cookie('user',9900,620)  #存储cookies
        return rep
    return HttpResponse('用户名或密码错误')
def student_sheet(request): #班级信息主页面
    sutdent=Tap.objects.filter(is_active=True)
    return render(request,'shougo/tap_data.html',locals())
def delect_sheet(request,id):   #删除信息,伪删除
    print('id：',id)
    try:
        delect=Tap.objects.get(id=id,is_active=True) #筛选is_active=True的字段信息
    except:
        print('数据不存在')
        return HttpResponse('请返回页面刷新后重试')  
    delect.is_active=False   #修改该字段的bool值为False
    delect.save()
    return redirect('/winshops/stud_datasheet')
def updates(request,id):  #修改信息
    try:
        table_shett=Tap.objects.get(id=id,is_active=True)
    except print(0):
        print('数据获取失败')
    if request.method=='GET':
        return render(request,'shougo/sheet.html',locals())
    clase=request.POST.get('clase')
    names=request.POST.get('names')
    student_sheet=request.POST.get('stud_number')
    Tap.objects.filter(id=id).update(clase=clase,names=names,stud_number=student_sheet)  #第一种修改方式
    # #修改
    # Tap.clase=clase     #直接字段修改，第二种修改方式
    # Tap.names=names
    # Tap.stud_number=student_sheet
    # #保存
    # Tap.save()  #报错：Exception Value:missing 1 required positional argument: 'self'	
    return redirect('/winshops/stud_datasheet')
def add_sheet(request):  #新增数据
    if request.method=='GET':
        return render(request,'shougo/add.html')
    try:
        clase=request.POST.get('clase')
        print('clase:',clase)
        names=request.POST.get('names')
        print('names',names)
        stud=request.POST.get('stud_number')
        print('stud',stud)
        iu=Tap.objects.filter(clase=clase,names=names,stud_number=stud)
        if iu:
            iu.update(is_active=True)
        else:
            iu.create(clase=clase,names=names,stud_number=stud)
    except:
        print('未知错误')
        ove='数据填写格式错误'
        return render(request,'shougo/add.html',{'ove':ove})   #注意ove这种变量只能使用字典形式传入
    return redirect('/winshops/stud_datasheet')