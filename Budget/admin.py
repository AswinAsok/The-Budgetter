from django.contrib import admin
from .models import Budget, MonthlyBudget

# Register your models here.

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'date',)
    search_fields = ('name','amount','date')

    class Meta:
        model = Budget

admin.site.register(MonthlyBudget)
admin.site.register(Budget,BudgetAdmin)
