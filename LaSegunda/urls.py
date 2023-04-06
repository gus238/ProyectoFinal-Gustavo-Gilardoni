from django.urls import path
from LaSegunda import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'', views.inicio, name='Inicio'),
    path(r'crear_amigo/', views.cargar_imagen_objeto, name='Amigo'),
    path(r'leer_amigo/', views.leer_amigo, name='LeerAmigo'),
    path(r'eliminar_amigo/<amigo_nombre>/', views.eliminar_amigo, name='EliminarAmigo'),
    path(r'editar_amigo/<amigo_nombre>', views.editar_amigo, name='EditarAmigo'),
    path(r'login/', views.login_request, name='Login'),
    path(r'register/', views.register, name='Register'),
    path(r'logout/', LogoutView.as_view(template_name=r'logout.html'), name='Logout'),
    path(r'editar_perfil/', views.editar_perfil, name='EditarPerfil'),
    path(r'agregar_avatar/', views.agregarAvatar, name='AgregarAvatar'),
    path(r'about/', views.about_me, name='SobreMi'),
    path(r'nada/', views.nada, name='Nada'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)