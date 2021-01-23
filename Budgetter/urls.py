from django.contrib import admin
from django.urls import path, include
from .settings import STATIC_ROOT, STATIC_URL
from django.conf.urls.static import static

from Budget.views import history,create,home,signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/signup/', signup, name='signup'),
    path('history/', history, name='history'),
    path('create/', create, name='create'),
    path('account/', include('django.contrib.auth.urls')),
    path('', home, name='home')
   
]+  static(STATIC_URL, document_root=STATIC_ROOT)
