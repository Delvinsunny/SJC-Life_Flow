import datetime
from django.shortcuts import render
from login.models import Login
from patient.models import Patient
from django.http import HttpResponseRedirect

# Create your views here.
def patient(request):
    if request.method=='POST':
        obj=Patient()
        obj.patient_name=request.POST.get('name')
        obj.age=request.POST.get('age')
        obj.bloodgroup=request.POST.get('bloodGroup')
        obj.bystandername=request.POST.get('byname')
        obj.phone=request.POST.get('phone')
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('password')
        obj.status='pending'
        obj.date=datetime.datetime.today()
        obj.save()
        ob=Login()
        ob.username=obj.username
        ob.password=obj.password
        ob.u_id=obj.patient_id
        ob.type='patient'
        ob.save()
        return HttpResponseRedirect('/login/login/')
    return render(request,'patient/patient.html')

def view_patient(request):
    obj=Patient.objects.all()
    context={
        'x':obj
    }
    return render(request,'patient/view_patient.html',context)