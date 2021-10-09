from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return render(request, 'home.html')

def home(request):

        if request.GET['param'] == '1' :
            return HttpResponse('<h2>hello  ' + request.GET['param']+'</h2>')
        else : 
            return HttpResponse('1 아님!!!!!!!!!!')