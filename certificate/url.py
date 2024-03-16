
from django.conf.urls import url
from certificate import views
urlpatterns=[
    url('add_certificate/',views.add_certificate),
    url('view_certificate/',views.view_certificate),
]