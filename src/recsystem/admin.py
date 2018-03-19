from django.contrib import admin
from .models import Question, Advice, Answer, FollowUp

admin.site.register(Question),
admin.site.register(Advice),
admin.site.register(FollowUp),
admin.site.register(Answer)
