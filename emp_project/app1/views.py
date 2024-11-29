from django.shortcuts import render
from app1.models import *

# Create your views here.
def home(request):
    response=render(request,'app1/home.html')
    return response


def add_emp(request):
    qs=dept.objects.all()
    dpt=[]
    for row in qs:
        dpt.append(row.deptno)
    response=render(request,'app1/add_emp.html',context={'dpt':dpt})
    return response

def delete_emp(request):
    response=render(request,'app1/delete_emp.html')
    return response

def add_dept(request):
    response=render(request,'app1/add_dept.html')
    return response

def display_dept(request):
    response=render(request,'app1/display_dept.html')
    return response

def add_dept_view(request):
    dno=int(request.GET['deptno'])
    dname=request.GET['deptname']
    try:
        d=dept.objects.create(deptno=dno,deptname=dname)
        d.save()
        msg="Dept Added."
    except:
        msg="Error in adding dept."
    response=render(request,'app1/add_dept.html',context={'msg':msg})
    return response

def display_dept_view(request):
    qs=dept.objects.all()
    response=render(request,'app1/display_dept.html',context={'qs':qs})
    return response

def add_emp_view(request):
    eno=request.GET['empno']
    empname=request.GET['empname']
    j=request.GET['job']
    s=request.GET['sal']
    d=request.GET['deptno']
    try:
        deptno=dept.objects.get(deptno=d)
        qs=Emp.objects.create(empno=eno,ename=empname,job=j,sal=s,dept=deptno)
        msg="Emp Added."
    except:
        msg="Invalid."
    response=render(request,'app1/add_emp.html',context={'msg':msg})
    return response

def delete_emp_view(request):
    eno=request.GET['empno']
    try:
        qs=Emp.objects.get(empno=eno)
        qs.delete()
        msg="Emp deleted."
    except:
        msg="Invalid Empno."
    response=render(request,'app1/delete_emp.html',context={'msg':msg})
    return response

def display_emp_view(request):
    qs=Emp.objects.all()
    
    response=render(request,'app1/display_emp.html',context={"qs":qs})
    return response





