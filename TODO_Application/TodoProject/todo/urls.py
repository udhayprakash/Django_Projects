from django.urls import path
from todo import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('tasks_api/', views.TasksView.as_view(), name='tasks_api'),

]
