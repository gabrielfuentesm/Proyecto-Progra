from django.db import models

class sintomas(models.Model):
    nombre = models.CharField(max_length=2)
    email = models.CharField(max_length=2)
    edad = models.CharField(max_length=2)
    fiebre = models.CharField(max_length=2)
    tos = models.CharField(max_length=2)
    cansancio = models.CharField(max_length=2)
    aire = models.CharField(max_length=2)
    pecho = models.CharField(max_length=2)
    cabeza = models.CharField(max_length=2)
    respirar = models.CharField(max_length=2)
    
    def publish(self):
        self.save()


class Lascondes(models.Model):
    hospital = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

    def publish(self):
        self.save()

class Vitacura(models.Model):
    hospital = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

    def publish(self):
        self.save()

class Providencia(models.Model):
    hospital = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

    def publish(self):
        self.save()

class Lobarnechea(models.Model):
    hospital = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

    def publish(self):
        self.save()
    
class Lareina(models.Model):
    hospital = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

    def publish(self):
        self.save()