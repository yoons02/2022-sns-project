from django.shortcuts import render
from django.contrib.auth.models import User
from main.models import *

def mypage(request):
    user=request.user
    #로그인한 유저이름과 글 작성자 이름이 동일한 글 필터링

    posts=Post.objects.filter(writer=user)
    like_list = Like.objects.filter(user = user)
    dislike_list = Dislike.objects.filter(user = user)

    context= {
        'like_list' : like_list,
        'dislike_list' : dislike_list,
        'posts':posts,
    }

    return render(request,'users/mypage.html',context)

