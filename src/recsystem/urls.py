from django.conf.urls import url
from . import views

app_name = 'recsystem'
urlpatterns = [

    # /recsystem/
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^studyrec/$', views.studyrec, name='studyrec'),
    url(r'^others/$', views.others, name='others'),
    url(r'^gitrec/$', views.gitrec, name='gitrec'),
    url(r'^allAdvices/$', views.allAdvices, name='allAdvices'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^add_question/$', views.add_question, name='add_question'),
    url(r'^question_form/$', views.question_form, name='question_form'),
    url(r'^add_answer/$', views.add_answer, name='add_answer'),
    url(r'^add_relation/$', views.add_relation, name='add_relation'),
    url(r'^save_relation/$', views.save_relation, name='save_relation'),
    url(r'^add_advice/$', views.add_advice, name='add_advice'),
    url(r'^saveAdvice/(?P<advice_id>[0-9]+)/$', views.saveAdvice, name='saveAdvice'),
    url(r'^save_question/$', views.save_question, name='save_question'),
    url(r'^details/$', views.details, name='details'),
    url(r'^followUp/$', views.followUp, name='followUp'),
    url(r'^getAns/$', views.getAns, name='getAns'),
    url(r'^getSliderAdvice/$', views.getSliderAdvice, name='getSliderAdvice'),
    url(r'^getAdvices/$', views.getAdvices, name='getAdvices'),
    url(r'^saveData/$', views.saveData, name='saveData'),
    url(r'^saveEditedData/$', views.saveEditedData, name='saveEditedData'),
    url(r'^editQuestion/(?P<question_id>[0-9]+)/$', views.editQuestion, name='editQuestion'),
    url(r'^editAdvice/(?P<advice_id>[0-9]+)/$', views.editAdvice, name='editAdvice'),
    url(r'^delete/(?P<question_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^deleteAll/$', views.deleteAll, name='deleteAll'),

    # /recsystem/123/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail')
]
