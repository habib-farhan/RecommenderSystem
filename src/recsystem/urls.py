from django.conf.urls import url
from . import views

app_name = 'recsystem'
urlpatterns = [

    # /recsystem/
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^add_question/$', views.add_question, name='add_question'),
    url(r'^question_form/$', views.question_form, name='question_form'),
    url(r'^add_answer/$', views.add_answer, name='add_answer'),
    url(r'^add_relation/$', views.add_relation, name='add_relation'),
    url(r'^add_advice/$', views.add_advice, name='add_advice'),
    url(r'^save_question/$', views.save_question, name='save_question'),
    url(r'^details/$', views.details, name='details'),
    url(r'^followUp/$', views.followUp, name='followUp'),
    url(r'^getAns/$', views.getAns, name='getAns'),
    url(r'^getSliderAdvice/$', views.getSliderAdvice, name='getSliderAdvice'),
    url(r'^getAdvices/$', views.getAdvices, name='getAdvices'),
    url(r'^saveData/$', views.saveData, name='saveData'),
    url(r'^saveEditedData/$', views.saveEditedData, name='saveEditedData'),
    url(r'^editQuestion/(?P<question_id>[0-9]+)/$', views.editQuestion, name='editQuestion'),
    url(r'^delete/(?P<question_id>[0-9]+)/$', views.delete, name='delete'),

    # /recsystem/123/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail')
]
