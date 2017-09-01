from django.shortcuts import render
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from semtiment import reserch
import os
def reserch(request):
	return render(request,"index.html",locals())
'''
def result(request):
	search_name=request.GET.get("name","")
	results=os.popen('python3 reserch.py %s' %(search_name)).read()
	f=open("/home/jamie/Reserch/semtiment/template/result.html",'wt')
	f.write('{% extends "reserch.html"%}'+'\n')
	f.write("{% block result %}")
	f.write(results)
	f.write("{% endblock%}")
	f.close()
	return render(request,"result.html",locals())
'''


from semtiment.models import ResultsModel
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
def result(request):
    '''
    for res in result:
        if res.get('semtiment')=='pos':
            x.append(res)
    '''
    #result=ResultsModel.objects.exclude(view="%s" %('大众')).values("id","semtiment","view","sentence")
    total=[]
    
    





    x=[]
    search_name=request.GET.get("keyword","")
    semtiment=request.GET.get('semtiment','')
    result=ResultsModel.objects.filter(view="%s" %(search_name)).values("id","semtiment","view","sentence").order_by('id')
    total=[]
    pos=0
    neu=0
    neg=0
    for r in result:
            total.append(r)
            if r['semtiment']=='pos':
                  pos+=1
            elif r['semtiment']=='neg':
                  neg+=1
            else:
                  neu+=1
    if semtiment:
        if semtiment!=None:
            for res in result:
                if res.get('semtiment')==semtiment:
                    x.append(res)
    else:
        '''
         for res in result:
            x.append(res)
        '''
        x=total
    paginator=Paginator(x,20)#分页器
    page= request.GET.get('page',1)
    p=int(page)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        #如果page不是整数，取第一页数据
        contacts = paginator.page(1)
    except EmptyPage:
        #如果page不再范围，取最后一页
        contacts = paginator.page(paginator.num_pages)
    #x=x[(page-1)*20:(page-1)*10+9]
    start_index=(p-1)*20
    end_index=start_index+19
    x=x[start_index:end_index]
    p= (pos/(pos+neu+neg))*100
    u=(neu/(pos+neu+neg))*100
    g=(neg/(pos+neu+neg))*100



    return render(request,"search.html",locals())

   
# Create your views here.
