from django.urls import path
from polls import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    # path('latest.html', views.index, name='index'),
    path('latest.html', views.IndexView.as_view(), name='index'),

    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detailasdasdasd'),
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
    path('specifics/<int:pk>/', views.DetailView.as_view(), name='detail'),

    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
