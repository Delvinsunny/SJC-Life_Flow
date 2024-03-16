from django.conf.urls import url
from bloodrequest import views
urlpatterns=[
    url('bloodrequest/',views.bloodrequest),
    url('manage/',views.manage_bloodrequest),
    url('view_stud/',views.view_bloodrequest),
    url('view_status/',views.view_bloodrequeststatus),
    url('approve/(?P<idd>\w+)',views.approve),
    url('reject/(?P<idd>\w+)',views.reject),
    url('view_summary/',views.view_summary),
]