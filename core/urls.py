from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("employees/", views.employee_list, name="employee_list"),
    path("employees/add/", views.employee_create, name="employee_create"),
    path("employees/<int:pk>/edit/", views.employee_edit, name="employee_edit"),
    path("sims/", views.sim_list, name="sim_list"),
    path("sims/add/", views.sim_create, name="sim_create"),
    path("payments/", views.payment_list, name="payment_list"),
    path("payments/add/", views.payment_create, name="payment_create"),
    path("", views.dashboard, name="dashboard"),
]
