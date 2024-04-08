from django.shortcuts import render
from beatbuddy.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect 
from django.urls import reverse
from django.http import JsonResponse
from django.db.models import Case,When


def watchlater(request):
    user = request.user
    
    if request.method == 'POST':
        video_id = request.POST.get('video_id')
        watch = Watchlater.objects.filter(user=user)

        for i in watch:
            if video_id == i.video_id:
                message = "Your music is already added"
                return JsonResponse({'message': message})
                
        else:
            watchlater = Watchlater(user=user, video_id=video_id)
            watchlater.save()
            message = "Your music successfully added"

        # Redirect to songpost view with the video_id
        return redirect(reverse('songpost', args=[video_id]))

    # Handle the 'GET' request
    wl = Watchlater.objects.filter(user=user)
    ids = [i.video_id for i in wl]
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)
    
    return render(request, "beatbuddy/watchlater.html", {'song': song})

    
def songs(request):
    song=Song.objects.all()
    return render(request, "beatbuddy/songs.html", {'song' :song})

def songpost(request,id):
    song=Song.objects.filter(song_id=id).first()
    return render(request, "beatbuddy/songpost.html", {'song' :song})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(username=username, password=password)
        from django.contrib.auth import login
        login(request, user)
        return redirect('/')
    
    return render(request, "beatbuddy/login.html")

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['pass1']
        username = request.POST['username']
        first_name = request.POST['firstname']
        second_name = request.POST['secondname']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = first_name
        myuser.second_name = second_name
        myuser.save()
        user= authenticate(username=username, password=pass1)
        from django.contrib.auth import login
        login(request, user)
        return redirect('/')
    
    return render(request, 'beatbuddy/signup.html')

def about(request):
    return render(request, 'beatbuddy/about.html')
def contact(request):
    return render(request, 'beatbuddy/contact.html')
