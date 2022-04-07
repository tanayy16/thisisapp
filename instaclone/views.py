from django.shortcuts import render, redirect
from .models import User, Photo, Followers
from .forms import *
from django.contrib.auth import authenticate, login, logout as dlogout


def ajaxsignup(request):
    ajax = AjaxSignUp(request.POST)
    context = {'ajax_output': ajax.output()}
    return render(request, 'ajax.html', context)


def ajaxlogin(request):
    ajax = AjaxLogin(request.POST)
    logged_in_user, output = ajax.validate()
    if logged_in_user != None:
        login(request, logged_in_user)
    context = {'ajax_output': output}
    return render(request, 'ajax.html', context)


def signup(request):
    context = {}
    return render(request, 'sign-up.html', context)


def home(request):
    context = {}
    if request.user.is_authenticated:
        u = User.objects.filter(username=request.user.username)[0]
        if u.profilepic == "":
            u.profilepic = "static/assets/img/default.png"
        context = {'user': request.user, 'ProfilePic': u.profilepic}
        return render(request, 'logged-in-index.html', context)
    return render(request, 'index.html', context)


def ajaxsavephoto(request):
    ajax = AjaxSavePhoto(request.POST, request.user)
    context = {'ajax_output': ajax.output()}
    return render(request, 'ajax.html', context)


def ajaxphotofeed(request):
    ajax = AjaxPhotoFeed(request.GET, request.user)
    context = {'ajax_output': ajax.output()}
    return render(request, 'ajax.html', context)


def ajaxprofilefeed(request):
    ajax = AjaxProfileFeed(request.GET, request.user)
    context = {'ajax_output': ajax.output()}
    return render(request, 'ajax.html', context)


def profile(request, username):
    if User.objects.filter(username=username).exists():
        u = User.objects.filter(username=username)[0]

        if not Followers.objects.filter(user=username, follower=request.user.username).exists():
            following = "Follow"
            cls = "btn-p"
        else:
            following = "Following"
            cls = "btn-t"

        if u.profilepic == "":
            u.profilepic = "static/assets/img/default.png"

        followers_p = 0
        following_p = 0
        posts = 0

        name = u.name
        bio = u.bio


        posts = Photo.objects.filter(owner=username)
        posts = len(posts)

        followers_p = len(Followers.objects.filter(user=username))
        following_p = len(Followers.objects.filter(follower=username))

        context = {
            'ProfilePic': u.profilepic, "whosprofile": username, "logged_in_as": request.user.username, "following": following, "cls":cls, "posts":posts, "followers_p":followers_p, "following_p": following_p,"name":name, "bio":bio
        }

        if request.user.is_authenticated:
            return render(request, 'logged-in-profile.html', context)
        return render(request, 'profile.html', context)


def logout(request):
    context = {}
    dlogout(request)
    return redirect(home)


def ajaxsetprofilepic(request):
    ajax = AjaxSetProfilePic(request.POST, request.user)
    context = {'ajax_output': ajax.output()}
    return render(request, 'ajax.html', context)

def ajaxlikephoto(request):
    ajax = AjaxLikePhoto(request.GET, request.user)
    context = {'ajax_output': ajax.output()}
    return render(request, 'ajax.html', context)

def ajaxfollow(request):
    ajax = AjaxFollow(request.GET,request.user)
    context = {'ajax_output': ajax.output()}
    return render(request, 'ajax.html', context)

