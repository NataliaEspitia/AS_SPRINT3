import json
import random
from decimal import Decimal
from datetime import datetime, timedelta

# Generate random values for the fixture
def generate_random_cobro(pk):
    valores = [Decimal('1000.50'), Decimal('2500.75'), Decimal('3200.30'), Decimal('1500.00'), Decimal('2100.99')]
    meses = range(1, 13)  # Months from 1 (January) to 12 (December)
    years = [2022, 2023, 2024]  # List of years
    tipos = ['Normal', 'Extraordinario', 'Mora', 'Descuento']  # Types of payments
    intereses = [Decimal('5.00'), Decimal('10.50'), Decimal('2.50'), Decimal('3.25')]  # Interest values

    valor = str(random.choice(valores))  
    mes = random.choice(meses)
    year = random.choice(years)
    day = random.randint(1, 28) 
    fecha_limite = (datetime(year, mes, day) + timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
    tipo = random.choice(tipos)
    interes = str(random.choice(intereses))  

    return {
        "model": "cobros.cobro",  
        "pk": pk,
        "fields": {
            "valor": valor,
            "mes": mes,
            "year": year,
            "fechaLimite": fecha_limite,
            "tipo": tipo,
            "interes": interes
        }
    }

# Generate records
def generate_fixture():
    records = []
    dataentries = 500
    for pk in range(1, dataentries+1):  
        record = generate_random_cobro(pk)
        records.append(record)

    # Write to a fixture file
    with open('cobro_fixture.json', 'w') as f:
        json.dump(records, f, indent=4)

if __name__ == '__main__':
    generate_fixture()
