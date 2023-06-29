from django.shortcuts import render, redirect
from .models import Post

def home(request):

    post_list = Post.objects.all()
    context = {
        'post_list':post_list ,
    }

    return render(request, 'index.html', context)

def delete(request, id):
    return render(request, 'post/delete.html')

def update(request, id):
    return render(request,'post/form.html')

def create(request):
    if request.method =="GET":
        return render(request,'post/form.html')
    else:
        img = request.FILES.get('image')
        content = request.POST.get('content')

        Post.objects.create(
            img = img,
            content=content,
            writer = request.user
        )
        return redirect('home')
    

def list(request):
    post_list = Post.objects.all()
    context = {
        'post_list':post_list ,
    }
    return render(request,'post/list.html', context)

def detail(request, id):
    return render(request,'post/detail.html')