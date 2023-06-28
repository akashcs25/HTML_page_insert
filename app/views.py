from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def topic(request):
    if request.method=='POST':
        us=request.POST['username']
        pw=request.POST['password']
        print(us)
        print(pw)
        return HttpResponse("Hello World")

    return render(request,'topic.html')

def topic_add(request):
    if request.method == 'POST':
        topic=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('one row added')
    return render(request,'topic_add.html')
