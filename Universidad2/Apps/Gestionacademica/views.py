from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404

# Create your views here.
from django.template.loader import get_template


class Views():

    def home(self):
        plantilla = get_template('Index.html')
        return HttpResponse(plantilla.render())

    def Alumno(self):
        plantilla = get_template('Alumno.html')
        return HttpResponse(plantilla.render())

    def Maestro(self):
        plantilla = get_template('Maestro.html')
        return HttpResponse(plantilla.render())

    def Materia(self):
        plantilla = get_template('Materia.html')
        return  HttpResponse(plantilla.render())
    def Carrera(self):
        pantilla = get_template('Carrera.html')
        return HttpResponse(pantilla.render())