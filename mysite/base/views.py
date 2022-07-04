from django.http import HttpResponse
from django.shortcuts import render
from .models import Room
#from django.http import HttpResponse

rooms = [
    {'id':1, 'name': 'Lets learn python!'},
    {'id':2, 'name': 'Design with me'},
    {'id':3, 'name': 'Frontend developers'},
]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    #return HttpResponse('ROOM')
    return render(request,'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=str(pk))

    context = {'room': room}        #context dictionary
    return render(request, 'base/room.html',context)