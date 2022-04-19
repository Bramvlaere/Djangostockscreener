from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TickerForm

def index(request):
    if request.method == 'POST':
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            return HttpResponseRedirect(ticker) #will look for ticker inserted based on user input
    else:
        form = TickerForm()

    return render(request, 'index.html', {'form':form})  

def ticker(request,tid):
    context = {}
    context['ticker'] = tid
    return render(request,'ticker.html', context)