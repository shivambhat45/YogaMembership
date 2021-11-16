from django.shortcuts import render
from YogaForm.models import CompletePayment
from datetime import datetime
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse

def home(request):
    # return HttpResponse("This is my Home Page")
    return render(request,'YogaForm/index.html')

def about(request):
    return render(request,'YogaForm/about.html')

def newbooking(request):
    if request.method=="POST":
        FullName=request.POST.get("FullName")
        Emailaddress=request.POST.get("email")
        Age=request.POST.get("age")
        batch=request.POST.get("batch")
        payment=request.POST.get("payment")
        newbooking=CompletePayment(FullName=FullName,Emailaddress=Emailaddress,Age=Age,batch=batch,payment=payment)
        newbooking.save()
        messages.success(request, 'You have been enrolled into the gym and the payment of Rs 500 is done as well!!!')

    return render(request,'YogaForm/newbooking.html')

def RenewMembership(request):
    return render(request,'YogaForm/renewmembership.html')

def Payment(request):
    return render(request,'YogaForm/payment.html')

