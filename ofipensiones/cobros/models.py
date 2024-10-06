from django.db import models

# Create your models here.

class Cobro(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    mes = models.IntegerField()
    year = models.IntegerField()
    fechaLimite = models.DateField()
    tipo = models.CharField(max_length=50)
    interes = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return '%s %s %s' % (self.valor, self.mes, self.year)