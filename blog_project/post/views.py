from django.shortcuts import render,redirect
from .models import Post




def HomeView(request):
    form= Post.objects.all()
    context={'form':form}
    return render(request,'home.html',context)

