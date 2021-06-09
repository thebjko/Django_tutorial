from django.urls import path

from . import views

app_name = 'POLLS'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='INDEX'),
    # ex: /polls/5/
    path('<int:question_id>', views.detail, name='DETAIL'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='RESULTS'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='VOTE'),

]