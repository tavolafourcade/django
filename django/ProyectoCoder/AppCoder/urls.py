from django.urls import path
from AppCoder.views import inicio, profesores, curso, cursos, estudiantes, entregables, cursosFormulario, busquedaComision, buscar, profesorFormulario, leerProfesores, eliminarProfesor, editarProfesor, EstudiantesList, EstudianteDetalle, EstudianteCreacion, EstudianteEdicion, EstudianteEliminacion
# from AppCoder.views import curso, profesores

urlpatterns = [
  path('curso/', curso),
  path('profesores/', leerProfesores, name='profesores'),
  path('cursos/', cursos, name='cursos'),
  path('estudiantes/', estudiantes, name='estudiantes'),
  path('entregables/', entregables, name='entregables'),
  path('inicio/', inicio, name='inicio'),
  path('cursosFormulario/', cursosFormulario, name='cursosFormulario'),
  path('profesorFormulario/', profesorFormulario, name='profesorFormulario'),
  path('busquedaComision/', busquedaComision, name='busquedaComision'),
  path('buscar/', buscar, name='buscar'),
  path('eliminarProfesor/<nombre>', eliminarProfesor, name='eliminarProfesor'),
  path('editarProfesor/<nombre>', editarProfesor, name='editarProfesor'),

  path('estudiante/list/', EstudiantesList.as_view(), name='estudiante_listar'),
  path('estudiante/<pk>', EstudianteDetalle.as_view(), name='estudiante_detalle'),
  path('estudiante/nuevo/', EstudianteCreacion.as_view(), name='estudiante_crear'),
  path('estudiante/editar/<pk>', EstudianteEdicion.as_view(), name='estudiante_editar'),
  path('estudiante/borrar/<pk>', EstudianteEliminacion.as_view(), name='estudiante_borrar'),

]