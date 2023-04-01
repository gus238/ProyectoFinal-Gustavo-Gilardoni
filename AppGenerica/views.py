from django.shortcuts import render
from AppGenerica.models import *
from AppGenerica.forms import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# Creo mis views

@login_required
def inicio(request):

    avatares = Avatar.objects.filter(user=request.user.id)
    print(avatares[0].imagen.url)
    return render(request, r'inicio.html', {"url":avatares[0].imagen.url})

# Creo mis formularios

@login_required
def juego_formulario(request):

    if request.method == 'POST':

        mi_formulario = form_juego_formulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:
            
            informacion = mi_formulario.cleaned_data

            juego = Juego(nombre=informacion['nombre'],
                          empresa=informacion['empresa'],
                          categoria=informacion['categoria'],
                          jugadores=informacion['jugadores'])
            juego.save()

            return render(request, r'inicio.html')
    else:
        mi_formulario = form_juego_formulario()
    
    return render(request, r'juego.html', {'mi_formulario':mi_formulario})


@login_required
def influencer_formulario(request):

    if request.method == 'POST':

        mi_formulario = form_influencer_formulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:
            
            informacion = mi_formulario.cleaned_data

            influencer = Influencer(nombre=informacion['nombre'],
                                    nacimiento=informacion['nacimiento'])
            
            influencer.save()

            return render(request, r'inicio.html')
    else:
        mi_formulario = form_influencer_formulario()
    
    return render(request, r'influencer.html', {'mi_formulario':mi_formulario})

@login_required
def plataforma_formulario(request):

    if request.method == 'POST':

        mi_formulario = form_plataforma_formulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:
            
            informacion = mi_formulario.cleaned_data

            plataforma = Plataforma(nombre=informacion['nombre'],
                                    ceo=informacion['ceo'])
            
            plataforma.save()

            return render(request, r'inicio.html')
    else:
        mi_formulario = form_plataforma_formulario()
    
    return render(request, r'plataforma.html', {'mi_formulario':mi_formulario})








# Creo las busquedas en la DB

@login_required
def buscar_juego(request):

    return render(request, r'buscar_juego.html')

