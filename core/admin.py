from django.contrib import admin
from .models import Employee, SimCard, Payment

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "status")
    list_filter = ("status",)

@admin.register(SimCard)
class SimCardAdmin(admin.ModelAdmin):
    list_display = ("sim_number", "operator", "assigned_to")

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("employee", "sim_card", "amount", "date")
    list_filter = ("employee",)
