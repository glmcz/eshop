from django.urls import path

from . import views

#  pokud mame vice app, tak definujeme namespace polls viz nize a pak upřesníme v sablone
#  <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    #  jelikož path ma atribut name= detail, tak lze odkazovat v sablone .html  pomoci {% url %} + jmeno
    #  ZMENA URL NA specifics
    #  path('specifics/<int:question_id>/', views.detail, name='detail'),
    #  z
    # path('<int:question_id>/', views.detail, name='detail'),
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]