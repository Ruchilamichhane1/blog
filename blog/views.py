
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog,  Message
def home(request):
    return render(request, 'blog/index.html',)

def about(request):
    return render(request, 'blog/about.html',)

def blog(request):
    return render(request, 'blog/blog.html',)

def post_details(request):
    return render(request, 'blog/post-details.html',)

def contact(request):
    return render(request, 'blog/contact.html',)

def post_create(request):
    return render(request, 'blog/post-create.html',)

def save_post(request):
    if request.method == "POST":
        #return HttpResponse(request.POST.items())
        name=request.POST.get('name')
        email=request.POST.get('email')
        title=request.POST.get('title')
        subject=request.POST.get('subject')
        data = Blog( name=name, email=email, title=title, subject=subject)
        data.save()
    return render(request, 'blog/post-details.html',)

def save_message(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data = Message( name=name,email=email, subject=subject, message=message)
        data.save()
    return render(request, 'blog/post-details.html',)

def search(request):
    return render(request, 'blog/post-details.html',)




