from django.shortcuts import render
from ProyectoApp.models import Employee
# Create your views here.
def employeeData(request):
    empleados = Employee.objects.all()
    data = {'empleados': empleados}
    return render(request,'ProyectoApp/empleados.html',data)

