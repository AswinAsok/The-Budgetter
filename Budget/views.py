from django.shortcuts import render, redirect
from .models import Budget
from .forms import CreateForm

# Create your views here.

def history(request):
    budgets = Budget.objects.all()
    context = {}
    context['Budgets'] = budgets
    total = 0
    for budget in budgets:
        total = total + budget.amount
    context['Total'] = total
    return render(request, 'history.html', context)

def home(request):
    budgets = Budget.objects.all()
    total = 0
    income = 0
    expenditure = 0
    for budget in budgets:
        total = total + budget.amount
        if(budget.amount<0):
            expenditure = expenditure + budget.amount
        else:
            income = income + budget.amount


    labels = []
    data = []

    queryset = Budget.objects.order_by('-amount')[:5]
    for budget in queryset:
        labels.append(budget.name)
        data.append(budget.amount)
    context = {}
    context['Total'] = total
    context['Income'] = income
    context['labels'] = labels
    context['data'] = data

    context['Expenditure'] = expenditure
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


        

