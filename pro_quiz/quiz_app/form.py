from django.forms import ModelForm
from .models import *

class addQuestionform(ModelForm):
    class Meta:
        model=QuizModel
        fields="__all__"