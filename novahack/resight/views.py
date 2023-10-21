from django.shortcuts import render
from django.urls import path, include
from .models import Gafa
from django.http import HttpResponse, JsonResponse
from django.views import View
from .serializers import GafaSerializer
from rest_framework import status
from . import views
from rest_framework.response import Response
#Shit for the get api
from rest_framework import generics

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


def index(request):
    return HttpResponse("You're looking at question" )

class GafaList(generics.ListAPIView):
    
    def get(self, request):
        gafas = Gafa.objects.filter(vendido=False)
        serializer = GafaSerializer(gafas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    















'''
urlpatterns = [
    path("", views.index, name="index"),
    path("resight/", include("resight.urls")),
    path('obtener-gafas/', views.obtener_gafas, name='obtener_gafas'),
]



def crear_gafas(request):
    if request.method == 'POST':
        nuevas_gafas = Gafa(
            solares = request.POST['solares'], 
            vendido = False, 
            miopia_right = request.POST['miopia_right'], 
            astigmatismo_right = request.POST['astigmatismo_right'], 
            hipermetropia_right = request.POST['hipermetropia_right'],         
            miopia_left = request.POST['miopia_left'], 
            astigmatismo_left = request.POST['astigmatismo_left'], 
            hipermetropia_left = request.POST['hipermetropia_left'], 
            img = request.POST['img'], 
            state = request.POST['state']
        )
        nuevas_gafas.save()
        # Redirect or render a response
    else:
        # Handle GET requests (display a form, for example)
        #
        pass
# post

@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def obtener_gafas(request):
    gafas_no_vendidas = Gafa.objects.filter(vendido=False)
    serializer = GafaSerializer(gafas_no_vendidas, many=True)
    return Response(serializer.data)
    modelos = Gafa.objects.all()
    data = [
        {
            'solares': modelo.solares, 
            'vendido': modelo.vendido,
            'miopia_right': modelo.miopia_right, 
            'astigmatismo_right': modelo.astigmatismo_right, 
            'hipermtropia_right': modelo.hipermtropia_right, 
            'miopia_left': modelo.miopia_left, 
            'astigmatismo_left': modelo.astigmatismo_left, 
            'hipermetropia_left': modelo.hipermetropia_left, 
            
        } for modelo in modelos]
    return JsonResponse(data, safe=False)
'''