from django.http.response import JsonResponse
from django.shortcuts import render
from HELLO_SAWON.dao_sawon import SawonDao

# Create your views here.


def sawon_list(request):

    se = SawonDao()
    data = {
        'list': se.myselect()
    }

    return render(request, "sawon_list.html", data)


def insert_ajax(request):

    se = SawonDao()

    s_name = request.POST['s_name']
    s_mobile = request.POST['s_mobile']
    dept_name = request.POST['dept_name']
    cnt = se.myinsert(s_name, s_mobile, dept_name)
    msg = "no"

    if cnt > 0:
        msg = "ok"

        data = {
            '이름': s_name,
            '전화번호': s_mobile,
            '부서': dept_name
        }

    return JsonResponse(data)


def update_ajax(request):

    se = SawonDao()

    s_id = request.POST['s_id']
    s_name = request.POST['s_name']
    s_mobile = request.POST['s_mobile']
    dept_name = request.POST['dept_name']
    cnt = se.myupdate(s_id,s_name, s_mobile, dept_name)
    if cnt > 0:
        data = {
            '사번' : s_id,
            '이름': s_name,
            '전화번호': s_mobile,
            '부서': dept_name
        }

    return JsonResponse(data)


def delete_ajax(request):

    se = SawonDao()

    s_id = request.POST['s_id']
    cnt = se.mydelete(s_id)

    if cnt > 0:

        data = {
            '사번': s_id
        }

    return JsonResponse(data)
