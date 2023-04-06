from django.shortcuts import render, get_object_or_404
from LaSegunda.models import *
from LaSegunda.forms import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# Create your views here.

@login_required
def inicio(request):

#    avatares = Avatar2.objects.filter(user=request.user.id)
#    print(avatares[0].imagen.url)
    return render(request, r'inicio.html')

#, {"url":avatares[0].imagen.url}




# Formulario

@login_required
def amigo_formulario(request):

    if request.method == 'POST':

        mi_formulario = form_amigo_formulario(request.POST)

        print(mi_formulario)

        if mi_formulario.is_valid:
            
            informacion = mi_formulario.cleaned_data

            amigo = Amigo(nombre=informacion['nombre'],
                               nacimiento=informacion['nacimiento'])
            
            amigo.save()

            return render(request, r'inicio.html')
    else:
        mi_formulario = form_amigo_formulario()
    
    return render(request, r'amigo.html', {'mi_formulario':mi_formulario})




# Imagen Objeto

def cargar_imagen_objeto(request):
    if request.method == 'POST':
        form = form_amigo_imagen(request.POST, request.FILES)
        if form.is_valid():
            nuevo_objeto = form.save(commit=False)
            nuevo_objeto.save()
            return render(request, r'inicio.html')
    else:
        form = form_amigo_imagen()

    return render(request, r'subir_amigo_imagen.html', {'form':form})

def ver_imagen_objeto(request):

    if request.method == 'POST':
        form = form_amigo_imagen(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(r'inicio.html')
    else:
        form = form_amigo_imagen()
    return render(request, r'ver_amigo_imagen.html', {'form': form})

def detalle_amigo(request, id):
    amigo = Amigo.objects.get(id=id)
    return render(request, r'detalle_amigo.html', {'amigo': amigo})






# Crud

@login_required
def leer_amigo(request):

    amigo = Amigo.objects.all()

    contexto = {'amigo':amigo}

    return render(request, r'leer_amigo.html', contexto)

@login_required
def eliminar_amigo(request, amigo_nombre):

    amigo = Amigo.objects.get(nombre=amigo_nombre)
    amigo.delete()

    amigos = Amigo.objects.all()

    contexto = {'amigos':amigos}

    return render(request, r'leer_amigo.html', contexto)

'''@login_required
def editar_amigo(request, amigo_nombre):

    amigo = Amigo.objects.get(nombre=amigo_nombre)

    if request.method == 'POST':

        mi_formulario = form_amigo_formulario(request.POST, request.FILES)

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            Amigo.nombre = informacion['nombre']
            Amigo.nacimiento = informacion['nacimiento']
            Amigo.imagen = informacion['imagen']


            Amigo.save()

            return render(request, r'inicio.html')
        
    else:
            mi_formulario = form_amigo_formulario(initial={'nombre': amigo.nombre, 'nacimiento': amigo.nacimiento, 'imagen': amigo.imagen})
            
    return render(request, r'editar_amigo.html', {"mi_formulario":mi_formulario, "amigo_nombre":amigo_nombre})'''

def editar_amigo(request, amigo_nombre):
    amigo = Amigo.objects.get(nombre=amigo_nombre)
    if request.method == 'POST':
        form = form_amigo_formulario(request.POST, request.FILES, instance=amigo)
        print(form)
        if form.is_valid():
            form.save()
            return render(request, r'inicio.html')
    else:
        form = form_amigo_formulario(instance=amigo)
    context = {'form': form}
    return render(request, r'editar_amigo.html', context)









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
            avatar = Avatar2(user=username, imagen=mi_formulario.cleaned_data['imagen'])
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