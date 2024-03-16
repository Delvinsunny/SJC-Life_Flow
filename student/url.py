from django.conf.urls import url
from student import views
urlpatterns=[
    url('add/',views.admin_add_stud),
    url('manage_student/',views.manage_student),
    url('profile/',views.profile),
    url('student/',views.student),
    url('approve/(?P<idd>\w+)',views.approve),
    url('reject/(?P<idd>\w+)',views.reject),
    
]