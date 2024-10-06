from ..models import Cobro
from datetime import datetime

def get_cobros():
    cobros = Cobro.objects.all()
    return cobros

def get_cobro(c_pk):
    cobro = Cobro.objects.get(pk=c_pk)
    return cobro

def create_cobro(c):
    fecha = datetime.strptime(c["fechaLimite"], "%Y-%m-%d")
    cobro = Cobro(valor=c["valor"], mes=c["mes"], year=c["year"], fechaLimite=fecha, tipo=c["tipo"], interes=c["interes"])
    cobro.save()
    return cobro

