from django import forms
from .models import Employee, SimCard, Payment

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["name", "email", "status"]

class SimCardForm(forms.ModelForm):
    class Meta:
        model = SimCard
        fields = ["sim_number", "operator", "assigned_to"]

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["employee", "sim_card", "amount"]
