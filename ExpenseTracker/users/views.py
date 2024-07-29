from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from users.models import Options
from .forms import manage_expense_form
from django.views.decorators.http import require_GET
from django.db.models import Sum, Count

@require_GET
def custom_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login or any other page after logout

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
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            
    return render(request, 'register.html')


       


    

def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
            # If user exists, try authenticating
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Wrong password. Please try again.")
                return render(request, 'login.html')
        
        except User.DoesNotExist:
            # If user does not exist
            messages.error(request, "You don't have an account, Sign Up Now!")
            return redirect('register')
    
    return render(request, 'login.html')


@login_required
def manage_expenses(request):
    if request.method == 'POST':
        form = manage_expense_form(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)  # Create an instance but don't save it yet
            expense.user = request.user        # Set the user to the currently logged-in user
            expense.save()   
            messages.success(request, 'Expense added successfully')                  # Now save the instance
            return redirect('manage_expenses') # Redirect to a URL name, not a template

    else:
        form = manage_expense_form(initial={
            'expense_title': '',
            'expense_type': '',
            'date':'',
            'amount': 0,
        })

    return render(request, 'manage_expenses.html', {'form': form})

@login_required
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


@login_required
def delete_expense(request, id):
    expense = get_object_or_404(Options, id=id)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'delete_expense.html', {'expense': expense})

    

@login_required
def expense_list(request):
    # Fetch all expense records from the database
    user_expenses = Options.objects.filter(user=request.user)

    # Pass the expenses to the template
    return render(request, 'show_expenses.html', {'expenses': user_expenses})

def summary(request):
    if request.user.is_authenticated:
        total_expenses = Options.objects.filter(user=request.user).aggregate(
            total_amount=Sum('amount'),
            total_count=Count('id')
        )
        expenses_by_category = Options.objects.filter(user=request.user).values('expense_type').annotate(
            category_count=Count('id'),
            category_amount=Sum('amount')
        )
    else:
        total_expenses = {'total_amount': 0, 'total_count': 0}
        expenses_by_category = []

    context = {
        'total_expenses': total_expenses,
        'expenses_by_category': expenses_by_category
    }
    return render(request, 'summary.html', context)



    