from django.conf.urls import url
from attendancereq import views
urlpatterns=[
    url('attendence_request/',views.attendence_request),
    url('manage_attendencerequest/',views.manage_attendencerequest),
    url('view_attentencerequest/',views.view_attentencerequest),
    url('approve/(?P<idd>\w+)',views.approve),
    url('reject/(?P<idd>\w+)',views.reject),
]