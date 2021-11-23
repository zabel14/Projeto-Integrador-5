from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from api.models import Medico, Especialidade, Consulta


def index(request):
    return render(request, 'index.html')

def criar_medico(request):
    especialidades = Especialidade.objects.all()
    if request.method == 'POST':
        nome = request.POST['nome']
        data_nascimento = request.POST['data_nascimento']
        crm = request.POST['crm']
        especialidade = request.POST['especialidade']
        especialidade = Especialidade.objects.get(pk=especialidade)
        medico = Medico.objects.create(nome=nome, data_nascimento=data_nascimento, crm=crm, especialidade=especialidade)
        medico.save()
        return redirect('listar_medico')
    return render(request, 'criar_medico.html', {'especialidades': especialidades})

def editar_medico(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    especialidades = Especialidade.objects.all()
    if request.method == 'POST':
        nome = request.POST['nome']
        data_nascimento = request.POST['data_nascimento']
        crm = request.POST['crm']
        especialidade = request.POST['especialidade']
        especialidade = Especialidade.objects.get(pk=especialidade)
        medico.nome = nome
        medico.data_nascimento = data_nascimento
        medico.crm = crm
        medico.especialidade = especialidade
        medico.save(update_fields=['nome', 'data_nascimento', 'crm', 'especialidade'])
        return redirect('listar_medico')
    return render(request, 'editar_medico.html', {'medico': medico, 'especialidades': especialidades})

def listar_medico(request):
    medicos = Medico.objects.all()
    return render(request, 'listar_medico.html', {'medicos': medicos})

def deletar_medico(request, pk):
    medico = Medico.objects.get(pk=pk)
    if request.method == 'POST':
        medico.delete()
        return redirect('listar_medico')
    return render(request, 'deletar_medico.html', {'medico': medico})

def criar_especialidade(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        especialidade = Especialidade.objects.create(nome=nome)
        especialidade.save()
        return redirect('listar_especialidade')
    return render(request, 'criar_especialidade.html')

def editar_especialidade(request, pk):
    especialidade = Especialidade.objects.get(pk=pk)
    if request.method == 'POST':
        nome = request.POST['nome']
        especialidade.nome = nome
        especialidade.save(update_fields=['nome'])
        return redirect('listar_especialidade')
    return render(request, 'editar_especialidade.html', {'especialidade': especialidade})

def listar_especialidade(request):
    especialidades = Especialidade.objects.all()
    return render(request, 'listar_especialidade.html', {'especialidades': especialidades})

def deletar_especialidade(request, pk):
    especialidade = Especialidade.objects.get(pk=pk)
    if request.method == 'POST':
        especialidade.delete()
        return redirect('listar_especialidade')
    return render(request, 'deletar_especialidade.html', {'especialidade': especialidade})

def criar_consulta(request):
    medicos = Medico.objects.all()
    if request.method == 'POST':
        data_consulta = request.POST['data_consulta']
        medico = request.POST['medico']
        nome_cliente = request.POST['nome_cliente']
        data_nascimento = request.POST['data_nascimento']
        celular_cliente = request.POST['celular_cliente']
        email_cliente = request.POST['email_cliente']
        medico = Medico.objects.get(pk=medico)
        consulta = Consulta.objects.create(data_consulta=data_consulta, medico=medico, nome_cliente=nome_cliente,
                                           data_nascimento=data_nascimento, celular_cliente=celular_cliente,
                                           email_cliente=email_cliente)
        consulta.save()
        return redirect('listar_consulta')
    return render(request, 'criar_consulta.html', {'medicos': medicos})

def editar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == 'POST':
        data_consulta = request.POST['data_consulta']
        medico = request.POST['medico']
        nome_cliente = request.POST['nome_cliente']
        data_nascimento = request.POST['data_nascimento']
        celular_cliente = request.POST['celular_cliente']
        email_cliente = request.POST['email_cliente']
        medico = Medico.objects.get(pk=medico)
        consulta.data_consulta = data_consulta
        consulta.medico = medico
        consulta.nome_cliente = nome_cliente
        consulta.data_nascimento = data_nascimento
        consulta.celular_cliente = celular_cliente
        consulta.email_cliente = email_cliente
        consulta.save(update_fields=['data_consulta', 'medico', 'nome_cliente', 'data_nascimento', 'celular_cliente',
                                     'email_cliente'])
        return redirect('listar_consulta')
    return render(request, 'editar_consulta.html', {'consulta': consulta})

def listar_consulta(request):
    consultas = Consulta.objects.all()
    return render(request, 'listar_consulta.html', {'consultas': consultas})

def deletar_consulta(request, pk):
    consulta = Consulta.objects.get(pk=pk)
    if request.method == 'POST':
        consulta.delete()
        return redirect('listar_consulta')
    return render(request, 'deletar_consulta.html', {'consulta': consulta})
