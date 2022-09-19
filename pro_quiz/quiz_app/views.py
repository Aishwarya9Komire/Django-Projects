from django.shortcuts import render, redirect
from .models import QuizModel
from .form import *

# Create your views here.
def home(request):
    if request.method == "POST":
        questions = QuizModel.objects.all()
        score, wrong, correct, total = 0, 0, 0, 0
        for q in questions:
            total += 1
            if q.ans == request.POST.get(q.question):
                score += 1
                correct += 1
            else:
                wrong += 1
        context = {
            'score':f'{score}/{total}',
            'correct': correct,
            'wrong': wrong,
            'total': total
        }
        return render(request, 'result.html', context)
    else:
        questions = QuizModel.objects.all()
        context = {'questions' : questions}
        return render(request, 'Home.html', context)

def addQues(request):
    form = addQuestionform()
    if request.method == 'POST':
        form = addQuestionform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('addQues')
    context = {'form':form}
    return render(request, 'AddQues.html', context)