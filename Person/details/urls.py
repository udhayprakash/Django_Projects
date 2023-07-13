from django.urls import path
from details.views import PersonListCreateView, PersonRetrieveUpdateDestroyView

urlpatterns = [
    path('api/persons/', PersonListCreateView.as_view(), name='person-list'),
    path('api/persons/<int:pk>/', PersonRetrieveUpdateDestroyView.as_view(), name='person-detail'),
]
