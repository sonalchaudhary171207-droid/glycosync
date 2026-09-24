from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse("GlycoSync API Server is Running!")),
    path('admin/', admin.site.urls),
    path('api/', include('clinical.urls')),
]