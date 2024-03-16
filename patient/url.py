
from django.conf.urls import url
from patient import views
urlpatterns=[
    url('patient/',views.patient),
    url('view/',views.view_patient),
    
]