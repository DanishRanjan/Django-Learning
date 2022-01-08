from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable1" : "This is variable1 sent",
        "variable2" : "Danish is great"
    }
    # messages.success(request, "this is debugging message")
    return render(request, 'index.html', context)
    # return HttpResponse("This is Homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is About page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is Service Page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        desc = request.POST.get('desc')
        # import ipdb // python debugger
        # ipdb.set_trace()
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
        
    return render(request, 'contact.html')
    # return HttpResponse("This is Contact page")        
