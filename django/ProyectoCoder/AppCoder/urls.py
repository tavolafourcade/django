from django.urls import path
from AppCoder.views import profesores, curso, inicio, cursos, estudiantes, entregables, cursoFormulario, profesorFormulario, busquedaCamada, buscar, leerProfesores, eliminarProfesor, editarProfesor, EstudiantesList, EstudianteDetalle, EstudianteCreacion, EstudianteEdicion, EstudianteEliminacion, login_request, register_request
from django.contrib.auth.views import LogoutView
# from AppCoder.views import curso, profesores

urlpatterns = [
  path('curso/', curso),
  path('cursos/', cursos, name='Cursos'),
  path('estudiantes/', estudiantes, name='Estudiantes'),
  path('entregables/', entregables, name='Entregables'),
  path('inicio/', inicio, name='Inicio'),
  path('cursoFormulario/', cursoFormulario, name='cursoFormulario'),
  path('profesorFormulario/', profesorFormulario, name='profesorFormulario'),
  path('busquedaCamada/', busquedaCamada, name='busquedaCamada'),
  path('buscar/', buscar, name='buscar'),
  path('profesores/', leerProfesores, name='Profesores'),
  path('eliminarProfesor/<nombre>', eliminarProfesor, name='eliminarProfesor'),
  path('editarProfesor/<profesor_nombre>', editarProfesor, name='editarProfesor'),
  #----------------------
  path('estudiante/list/', EstudiantesList.as_view(), name='estudiante_listar'),
  path('estudiante/<pk>', EstudianteDetalle.as_view(), name='estudiante_detalle'),
  path('estudiante/nuevo/', EstudianteCreacion.as_view(), name='estudiante_crear'),
  path('estudiante/editar/<pk>', EstudianteEdicion.as_view(), name='estudiante_editar'),
  path('estudiante/borrar/<pk>', EstudianteEliminacion.as_view(), name='estudiante_borrar'),

  path('login', login_request, name='login'),
  path('register', register_request, name='registro'),
  path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout'),

]