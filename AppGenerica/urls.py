from django.urls import path
from AppGenerica import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path(r'', views.inicio, name='Inicio'),
    path(r'crear_juego/', views.juego_formulario, name='Juegos'),
    path(r'buscar_juego/', views.buscar_juego, name='BuscarJuego'),
    path(r'resultado_juego/', views.resultado_juego),
    path(r'leer_juego/', views.leer_juego, name='LeerJuego'),
    path(r'eliminar_juego/<juego_nombre>/', views.eliminar_juego, name='EliminarJuego'),
    path(r'editar_juego/<juego_nombre>', views.editar_juego, name='EditarJuego'),
    path(r'crear_influencer/', views.influencer_formulario, name='Influencers'),
    path(r'buscar_influencer/', views.buscar_influencer, name='BuscarInfluencer'),
    path(r'resultado_influencer/', views.resultado_influencer),
    path(r'crear_plataforma/', views.plataforma_formulario, name='Plataformas'),
    path(r'buscar_plataforma/', views.buscar_plataforma, name='BuscarPlataforma'),
    path(r'resultado_plataforma/', views.resultado_plataforma),
    path(r'leer_plataforma/', views.leer_plataforma, name='LeerPlataforma'),
    path(r'eliminar_plataforma/<plataforma_nombre>/', views.eliminar_plataforma, name='EliminarPlataforma'),
    path(r'editar_plataforma/<plataforma_nombre>', views.editar_plataforma, name='EditarPlataforma'),
    path(r'leer_influencer/', views.leer_influencer, name='LeerInfluencer'),
    path(r'eliminar_influencer/<influencer_nombre>/', views.eliminar_influencer, name='EliminarInfluencer'),
    path(r'editar_influencer/<influencer_nombre>', views.editar_influencer, name='EditarInfluencer'),
    path(r'login/', views.login_request, name='Login'),
    path(r'register/', views.register, name='Register'),
    path(r'logout/', LogoutView.as_view(template_name=r'logout.html'), name='Logout'),
    path(r'editar_perfil/', views.editar_perfil, name='EditarPerfil'),
    path(r'agregar_avatar/', views.agregarAvatar, name='AgregarAvatar'),
    path(r'about/', views.about_me, name='SobreMi'),
    path(r'nada/', views.nada, name='Nada')
]