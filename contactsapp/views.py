from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.

def say_hello(request):
    contacts = Contact.objects.all()
    
    return render(request, "contactsapp/index.html", {"contacts": contacts})

    
def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        form.save()
        
        return redirect("/")
    else:
        form = ContactForm()
        
        return render(request, "contactsapp/contact_form.html", {"form": form})
    

def edit_contact(request, id):
    contact = Contact.objects.get(pk=id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        form.save()
        
        return redirect("/")
    else:    
        form=ContactForm(instance=contact)
        
        return render(request, "contactsapp/contact_form.html", {"form": form}) 