from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
  path('', views.homepage, name = 'homepage'),
  path('register/x',views.register, name = 'register')
]