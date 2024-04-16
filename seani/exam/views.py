from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Exam
from .forms import CandidateForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    user = request.user
    if user.is_superuser:
        return redirect('admin:index')
    return render(request, 'exam/home.html', {'user': user})

@login_required
def question(request, m_id, q_id=1):
    exam = request.user.exam

    # Obtener todas las preguntas del examen actual para el módulo dado
    questions = exam.breakdown_set.filter(question__module_id=m_id)
    
    try:
        # Verificar si la pregunta solicitada existe en la base de datos
        question = questions.get(pk=q_id)
    except questions.model.DoesNotExist:
        # Si la pregunta no existe, redireccionar al usuario a la página de inicio
        return redirect('exam:home')

    if request.method == 'POST':
        answer = request.POST.get('answer')
        # Procesar la respuesta y guardarla en la base de datos
        question.answer = answer
        question.save()
        
        # Redireccionar al usuario a la siguiente pregunta si existe
        next_question = questions.filter(pk__gt=q_id).first()
        if next_question:
            return redirect('exam:question', m_id=m_id, q_id=next_question.pk)
        else:
            return redirect('exam:home')

    # Renderizar la pregunta y sus detalles
    return render(request, 'exam/question.html', {
        'question': question.question,
        'answer': question.answer,
        'm_id': m_id,
        'q_id': q_id
    })

@login_required
def add_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            #Recibir datos
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            career = form.cleaned_data['career']
            stage = form.cleaned_data['stage']

            #Crear usuario
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            #Crear examen
            exam = Exam.objects.create(
                            user=user,
                            career=career,
                            stage=stage
            )
            #LLenar examen
            exam.set_modules()
            exam.set_questions()
            return HttpResponse("Usuario y contraseña creado!")

    form = CandidateForm()
    return render(request,
                  'exam/add_candidate.html',
                  {'form': form})