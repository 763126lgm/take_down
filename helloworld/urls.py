"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),   #django管理界面必须的url,不能注释
    path('url1/',views.hello,name='tuen'),
    path('url001/',views.hello_is),
    path('url2/',views.world,name='tur'),
    path('test_001',views.test01),
    path('test_002',views.test02),
    path('sai/',views.saitening),
    path('sai001/',views.saitening001),
    path('sai002/',views.saitening002),
    path('test_mu',views.test_mush),
    path('down_csv',views.down_csv),
    path('file_up',views.file_upload),
    path("mail_tran/",views.mail_tran),
    path('winshops/',include('winshop.urls'))
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)