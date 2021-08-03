from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime
    
def index(request):
    context = {
        "time": strftime("%b %d, %Y", localtime()),
        "hour": strftime("%H:%M %p", localtime()),
    }
    return render(request,'index.html', context)


def second(request, name):
    return HttpResponse('Hola ' + name)

