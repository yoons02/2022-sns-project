from django.contrib.auth.models import User
from main.models import *
from django.shortcuts import render, get_object_or_404, redirect
from .models import User

def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    #로그인한 유저이름과 글 작성자 이름이 동일한 글 필터링

    posts=Post.objects.filter(writer=user)
    like_list = Like.objects.filter(user = user)
    dislike_list = Dislike.objects.filter(user = user)

    context= {
        'like_list' : like_list,
        'dislike_list' : dislike_list,
        'posts':posts,
        'user':user,
        'blogs':Blog.objects.filter(writer=user),
        'followings' :user.profile.followings.all(),
        'followers' :user.profile.followers.all(),
    }

    return render(request,'users/mypage.html',context)

def follow(request, id):
    user=request.user
    followed_user=get_object_or_404(User, pk=id)
    is_follower=user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)
