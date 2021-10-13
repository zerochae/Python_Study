from django.shortcuts import render
from HELLO_SAWON.dao_sawon import SawonDao

# Create your views here.

def sawon_list(request) :

    se = SawonDao()
    data = {
        'list' : se.myselect()
    }

    return render(request,"sawon_list.html",data)
