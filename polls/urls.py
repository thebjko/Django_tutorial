from django.urls import path

from . import views

app_name = 'POLLS'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='INDEX'),
    # ex: /polls/5/
    path('<int:pk>', views.DetailView.as_view(), name='DETAIL'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='RESULTS'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='VOTE'),
]