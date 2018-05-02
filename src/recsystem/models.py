from django.db import models
from django.utils import timezone
#Question table which stores all questions and the followuo questions, each question has differetn answers and are connected
#to the answer table with a foreign key of question table in the answetr table

class Question(models.Model):
    question_title = models.CharField(max_length = 250)
    question_text = models.TextField(max_length = 3000)
    description = models.TextField(max_length = 3000)
    options_type = models.CharField(max_length = 250)
    followUp = models.BooleanField(default=False)
    max = models.CharField(max_length = 250, null=True)
    min = models.CharField(max_length = 250, null=True)
    step = models.CharField(max_length = 250, null=True)

    def __str__(self):
            return self.question_title

class Advice(models.Model):
    advice_label = models.TextField(max_length = 2000)
    advice_text = models.TextField(max_length = 3000)
    time_stamp = models.TextField( default=timezone.now, max_length= 2000)


    def __str__(self):
                return self.advice_label

#answer tabel for the answers and labels that we want to trigger in order to provide some advice in the end.
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length = 250)
    max_val = models.CharField(max_length = 250, null=True)
    min_val = models.CharField(max_length = 250, null=True)
    advices = models.ManyToManyField(Advice)

    def __int__(self):
                return self.id

#cross table for finding the followup questions associated with a particular answer
class FollowUp(models.Model):
    description = models.CharField(max_length = 250)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
