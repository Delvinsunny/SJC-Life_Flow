from django.shortcuts import render
from django.http import HttpResponseRedirect
from login.models import Login
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        obj=Login.objects.filter(username=username,password=password)
        tp=""
        for ob in obj:
            tp=ob.type
            uid=ob.u_id
            if tp=="admin":
                request.session['u_id']=uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp=="student":
                request.session['u_id']=uid
                return HttpResponseRedirect('/temp/student/')
            elif tp=="patient":
                request.session['u_id']=uid
                return HttpResponseRedirect('/temp/patient/')
        else:
            objlist="incorrect username or password......"
            context={
                    'x':objlist,
                }
        return render(request,'login/login.html',context)
    return render(request,'login/login.html')