# Generated by Django 5.1.1 on 2024-10-06 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cobro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mes', models.IntegerField()),
                ('year', models.IntegerField()),
                ('fechaLimite', models.DateField()),
                ('tipo', models.CharField(max_length=50)),
                ('interes', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]