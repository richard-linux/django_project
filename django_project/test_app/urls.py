from django.urls import path
from . import views   # ("." = import from current directory)

urlpatterns = [
    path('home/', views.home, name='test_app-home'),
    path('', views.base, name='test_app-base')
]