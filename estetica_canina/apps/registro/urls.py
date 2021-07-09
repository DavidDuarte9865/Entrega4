from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from django.contrib.auth.views import login_required

from . import views

urlpatterns = [

    path('listar/', CitaList.as_view(), name="citas_list"),
    path('crear/', CitaCreate.as_view(), name="citas_form"),
    path('editar/<int:pk>', login_required(CitaUpdate.as_view()), name="citas_update"),
    path('borrar/<int:pk>', login_required(CitaDelete.as_view()), name="citas_borrar"),
    # solo existe el ID 4 y 5 si quieres borrar o editar
    # api
    path('citas/',  views.cita_collection , name='citas_collection'),
    path('cita/<int:pk>/', views.cita_element ,name='cita_element')

]
urlpatterns += [
    path('api/', views.API_objects.as_view()),
    path('api/<int:pk>/', views.API_objects_details.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
