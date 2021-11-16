from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.home),
path('about/',views.about,name='about'),
path('newbooking/',views.newbooking,name="NewBooking"),
path('renewmembership/',views.RenewMembership,name="RenewMembership")

]