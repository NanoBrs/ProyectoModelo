from django.shortcuts import render
from ProyectoApp.models import Employee
from . import forms
# Create your views here.
def employeeData(request):
    empleados = Employee.objects.all()
    data = {'empleados': empleados}
    return render(request,'ProyectoApp/empleados.html',data)

def UserRegistrationView(request):
    form = forms.UserRegistrationForm(request.POST)
    if form.is_valid():
        print("Forms es valido")
        print("Nombre:",form.cleaned_data["nombre"])
        print("Email:",form.cleaned_data['email'])
        print("Fono:", form.cleaned_data['fono'])
    data = {'form' : form}
    return render(request, 'ProyectoApp/registro.html',data)

