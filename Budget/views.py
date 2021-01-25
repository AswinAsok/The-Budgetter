from django.shortcuts import render, redirect
from .models import Budget,MonthlyBudget
from .forms import CreateForm,MonthlyForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def history(request):
    budgets = Budget.objects.filter(user = request.user.id)
    context = {}
    context['Budgets'] = budgets
    total = 0
    for budget in budgets:
        total = total + budget.amount
    context['Total'] = total
    return render(request, 'history.html', context)

def home(request):
    budgets = Budget.objects.filter(user = request.user.id)
    monthly_budget = MonthlyBudget.objects.filter(user = request.user.id)
    total = 0
    income = 0
    expenditure = 0
    for budget in budgets:
        total = total + budget.amount
        if(budget.amount<0):
            expenditure = expenditure + budget.amount
        else:
            income = income + budget.amount

    labels = ['Total','Expenditure']
    data = [total, expenditure]

    if request.method == 'POST':
        form = MonthlyForm(request.user.username,request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = MonthlyForm(request.user.username)

    context = {}
    context['labels'] = labels
    context['form'] = form
    context['data'] = data
    context['hasmbudget'] = monthly_budget.exists()
    if request.user.is_authenticated and monthly_budget.exists():
        context['mbudget'] = monthly_budget[0].max_amount
        context['exceed'] = monthly_budget[0].max_amount - (expenditure*-1)
        
    context['Expenditure'] = expenditure*-1
    context['Income'] = income
    context['Total'] = total
    return render(request, 'home.html', context)

def create(request):
    budgets = Budget.objects.filter(user = request.user.id)
    total = 0
    income = 0
    expenditure = 0

    

    for budget in budgets:
        total = total + budget.amount
        if(budget.amount<0):
            expenditure = expenditure + budget.amount
        else:
            income = income + budget.amount


    if request.method == 'POST':
        form = CreateForm(request.user.username,request.POST)
        if form.is_valid():
            #print(form.cleaned_data['amount'])
            if(form.cleaned_data['amount']< 0 and form.cleaned_data['amount']*-1>total):
                form = CreateForm(request.user.username)
                context = {}
                context['error'] = True
                context['form'] = form
                return render(request,'create.html', context)
            else:
                form.save()
                return redirect('history')

    else:
        form = CreateForm(request.user.username)

        
    context = {}
    context['form'] = form
    return render(request,'create.html', context)

def signup(request):

    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(" I reached here")
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    
    context = {}
    context['form'] = form
    return render(request, 'registration/signup.html', context )


def reset(request):
    MonthlyBudget.objects.filter(user = request.user.id).delete()
    return redirect('home')

def resetall(request):
    Budget.objects.filter(user = request.user.id).delete()
    return redirect('home')

