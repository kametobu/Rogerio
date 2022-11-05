from django.shortcuts import render,redirect
from django.http import HttpResponse
import hashlib
from django.contrib.auth import authenticate,login,logout
from usuarios.forms import *

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    user = authenticate(username=email, password=senha)
    if user is None:
         return render(request, 'login.html')
    login(request, user)
    return redirect('/')

def cadastro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, "cadastro.html", {'form': form })
    form = UserForm()
    return render(request, "cadastro.html", {'form': form })
    



#def login(request):
#    if request.session.get('usuario'):
#        return redirect('/home')
#    status = request.GET.get('status')
#    return render(request, 'login.html', {'status':status})

#def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario_existe = Usuario.objects.filter(email=email)

    if len(senha) < 8 or len(senha) > 12:
        return redirect('/auth/cadastro?status=1')

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro?status=2')

    if len(usuario_existe) > 0:
        return redirect('/auth/cadastro?status=3')

    try:
        senha = hashlib.sha256(senha.encode()).hexdigest() #encripta senha do usuário
        usuario = Usuario(nome=nome,
                     email=email,
                     senha=senha)
        usuario.save()        
        return redirect('/auth/cadastro?status=0')# msg cadastro com sucesso
    except:
        return HttpResponse('ERRO INTERNO DO SISTEMA! TENTE NOVAMENTE!')

#def valida_login(request):
#    email = request.POST.get('email')
#    senha = request.POST.get('senha')
#    senha = hashlib.sha256(senha.encode()).hexdigest()
#    usuarios = Usuario.objects.filter(email = email).filter(senha = senha)
#
#    if len(usuarios) == 0:
#        return redirect('/auth/login/?status=1')
#    elif len(usuarios) > 0:
#        request.session['usuario'] = usuarios[0].id
#        return redirect('/')

def sair(request):
    logout(request)
    return redirect('/')
    

