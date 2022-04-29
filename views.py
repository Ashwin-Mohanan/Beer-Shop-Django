
from dataclasses import field
from django.urls import reverse_lazy
from testapp.models import Beer
from django.shortcuts import render,HttpResponse
from django.views.generic import View,CreateView,ListView,DetailView,DeleteView,UpdateView

# Create your views here.
class BeerView(View):
    def get(self,request):
        return render( request,'testapp/home.html')
class BeerCreate(CreateView):
    model=Beer
    fields=('Bname','Taste','color','price')
class BeerList(ListView):
    model=Beer
class BeerDetails(DetailView):
    model=Beer
class BeerDelete(DeleteView):
    model=Beer
    success_url=reverse_lazy('list')
class BeerUpdate(UpdateView):
    model=Beer
    fields=('Bname','Taste','color','price')