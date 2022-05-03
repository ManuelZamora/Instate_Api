from django. urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
from .views import testeo, testeo2


urlpatterns =[
    path('/a', testeo.as_view(), name='geta'),
    path('/b', csrf_exempt(views.posti), name='posti'),
    path('/csv', csrf_exempt(views.csv), name='csv'),
    path('/mapa', csrf_exempt(views.mapa), name='mapa'),
    path('/colorbar', csrf_exempt(views.colorbar), name='colorbar'),
]
#otra forma de direccionar
""" from django. urls import path
from . import views

urlpatterns =[
    path('/a', views.testeo, name='get'),
] """