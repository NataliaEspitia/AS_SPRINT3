from django.shortcuts import render
from django.http import HttpResponse
from .logic import cobros_logic as cl
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def get_cobros(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            cobro_dto = cl.get_variable(id)
            cobro = serializers.serialize('json', [cobro_dto,])
            return HttpResponse(cobro, 'applications/json')
        else:
            cobros = cl.get_cobros()
            cobros_dto = serializers.serialize('json', cobros)
            return HttpResponse(cobros_dto, 'application/json')
    if request.method == 'POST':
        cobro_dto = cl.create_cobro(json.loads(request.body))
        cobro = serializers.serialize('json', [cobro_dto,])
        return HttpResponse(cobro, 'application/json')

def get_cobro(request, pk):
    if request.method == 'GET':
        cobro = cl.get_cobro(pk)
        cobro_dto = serializers.serialize('json', [cobro])
        return HttpResponse(cobro_dto, 'application/json')

