from django.shortcuts import render, redirect
from .models import Budget
from .forms import CreateForm

# Create your views here.

def history(request):
    Budgets = Budget.objects.all()
    context = {}
    context['Budgets'] = Budgets
    print(Budgets)
    return render(request, 'history.html', context)

def home(request):
    budgets = Budget.objects.all()
    total = 0
    for budget in budgets:
        total = total + budget.amount
    
    context = {}
    context['Total'] = total
    return render(request, 'home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('history')

    else:
        form = CreateForm()

        
    context = {}
    context['form'] = form
    return render(request,'create.html', context)


        

