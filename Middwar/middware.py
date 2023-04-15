from django.utils.deprecation import MiddlewareMixin 
'''调用中间件类'''
import re
from django.shortcuts import render,HttpResponse,redirect
'''
继承中间件类MiddlewareMixin
创建什么中间件方法可根据业务需求创建
'''
class Mare(MiddlewareMixin):
    def process_request(self,request):  
        ip_address=request.META['REMOTE_ADDR']   #获取访问者的ip
        path_url=request.path_info   #获取访问者路由
        if not re.match('^/url001',path_url):  #如果请求URL开头不是/url001，则请求被终止
            return      #如果返回为None，则请求已通过路由进入视图
        print('{}访问被接收'.format(ip_address))
        return HttpResponse(f'{ip_address}已被禁止访问')  #如果路由正则匹配失败则返回这行业务逻辑