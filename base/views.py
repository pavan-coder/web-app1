from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

rooms = [
    {'id':1,  'tenant':'gunadeep', 
     'address':"Daba-Garden Rd, 104 Area, Visakhapatnam, Andhra Pradesh 530004"},
    {'id':2,'tenant':'sunil', 
     'address':"Daba-Garden Rd, 104 Area, Visakhapatnam, Andhra Pradesh 530004"},
    {'id':3,'tenant':'ganesh', 
     'address':"Daba-Garden Rd, 104 Area, Visakhapatnam, Andhra Pradesh 530004"},
    {'id':4,'tenant':'lokesh', 
     'address':"Daba-Garden Rd, 104 Area, Visakhapatnam, Andhra Pradesh 530004"},
    {'id':5,'tenant':'pavan kumar', 
     'address':"Daba-Garden Rd, 104 Area, Visakhapatnam, Andhra Pradesh 530004"},
    
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html',context )

def room(request, pk):
    room =None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    return render(request, 'base/room.html', context)

def create_tenant_Room(request):
    form = RoomForm()
    if request.method == 'POST':
        form =RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request, "base/room_form.html", context)


def update_tenant_room(request,pk):
    room = Room.objects.get(id=pk)
    form =RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
             form.save()
             return redirect('home')
    context={'form':form}
    return render(request, 'base/room_form.html', context)

def delete_tenant_room(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})

def user_login_page(request):
    if request.method == 'POST':
        mobile_no = request.POST.get('mobile number')
        password = request.POST.get('password')        
        #try:
            #user = User.objects.get(mobile_no=mobile_no)
        
    context ={}
    return render(request, "base/create_post_form.html",context)
    