from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import Employee
from .forms import EmployeeForm
import json
# Create your views here.
def home(request):
   context = {'totalEmp':Employee.objects.all().count(),'is_leave':Employee.objects.all().filter(on_leave=True)}
   return render(request,'home.html',context)

def create(request):
   form = EmployeeForm()
   if request.method == "POST":

      form = EmployeeForm(request.POST)

      if form.is_valid():
         print("Hello World")
         form.save()
         return redirect("home")
      
   return render(request,'CreateEmployee.html',{'form':form})

def employee(request):
   if request.method=="POST":
      emp_id = request.POST.get("emp_id")
      emp = Employee.objects.get(id=emp_id)
      if "leave" in request.POST:
         emp.on_leave = True
         emp.leaveCount+=1
         emp.save()
         return redirect("employee")
      else:
         emp.is_active = not emp.is_active
         emp.save()
         return redirect("employee")
   employee = Employee.objects.all()
   form = EmployeeForm()
   return render(request,'employee.html',{'totalEmp':Employee.objects.all().count(),'employee':employee,'form':form})


def editEmployee(request,id):
   emp = Employee.objects.get(id=id) 
   form = EmployeeForm(instance=emp) 
   if request.method == "POST":
      form = EmployeeForm(request.POST,instance=emp) 
       
      if form.is_valid():
         form.save()
         return redirect('/employee')

   return render(request,'update.html',{'form':form})


def views(request,id):
   emp = Employee.objects.get(id=id)
   
   if "leave" in request.POST:
         emp.on_leave = True
         emp.leaveCount+=1
         emp.save()
   
   return render(request,'view.html',{'employee':emp})



def managment(request):
   try:
      with open('management.json') as f:
         data = json.load(f)
   except:
      data = {}
      

  
   context = {
      'jsonData': json.dumps(data),
      'docstats': data['docstats']
   }
   context.update(data)

   return render(request, 'index.html', context)

