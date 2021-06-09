from django.urls import path, include
from ftp_to_db import views


urlpatterns = [
    path('', views.FTPCredentialsCreateView.as_view(), name='create_view'),
    path('update/', views.FTPCredentialsCreateView.as_view(), name='update_view'),

    path('detail/<int:question_id>/', views.detail, name='detail_view'),
]