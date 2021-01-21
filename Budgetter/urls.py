from django.contrib import admin
from django.urls import path

from Budget.views import history,create,home,signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('history/', history, name='history'),
    path('create/', create, name='create'),
    path('', home, name='home')
   
]
