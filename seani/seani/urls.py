
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exam/', include('exam.urls')) ,
    path('',include('home.urls')),
    path('accounts', include('django.contrib.auth.urls'))
]
