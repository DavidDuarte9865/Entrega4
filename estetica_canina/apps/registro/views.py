from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cita
from .forms import CitasForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# las importaciones para la API
from rest_framework import generics
from .serializers import CitaSerializer
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser


# ------------- importacines API ---------------------

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.


class CitaList (ListView):
    model = Cita
    template_name = 'Registro/listar_cita.html'


class CitaCreate (CreateView):
    model = Cita
    form_class = CitasForm
    template_name = 'Registro/agregar_cita.html'
    success_url = reverse_lazy('citas_list')


class CitaUpdate(UpdateView):
    model = Cita
    form_class = CitasForm
    template_name = 'Registro/agregar_cita.html'
    success_url = reverse_lazy('citas_list')


class CitaDelete(DeleteView):
    model = Cita
    template_name = 'Registro/eliminar_cita.html'
    success_url = reverse_lazy('citas_list')

# ===================


class API_objects(generics.ListCreateAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer


class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def cita_element(request, pk):
    cita = get_object_or_404(Cita, id=pk)

    if request.method == 'GET':
        serializer = CitaSerializer(cita)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        cita.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        cita_new = JSONParser().parse(request)
        serializer = CitaSerializer(cita, data=cita_new)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def cita_collection(request):
    if request.method == 'GET':
        citas = Cita.objects.all()
        serializer = CitaSerializer(citas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CitaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

