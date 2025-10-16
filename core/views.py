from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, SimCard, Payment
from .forms import EmployeeForm, SimCardForm, PaymentForm

def home(request):
    return render(request, "home.html")

# Employee views
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employees/list.html", {"employees": employees})

def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm()
    return render(request, "employees/form.html", {"form": form})

def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "employees/form.html", {"form": form})

# SIM views
def sim_list(request):
    sims = SimCard.objects.all()
    return render(request, "sims/list.html", {"sims": sims})

def sim_create(request):
    if request.method == "POST":
        form = SimCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sim_list")
    else:
        form = SimCardForm()
    return render(request, "sims/form.html", {"form": form})

# Payment views
def payment_list(request):
    payments = Payment.objects.all()
    return render(request, "payments/list.html", {"payments": payments})

def payment_create(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("payment_list")
    else:
        form = PaymentForm()
    return render(request, "payments/form.html", {"form": form})

def dashboard(request):
    context = {
        'total_employees': Employee.objects.count(),
        'total_sims': SimCard.objects.count(),
        'assigned_sims': SimCard.objects.filter(assigned_to__isnull=False).count(),
        'total_payments': Payment.objects.count(),
        'recent_employees': Employee.objects.order_by('-id')[:5],
        'recent_sims': SimCard.objects.order_by('-id')[:5],
        'recent_payments': Payment.objects.order_by('-date')[:5],
    }
    return render(request, 'dashboard.html', context)