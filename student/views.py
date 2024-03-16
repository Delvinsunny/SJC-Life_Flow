from django.shortcuts import render
from login.models import Login
from student.models import Student
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect

# Create your views here.

def admin_add_stud(request):
    if request.method=='POST':
        obj=Student()
        obj.name=request.POST.get('name')
        obj.adm_no=request.POST.get('ad')
        obj.course=request.POST.get('course')
        obj.year=request.POST.get('year')
        obj.dob=request.POST.get('dob')
        myfile=request.FILES['photo']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.photo=myfile.name
        obj.bloodgroup=request.POST.get('bloodGroup')
        obj.phone=request.POST.get('phone')
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('password')
        obj.status='pending'
        obj.save()
        return HttpResponseRedirect('/temp/admin/')
    return render(request,'student/admin_add_stud.html')


def manage_student(request):
    obj=Student.objects.all()
    context={
        'x':obj
    }
    return render(request,'student/manage_student.html',context)


def approve(request,idd):
    obj=Student.objects.get(student_id=idd)
    obj.status='approve'
    obj.save()
    ob=Login()
    ob.username=obj.username
    ob.password=obj.password
    ob.u_id=obj.student_id
    ob.type='student'
    ob.save()
    return  manage_student(request)
def reject(request,idd):
    obj=Student.objects.get(student_id=idd)
    obj.status='reject'
    obj.save()
    return  manage_student(request)
def profile(request):
    ss=request.session['u_id']
    obj=Student.objects.filter(student_id=ss)
    context={
        'x':obj
    }
    return render(request,'student/profile.html',context)

def student(request):
    if request.method=='POST':
        obj=Student()
        obj.name=request.POST.get('name')
        obj.adm_no=request.POST.get('ad')
        obj.course=request.POST.get('course')
        obj.year=request.POST.get('semester')
        obj.dob=request.POST.get('dob')

        myfile=request.FILES['photo']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.photo=myfile.name
         
        obj.bloodgroup=request.POST.get('bloodGroup')
        obj.phone=request.POST.get('phone')
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('password')
        obj.status='pending'
        obj.save()
        return HttpResponseRedirect('/login/login/')
    return render(request,'student/student.html')