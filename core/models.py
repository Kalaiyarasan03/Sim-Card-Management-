from django.db import models

class Employee(models.Model):
    STATUS_CHOICES = (('active', 'Active'), ('inactive', 'Inactive'))
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    def __str__(self): return f"{self.name} ({self.status})"

class SimCard(models.Model):
    sim_number = models.CharField(max_length=20, unique=True)
    operator = models.CharField(max_length=50)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self): return f"{self.sim_number} - {self.operator}"

class Payment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, limit_choices_to={'status': 'active'})
    sim_card = models.ForeignKey(SimCard, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.employee.name} paid {self.amount} on {self.date.strftime('%Y-%m-%d')}"
