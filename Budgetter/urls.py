from django.contrib import admin
from django.urls import path

from Budget.views import history,create,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('history/', history, name='history'),
    path('create/', create, name='create'),
    path('', home, name='home')
]
