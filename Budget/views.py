from django.shortcuts import render
from .models import Budget

# Create your views here.

def home(request):
    Budgets = Budget.objects.all()
    context = {}
    context['Budgets'] = Budgets
    print(Budgets)
    return render(request, 'history.html', context)
