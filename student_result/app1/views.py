from django.shortcuts import render
from app1.models import students

# Create your views here.
def home(request):
    response=render(request,'app1/home.html')
    return response

def add_marks(request):
    response=render(request,'app1/add_marks.html')
    return response

def update_marks(request):
    response=render(request,'app1/update_marks.html')
    return response

def find_result(request):
    response=render(request,'app1/find_result.html')
    return response

def delete_stud(request):
    response=render(request,'app1/delete_stud.html')
    return response

def view_results(request):
    response=render(request,'app1/view_results.html')
    return response

def add_stud_view(request):
    r=request.GET['rno']
    n=request.GET['name']
    s1=request.GET['sub1']
    s2=request.GET['sub2']
    qs=students.objects.filter(rollno=r)
    if len(qs)==0:
        m1=students(rollno=r,name=n,subject1=s1,subject2=s2)
        m1.save()
        msg="Student added"
    else:
        msg="Roll no already exists."
    response=render(request,"app1/add_marks.html",context={'msg':msg})
    return response

def update_stud_view(request):
    r=int(request.GET['rno'])
    s1=float(request.GET['sub1'])
    s2=float(request.GET['sub2'])
    try:
        qs=students.objects.get(rollno=r)
        qs.subject1=s1
        qs.subject2=s2
        qs.save()
        msg="Updated successfully"
    except:
        msg="Invalid rollno"
    response=render(request,'app1/update_marks.html',context={'msg':msg})
    return response

def find_result_view(request):
    r=request.GET['rno']
    if r!='':
        try:
            qs=students.objects.get(rollno=int(r))
            s1=qs.subject1
            s2=qs.subject2
            n=qs.name
            r1="Pass" if float(s1)>=40 else "Fail"
            r2="Pass" if float(s2)>=40 else "Fail"
            response=render(request,"app1/find_result.html",context={'r':r,'name':n,'s1':s1,'s2':s2,'r1':r1,'r2':r2})
        except:
            response=render(request,'app1/find_result.html',context={'msg':"Invalid rollno"})
    else:
        response=render(request,'app1/find_result.html',context={'msg':"Rollno cannot be empty"})
    return response

def delete_stud_view(request):
    r=request.GET['rno']
    if r!='':
        try:
            qs=students.objects.get(rollno=int(r))
            qs.delete()
            response=render(request,"app1/delete_stud.html",context={'msg':"Student deleted."})
        except:
            response=render(request,"app1/delete_stud.html",context={'msg':"Invalid rollno"})
    else:
        response=render(request,'app1/delete_stud.html',context={'msg':"Rollno cannot be empty"})
    return response
       
def display_results_view(request):
    qs=students.objects.all()
    if len(qs)!=0:
        response=render(request,'app1/view_results.html',context={"qs":qs})
    else:
        response=render(request,"app1/view_results.html",context={"msg":"No details to display."})
    return response


