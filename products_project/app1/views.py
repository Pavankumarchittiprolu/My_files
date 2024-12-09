from django.shortcuts import render
from app1.forms import *
from app1.models import *


# Create your views here.
def home(request):
    response=render(request,'app1/home.html')
    return response

def add_prod_view(request):
    if request.method=="GET":
        pform=ProductsForm()
        response=render(request,'app1/add_prod.html',context={'pform':pform})
        return response
    elif request.method=="POST":
        pform=ProductsForm(request.POST)
        if pform.is_valid():
            pform.save(commit=True) 
            pform=ProductsForm()
            msg='Product Added.'
            response=render(request,'app1/add_prod.html',context={'pform':pform,'pform':pform,'msg':msg})
            return response
        else:
            response=render(request,'app1/add_prod.html',context={'pform':pform})
            return response
        

def list_prod_view(request):
    prods=Products.objects.all()
    response=render(request,'app1/list_prod.html',context={'prods':prods})
    return response


def edit_prod(request,pid):
    if request.method=='GET':
        p=Products.objects.get(prodId=pid)
        pform=ProductsForm(instance=p)
        response=render(request,'app1/edit_prod.html',context={'pform':pform})
        return response
    
def update_prod(request):
    if request.method=="POST":
        p=Products.objects.get(prodId=request.POST['prodId'])
        pform=ProductsForm(request.POST,instance=p)
        if pform.is_valid():
            pform.save(commit=True)
            msg="Product updated."
        response=render(request,'app1/home.html',context={'msg':msg})
        return response

def delete_prod(request,pid):
    p=Products.objects.get(prodId=pid)
    p.delete()
    msg="Product deleted."
    response=render(request,'app1/home.html',context={'msg':msg})
    return response
    

    


