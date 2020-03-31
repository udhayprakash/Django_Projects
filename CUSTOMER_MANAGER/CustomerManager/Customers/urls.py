from Customers import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Customers', views.CustomerDetailsView)

urlpatterns = [
    path('', include(router.urls))
]
