from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import BlogForms,RoomForm
from django.http import HttpResponse
from .models import Blog,Room,Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def home(request):
    blogs=Blog.objects.all()
    context={'blogs':blogs}
    return render(request, 'index.html',context)

def blogpost(request,pk):
    blog=Blog.objects.get(id=pk)
    context={'blog':blog}
    return render(request, 'blogpost.html',context)

@login_required(login_url='login')
def blogadd(request):
    form = BlogForms()
    if request.method=='POST':
        myData=BlogForms(request.POST)
        if myData.is_valid():
            myData.save()
            messages.success(request,"Blog created.")
            return redirect("home")

    context={'form':form}
    return render(request,'blogadd.html',context)

def loginPage(request):

    page = 'login'
    if request.method=='POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,"Username OR password is invalid")
        
        user=authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Username OR password is invalid')
    
    if request.user.is_authenticated:
        return redirect('home')

    context={'page':page}
    return render(request,'login_register.html',context)

def logoutPage(request):
    logout(request)
    return redirect('home')

def registerPage(request):

    if request.method=='POST':
        user=request.POST['Name']
        e_mail=request.POST['email']
        password1=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        if password1==confirmpassword:
            if not User.objects.filter(username=user).exists():
                if not User.objects.filter(email=e_mail).exists():           
                    user=User.objects.create_user(username = user, email = e_mail, password=password1)
                    user.save()

                    login(request,user)
                    return redirect('home')
        else:
            messages.error(request,'An error occurred')

    context={}
    return render(request,'login_register.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    room_messages=room.message_set.all()
    participants=room.participants.all()

    if request.method=="POST":
        message=Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    context={'room':room, 'room_messages':room_messages, 
    'participants':participants}
    return render(request,"room.html",context)

def createRoom(request):
    form=RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room=form.save(commit=False)
            room.host=request.user
            room.save()
            return redirect('home')

    context={'form':form}
    return render(request, 'room_form.html',context)

def UpdateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user!=room.host:
        return HttpResponse("You are not allowed to change this room")

    if request.method == 'POST':
        form = RoomForm(request.POST or None,instance=room)
        if form.is_valid():
            form.save()
            return redirect('roomforum')

    context={'form':form}
    return render(request, "roomadd.html",context)

def DeleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.user!=room.host:
        return HttpResponse("You are not allowed to change this room")
    if request.method=='POST':
        room.delete()
        return redirect('roomforum')
    context={"obj":room}
    return render(request, "delete.html",context)

def roomforum(request):
    rooms=Room.objects.all()
    context={"rooms":rooms}
    return render(request,'roomforum.html',context)

def blogroom(request):
    blogs=Blog.objects.all()
    context={"blogs":blogs}
    return render(request,'blogroom.html',context)

def donations(request):
    return render(request,'donations.html')

def aboutcancer(request):
    return render(request,'aboutcancer.html')

def delete_message(request,pk):
    message=Message.objects.get(id=pk)
    if request.user!=message.user:
        return HttpResponse("You are not allowed to change this room")
    if request.method=='POST':
        message.delete()
        return redirect('home')
    context={"obj":message}
    return render(request, "delete.html",context)

def userProfile(request,pk):
    user = User.objects.get(id=pk)
    rooms=user.room_set.all()
    room_messages=user.message_set.all()
    #topics=Topic.objects.all()
    context={'user':user,'rooms':rooms,'room_messages':room_messages}

    return render(request,'profile.html',context)

def search(request):
    query=request.GET['query']
    posts=Blog.objects.filter(title__icontains=query)
    context={"blogs":posts}
    return render (request,'search.html',context)

def searchroom(request):
    query=request.GET['query']
    posts=Room.objects.filter(name__icontains=query)
    context={"rooms":posts}
    return render (request,'searchroom.html',context)