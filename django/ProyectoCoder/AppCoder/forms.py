from django import forms

class CursosFormulario(forms.Form):
  #Especificar los campos
  curso = forms.CharField(max_length=50)
  camada = forms.IntegerField()