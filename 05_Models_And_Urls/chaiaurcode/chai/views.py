from django.shortcuts import render
from .models import chaiVariery
from django.shortcuts import get_object_or_404
def all_chai(request):
    chais = chaiVariery.objects.all()  #Ye as an array ki form me ayega to html file me looping karna easy huga 
    return render(request,'chai/index.html',{'chais':chais} )


def chai_detail(request,chai_id):
    chai = get_object_or_404(chaiVariery,pk=chai_id)
    return render(request,'chai/chai_detail.html',{'chai':chai})