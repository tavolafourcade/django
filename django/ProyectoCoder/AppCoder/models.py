from django.db import models

class Curso(models.Model):
  nombre = models.CharField(max_length=40)
  camada = models.IntegerField()

  def __str__(self) -> str:
    return self.nombre+" "+str(self.camada)

class Estudiante(models.Model):
  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  email = models.EmailField()

  def __str__(self) -> str:
    return self.nombre+" "+str(self.apellido)

class Profesor(models.Model):
  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  email = models.EmailField()
  profesion = models.CharField(max_length=30)

  def __str__(self) -> str:
    return self.nombre+" "+self.apellido

class Entregable(models.Model):
  nombre = models.CharField(max_length=30)
  fechaDeEntrega = models.DateField()
  entregado = models.BooleanField()
