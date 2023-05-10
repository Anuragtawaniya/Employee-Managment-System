
from django.urls import path
from employee import views

urlpatterns = [
    path('',views.home,name="home"),
    path('create',views.create,name="create"),
    path('employee',views.employee,name="employee"),
    path('editEmployee/<int:id>',views.editEmployee,name="editEmployee"),
    path('views/<int:id>',views.views,name="views"),
    path('managment',views.managment,name="managment"),

]
