from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ContactForm

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
      # this is all for making a  user
      if request.method=="POST":
        form= ContactForm(request.POST)
        if form.is_valid() :
               form.save()
               print ('Form Saved')
               return redirect ('/index')

      else:   
            form= ContactForm(request.POST)
            return render(request, 'contact.html', {'form':form} )
   