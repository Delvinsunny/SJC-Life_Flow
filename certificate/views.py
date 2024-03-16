from django.shortcuts import render
from certificate.models import Certificate
from student.models import Student
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect


# Create your views here.
def add_certificate(request):
    ob=Student.objects.filter(status='approve')
    context={
        'x':ob
    }
    if request.method=='POST':
        obj=Certificate()
        obj.donated_date=request.POST.get('date')
        obj.hospital=request.POST.get('patient')

        myfile=request.FILES['file']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.certificate=myfile.name

        obj.student_id=request.POST.get('name')
        obj.save()
        return HttpResponseRedirect('/temp/admin/')
    return render(request,'certificate/add_certificate.html',context)

def view_certificate(request):
    ss=request.session['u_id']
    obj=Certificate.objects.filter(student_id=ss)
    context={
        'x':obj
    }
    return render(request,'certificate/view_certificate.html',context)