from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'website/index.html')
def about(request):
    return HttpResponse("Hello World You are at chai aur code Aboutpage.")
def contact(request):
    return HttpResponse("Hello World You are at chai aur code contact page.")

