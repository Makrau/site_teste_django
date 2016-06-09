from django.shortcuts import render
from django import http
from polls.models import Poll

# Create your views here.

def my_view(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    name = poll.name
    description = poll.description

    information = {
        'name' : name,
        'description' : description,
    }

    return render(request, 'polls/my_view.html', information)
    #return http.HttpResponse(html % (name, description))

def demo_view(request, arg1, arg2):
    html = '<html><body><h1>Olá Mundo %s </h1></body></html>'
    N1 = 0
    N2 = 0

    if(arg1):
        N1 = int(arg1)
    
    if(arg2):
        N2 = int(arg2)

    N = int(arg1) + int(arg2)


    return http.HttpResponse(html % N)