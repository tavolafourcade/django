from django.http import HttpResponse
from CodingApp.models import Course

def course(self):
  course = Course(name='Web Development', course_id=24500)
  course.save()
  document = f'---> Course: {course.name} Course ID: {course.course_id}'
  return HttpResponse(document)