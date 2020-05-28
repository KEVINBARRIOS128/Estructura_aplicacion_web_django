"""Universidad2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

import Universidad2
from Universidad2.Apps.Gestionacademica.views import Views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',Universidad2.Apps.Gestionacademica.views.Views.home, name= 'home'),
    path('alumno/',Universidad2.Apps.Gestionacademica.views.Views.Alumno, name = 'Alumno'),
    path('maestro/',Universidad2.Apps.Gestionacademica.views.Views.Maestro, name = 'Maestro'),
    path('Materia/',Universidad2.Apps.Gestionacademica.views.Views.Materia, name = 'Materia'),
    path('Carrera', Universidad2.Apps.Gestionacademica.views.Views.Carrera, name = 'Carrera')
]
