from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.

def say_hello(request):
    contacts = Contact.objects.all()
    
    return render(request, "contactsapp/index.html", {"contacts": contacts})
    
def add_contact(request):
    form = ContactForm()
    return render(request, "contactsapp/add_contact.html", {"form": form})
    
def add_contact_confirm(request):
    
    form = ContactForm(request.POST)
    form.save()
    
    return redirect("/")
    
def edit_contact(request, id):
    if request.method == "POST":
        contact = Contact.objects.get(pk-id)
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:    
        form=ContactForm(instance=contact)
        return render(request, "contactsapp/add_contact.html", {"form": form}) 