from django.http import HttpResponse
from django.template import Template, Context

def first_template(self):

  name = 'John'
  last_name = 'Doe'

  dictionary = {'name': name, 'last_name': last_name}

  html_path = open('/Users/octaviolafourcade/Documents/PYTHON/django/hello_world/hello_world/templates/first_template.html')

  template = Template(html_path.read())
  html_path.close()

  context = Context(dictionary)

  document = template.render(context)

  return HttpResponse(document)