@login_required
def resultado_juego(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        empresa = Juego.objects.filter(nombre__icontains=nombre)
        categoria = Juego.objects.filter(nombre__icontains=nombre)
        jugadores = Juego.objects.filter(nombre__icontains=nombre)

        return render(request, r'resultado_juego.html', {"nombre":nombre,
                                                        "empresa":empresa,
                                                        "categoria":categoria,
                                                        "jugadores":jugadores})
    else:

        respuesta = 'No enviaste datos'

    return HttpResponse(respuesta)






@login_required
def buscar_influencer(request):

    return render(request, r'buscar_influencer.html')


@login_required
def resultado_influencer(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        nacimiento = Influencer.objects.filter(nombre__icontains=nombre)

        return render(request, r'resultado_influencer.html', {"nombre":nombre,
                                                            "nacimiento":nacimiento})
    else:

        respuesta = 'No enviaste datos'

    return HttpResponse(respuesta)







@login_required
def buscar_plataforma(request):

    return render(request, r'buscar_plataforma.html')


@login_required
def resultado_plataforma(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        ceo = Plataforma.objects.filter(nombre__icontains=nombre)

        return render(request, r'resultado_plataforma.html', {"nombre":nombre,
                                                            "ceo":ceo})
    else:

        respuesta = 'No enviaste datos'

    return HttpResponse(respuesta)


#CRUD

@login_required
def leer_juego(request):

    juego = Juego.objects.all()

    contexto = {'juego':juego}

    return render(request, r'leer_juego.html', contexto)

@login_required
def eliminar_juego(request, juego_nombre):

    juego = Juego.objects.get(nombre=juego_nombre)
    juego.delete()

    juegos = Juego.objects.all()

    contexto = {'juegos':juegos}

    return render(request, r'leer_juego.html', contexto)

@login_required
def editar_juego(request, juego_nombre):

    juego = Juego.objects.get(nombre=juego_nombre)

    if request.method == 'POST':

        mi_formulario = form_juego_formulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            juego.nombre = informacion['nombre']
            juego.empresa = informacion['empresa']
            juego.categoria = informacion['categoria']
            juego.jugadores = informacion['jugadores']

            juego.save()

            return render(request, r'inicio.html')
        
    else:
            mi_formulario = form_juego_formulario(initial={'nombre': juego.nombre, 'empresa': juego.empresa,
                                                           'categoria': juego.categoria, 'jugadores': juego.jugadores})
            
    return render(request, r'editar_juego.html', {"mi_formulario":mi_formulario, "juego_nombre":juego_nombre})



@login_required
def leer_plataforma(request):

    plataforma = Plataforma.objects.all()

    contexto = {'plataforma':plataforma}

    return render(request, r'leer_plataforma.html', contexto)

@login_required
def eliminar_plataforma(request, plataforma_nombre):

    plataforma = Plataforma.objects.get(nombre=plataforma_nombre)
    plataforma.delete()

    plataformas = Plataforma.objects.all()

    contexto = {'plataformas':plataformas}

    return render(request, r'leer_plataforma.html', contexto)

@login_required
def editar_plataforma(request, plataforma_nombre):

    plataforma = Plataforma.objects.get(nombre=plataforma_nombre)

    if request.method == 'POST':

        mi_formulario = form_plataforma_formulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            plataforma.nombre = informacion['nombre']
            plataforma.ceo = informacion['ceo']


            plataforma.save()

            return render(request, r'inicio.html')
        
    else:
            mi_formulario = form_plataforma_formulario(initial={'nombre': plataforma.nombre, 'ceo': plataforma.ceo})
            
    return render(request, r'editar_plataforma.html', {"mi_formulario":mi_formulario, "plataforma_nombre":plataforma_nombre})



@login_required
def leer_influencer(request):

    influencer = Influencer.objects.all()

    contexto = {'influencer':influencer}

    return render(request, r'leer_influencer.html', contexto)

@login_required
def eliminar_influencer(request, influencer_nombre):

    influencer = Influencer.objects.get(nombre=influencer_nombre)
    influencer.delete()

    influencers = Influencer.objects.all()

    contexto = {'influencers':influencers}

    return render(request, r'leer_influencer.html', contexto)

@login_required
def editar_influencer(request, influencer_nombre):

    influencer = Influencer.objects.get(nombre=influencer_nombre)

    if request.method == 'POST':

        mi_formulario = form_influencer_formulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            influencer.nombre = informacion['nombre']
            influencer.nacimiento = informacion['nacimiento']


            influencer.save()

            return render(request, r'inicio.html')
        
    else:
            mi_formulario = form_influencer_formulario(initial={'nombre': influencer.nombre, 'nacimiento': influencer.nacimiento})
            
    return render(request, r'editar_influencer.html', {"mi_formulario":mi_formulario, "influencer_nombre":influencer_nombre})




#Login, Registro, Editar Perfil y Agregar Avatar

def login_request(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, r'inicio.html', {'mensaje':f"Bienvenido {usuario}"})
            
            else:

                return render(request, r'inicio.html', {"mensaje":"Error, datos incorrectos"})
            
        else:

                return render(request, r'inicio.html', {'mensaje':'error, formulario erroneo'})
        
    form = AuthenticationForm()

    return render(request, r'login.html', {'form':form})


def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, r'inicio.html', {'mensaje':'Usuario Creado'})
        

    else:

        form = UserRegisterForm

    return render(request, r'registro.html', {'form':form})


@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        mi_formulario = UserEditForm(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            print(mi_formulario)

            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            if informacion['password1'] == informacion['password2']:
                usuario.password = make_password(informacion['password1'])
                usuario.save()
            else:
                return render(request, r'inicio.html', {'mensaje':'Contraseña incorrecta.'})
            return render(request, r'inicio.html')
    else:
        mi_formulario = UserEditForm(initial={'email':usuario.email})
        
    return render(request, r'editar_perfil.html', {'mi_formulario':mi_formulario, 'usuario':usuario})
    
@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        mi_formulario = AvatarFormulario(request.POST, request.FILES)
        if mi_formulario.is_valid():
            username = User.objects.get(username=request.user)
            avatar = Avatar(user=username, imagen=mi_formulario.cleaned_data['imagen'])
            avatar.save()

            return render(request, r'inicio.html')
    else:
        mi_formulario = AvatarFormulario()
    return render(request, r'agregar_avatar.html', {'mi_formulario':mi_formulario})


#Sobre mi y paginas nulas

@login_required
def about_me(request):

    return render(request, r'sobre_mi.html')

@login_required
def nada(request):

    return render(request, r'nada.html')