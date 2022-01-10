from django.urls import path
from . import views

urlpatterns = [
    path('', views.create, name='create'),
    path('sign-up/', views.sign_up, name='sign_up'),

]