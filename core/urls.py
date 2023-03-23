
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('search.urls'), name='search'),
    path('admin/', admin.site.urls),
]
