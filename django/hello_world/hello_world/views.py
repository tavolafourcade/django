from django.http import HttpResponse
from django.template import Template, Context, loader

def first_template(self):

  name = 'John'
  last_name = 'Doe'

  dictionary = {'name': name, 'last_name': last_name}

  template = loader.get_template('first_template.html')

  document = template.render(dictionary)

  return HttpResponse(document)