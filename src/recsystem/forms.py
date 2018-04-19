from django import forms
from django.contrib.auth.models import User

from .models import Question, Advice, Answer, FollowUp
#
# class QuestionForm(forms.ModelForm):
#
#     class Meta:
#         model = Question
#         fields = ['question_title', 'question_text', 'description', 'options_type']
#
#
# class AnswerForm(forms.ModelForm):
#
#     class Meta:
#         model = Answer
#         fields = ['question', 'answer_text', 'answer_label']
#
# class FollowUpForm(forms.ModelForm):
#
#      class Meta:
#          model = FollowUp
#          fields = ['description','question', 'answer']
#
class AdviceForm(forms.ModelForm):

     class Meta:
         model = Advice
         fields = ['advice_label', 'advice_text', 'time_stamp']




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
