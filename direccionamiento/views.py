import json

from requests.api import patch
import pandas as pd
from direccionamiento.metodos import houseList
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse, request, HttpResponseRedirect, HttpRequest
from django.views.generic import TemplateView
from django.views.generic.dates import DayArchiveView
from direccionamiento.metodos.houseList import HouseList, instancia_houslist
from direccionamiento.metodos.mapa import mapa, instanciamapa
""""from django.views.decorators.csrf import csrf_exempt
@csrf_exempt"""
# Create your views here.
#ahi esatn mis npinches n8 qwer

def posti(request, *arg, **kwargs):
    if request.method == 'POST':
        department_data=JSONParser().parse(request)
        print(department_data)
        datos_retornar=[]
        dt=[]
        datos_houstlist={}

        print("entrara a houslist")
        houstlist=instancia_houslist(department_data['ciudad'])
        print("salio de houstlist")
        
        lista=houstlist.lista
        ubicaciones= houstlist.ubicaion
        
        
        
        
        

        datos_houstlist['lista']=lista['data']
        
        datos_houstlist['ubicaciones']=ubicaciones['data']
        
    
        datos_retornar.append(datos_houstlist)
        print("has entrado al post")
        print("ya voy a retornar datos")
        #return HttpResponse(json.dumps(lista[:8]), content_type="application/json")
        return JsonResponse(datos_retornar, safe=False)


    else:
        l= []
        datas={}
        datasb={}
        datas['a']="has entrado a djangasdo"
        datas['b']="has entrado a b"
        datas['c']="has entrado a c"
        datas['d']="has entrado a d"
        l.append(datas)
        print(request)
        print(l)
        print(datas)
        s= (list(datas.values()))
        print(s)
        return JsonResponse(list(datas.values()), safe=False)

def csv(request, *arg, **kwargs):
    if request.method == 'POST':
        department_data=JSONParser().parse(request)
        
        
        

        nombre=department_data['nombre']
        datos=department_data['Lista']
        print("entrara a houslist")
        dataFrame = pd.DataFrame(datos)
        dataFrame.to_csv(nombre)

        
        
        l= []
        datas={}
        datas['nombre']=nombre
        l.append(datas)
        return JsonResponse(list(datas.values()), safe=False)

class testeo(ListView):
    def get(self, request):
        l= []
        datas={}
        datasb={}
        datas['a']="has entrado a django"
        datas['b']="has entrado a b"
        datas['c']="has entrado a c"
        datas['d']="has entrado a d"
        l.append(datas)
        print(request)
        print(l)
        print(datas)
        print(self)
        s= (list(datas.values()))
        print(s)
        return JsonResponse(list(datas.values()), safe=False)

class testeo2(ListView):
    def get(self, request):
        l2= []
        datas2={}
        datas2['a']=2
        l2.append(datas2)
        print(datas2)
        return JsonResponse(list(datas2.values()), safe=False)


def mapa(request, *arg, **kwargs):
    if request.method == 'GET':
        print("sas")
        a = instanciamapa()
        b= a.lista
        l2= []
        datas2={}
        datas2['a']=b
        l2.append(datas2) 
        return JsonResponse(list(datas2.values()), safe=False)

    if request.method == 'POST':
        department_data=JSONParser().parse(request)
        print("hi")
        print(department_data)
        cordenas = department_data['cordenadas']
        print('corde')
        print(cordenas)
        ubi=department_data['ubi_costo']
        print('ubi')
        print(ubi)
        a = instanciamapa(ubi, cordenas)
        b= a.lista
        l2= []
        datas2={}
        datas2['a']=b
        l2.append(datas2)
        return JsonResponse(list(datas2.values()), safe=False)

def colorbar(request, *arg, **kwargs):
    if request.method == 'GET':
        print("sas")
        a = instanciamapa()
        b= a.lista
        l2= []
        datas2={}
        datas2['a']=b
        l2.append(datas2) 
        return JsonResponse(list(datas2.values()), safe=False)

    if request.method == 'POST':
        department_data=JSONParser().parse(request)
        print("hi")
        print(department_data)
        cordenas = department_data['cordenadas']
        print('corde')
        print(cordenas)
        ubi=department_data['ubi_costo']
        print('ubi')
        print(ubi)
        a = instanciamapa(ubi, cordenas)
        b= a.lista
        l2= []
        datas2={}
        datas2['a']=b
        l2.append(datas2)
        return JsonResponse(list(datas2.values()), safe=False)
        
        
        


"""
lat, lng, json
"""