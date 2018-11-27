from django.urls import path
from . import views   # ("." = import from current directory)

urlpatterns = [
    path('', views.home, name='test_app-home'),
]