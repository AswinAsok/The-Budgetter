from django.contrib import admin
from django.urls import path, include

from Budget.views import history,create,home,signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/signup/', signup, name='signup'),
    path('history/', history, name='history'),
    path('create/', create, name='create'),
    path('account/', include('django.contrib.auth.urls')),
    path('', home, name='home')
   
]
