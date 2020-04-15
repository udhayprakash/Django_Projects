from Clusters import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Clusters', views.ClusterDetailsView)

urlpatterns = [
    path('index/', views.index, name='index'),
    path('clusters_api/', views.ClustersView.as_view(), name='clusters_api'),
    path('', include(router.urls))
]
