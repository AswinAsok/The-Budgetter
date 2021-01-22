from django.shortcuts import render, redirect
from .models import Budget
from .forms import CreateForm
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
    context['labels'] = labels
    context['data'] = data
    context['Expenditure'] = expenditure*-1
    context['Income'] = income
    context['Total'] = total
    return render(request, 'home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.user.username,request.POST)
        if form.is_valid():
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


        

