from django.shortcuts import render
from attendancereq.models import Attendancereq
from django.core.files.storage import FileSystemStorage
import datetime
from django.http import HttpResponseRedirect

# Create your views here.
def attendence_request(request):
    ss=request.session['u_id']
    if request.method=='POST':
        obj=Attendancereq()
        obj.request=request.POST.get('request')

        myfile=request.FILES['file']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.file=myfile.name

        obj.status='pending'
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.student_id=ss
        obj.save()
        return HttpResponseRedirect('/temp/student/')
    return render(request,'attendancereq/attendence_request.html')

def manage_attendencerequest(request):
    obj=Attendancereq.objects.all()
    context={
        'x':obj
    }
    return render(request,'attendancereq/manage_attendencerequest.html',context)

def view_attentencerequest(request):
    ss=request.session['u_id']
    obj=Attendancereq.objects.filter(student_id=ss)
    context={
        'x':obj
    }
    return render(request,'attendancereq/view_attentencerequest.html',context)

def approve(request,idd):
    obj=Attendancereq.objects.get(req_id=idd)
    obj.status='approve'
    obj.save()
    return  manage_attendencerequest(request)
def reject(request,idd):
    obj=Attendancereq.objects.get(req_id=idd)
    obj.status='reject'
    obj.save()
    return  manage_attendencerequest(request)