from django.shortcuts import render

# Create your views here.


def Index(request):
    return render(request,'index.html')

def Home(request):
    return render(request,'index.html')

def Generic(request):
    return render(request,'generic.html')

def Elements(request):
    return render(request,'elements.html')

def Contact(request):
    return render(request,'contact.html')