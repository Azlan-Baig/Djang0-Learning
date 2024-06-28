from django.shortcuts import render
from .models import chaiVariery,store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarieryForm
def all_chai(request):
    chais = chaiVariery.objects.all()  #Ye as an array ki form me ayega to html file me looping karna easy huga 
    return render(request,'chai/index.html',{'chais':chais} )


def chai_detail(request,chai_id):
    chai = get_object_or_404(chaiVariery,pk=chai_id)
    return render(request,'chai/chai_detail.html',{'chai':chai})

def chai_store(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarieryForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['cha_varity' ]
            stores = store.objects.filter(chai_varieties=chai_variety)
    else:
         form = ChaiVarieryForm()       
    return render(request,'chai/chai_stores.html',{'stores': stores,'form':form})