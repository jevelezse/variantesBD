from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^paciente_gen$', views.paciente_gen, name='paciente_gen'),
]
