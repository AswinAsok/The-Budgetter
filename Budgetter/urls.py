from django.contrib import admin
from django.urls import path

from Budget.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('history/', home, name='history')
]
