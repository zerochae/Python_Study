from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

from HELLO_DJANGO.dao_emp import DaoEmp


# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):

    if request.GET['param'] == '1' :
        return HttpResponse('<h2>hello  ' + request.GET['param']+'</h2>')
    else : 
        return HttpResponse('1 아님!!!!!!!!!!')

def myforward(request):
    str = "1111"
    arr= [1,2,3,4]

    emplist = DaoEmp.myselect()

    print(emplist)

    data = {
        'id' : '1',
        'name' : '홍길동',
        'str' : str,
        'arr' : arr,
        'emplist' : emplist
    }

    return render(request,"myforward.html",data)

def emp_list(request) :

    de = DaoEmp()
    data = {
        'list' : de.myselect() 
    }

    return render(request,"emp_list.html",data)

def insert_ajax(request):
    de = DaoEmp()
    emp_id = request.POST['emp_id']
    emp_name = request.POST['emp_name']
    tel = request.POST['tel']
    address = request.POST['address']
    cnt = de.myinsert(emp_id,emp_name,tel,address);
    msg = "ng"
    if cnt > 0 :
        msg = "ok"
    print(cnt)
    print(msg)
    myjson = {'msg' : msg}
    return JsonResponse(myjson)


