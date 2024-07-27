from django import forms
from .models import Options

class manage_expense_form(forms.ModelForm):
    class Meta:
        model = Options
        fields = ['expense_title','expense_type','amount']