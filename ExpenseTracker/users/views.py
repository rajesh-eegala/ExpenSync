from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.contrib import messages
from users.models import Options
from .forms import manage_expense_form


# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save()
                messages.success(request, 'User registered successfully')
                return redirect('register')
        else:
            messages.error(request, 'Passwords do not match')
            
    return render(request, 'register.html')


       


    

def login_(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login_(request,user)
            return redirect('/')
    
        else:
            messages.error(request, "Invalid credentials")

        
    return render(request, 'login.html')



def manage_expenses(request):
    if request.method == 'POST':
        form = manage_expense_form(request.POST)
        if form.is_valid():
            form.save()
            redirect('manage_expenses.html')
    else:
        form = manage_expense_form(initial={
            'expense_title': 'New Expense',
            'expense_type': 'Type',
            'amount': 0,
        })

    return render(request, 'manage_expenses.html', {'form': form})

def edit_expense(request,id):
    expense = get_object_or_404(Options, id=id)
    if request.method == 'POST':
        form = manage_expense_form(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = manage_expense_form(instance=expense)
    return render(request, 'edit_expense.html', {'form': form, 'id' : id})

    


def expense_list(request):
    # Fetch all expense records from the database
    expenses = Options.objects.all()

    # Pass the expenses to the template
    return render(request, 'show_expenses.html', {'expenses': expenses})





    