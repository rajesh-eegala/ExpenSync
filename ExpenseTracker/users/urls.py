# myapp/urls.py
from django.urls import path

from . import views


urlpatterns = [
   
    path('', views.home, name='home'),
    
    path('login/', views.login_, name='login'),
    
    path('register/', views.register, name='register'),

    path('expense_list/', views.expense_list, name='expense_list'),
    path('manage_expenses/', views.manage_expenses, name='manage_expenses'),
    path('expense/<int:id>/edit/', views.edit_expense, name='edit_expense'),
    path('expense_edit/', views.edit_expense, name='edit_expense'),
    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
    path('logout/', views.custom_logout, name='logout'),
    path('summary/', views.summary, name='summary'),

]
