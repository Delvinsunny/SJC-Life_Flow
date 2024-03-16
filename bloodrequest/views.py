import datetime
from django.shortcuts import render
from bloodrequest.models import Bloodrequest
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect

# Create your views here.
def bloodrequest(request):
    ss=request.session['u_id']
    if request.method=='POST':
        obj=Bloodrequest()
        obj.group=request.POST.get('bloodGroup')
        obj.unit=request.POST.get('unit')
        obj.hospital=request.POST.get('hospital')

        myfile=request.FILES['file']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.document=myfile.name

        obj.status='pending'
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.patient_id=ss
        obj.save()
        return HttpResponseRedirect('/temp/patient/')
    return render(request,'bloodrequest/bloodrequest.html')

def manage_bloodrequest(request):
    obj=Bloodrequest.objects.all()
    context={
        'x':obj
    }
    return render(request,'bloodrequest/manage_bloodrequest.html',context)

def approve(request,idd):
    obj=Bloodrequest.objects.get(blood_id=idd)
    obj.status='approve'
    obj.save()
    return  manage_bloodrequest(request)
def reject(request,idd):
    obj=Bloodrequest.objects.get(blood_id=idd)
    obj.status='reject'
    obj.save()
    return  manage_bloodrequest(request)

def view_bloodrequest(request):
    obj=Bloodrequest.objects.all()
    context={
        'x':obj
    }
    return render(request,'bloodrequest/view_bloodrequest.html',context)

def view_bloodrequeststatus(request):
    ss=request.session['u_id']
    obj=Bloodrequest.objects.filter(patient_id=ss)
    context={
        'x':obj
    }
    return render(request,'bloodrequest/view_bloodrequeststatus.html',context)

def view_summary(request):
    if request.method=='POST':
        start=request.POST.get('start')
        end=request.POST.get('end')
        blood=request.POST.get('blood')
        obj=Bloodrequest.objects.filter(date__range=(start, end),group=blood)
        context={
        'x':obj
        }
    else:
        obj=Bloodrequest.objects.all()
        context={
            'x':obj
        }
    return render(request,'bloodrequest/summry.html',context)