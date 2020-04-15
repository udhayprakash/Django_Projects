from Clusters.models import ClusterDetails
from Clusters.serializers import ClusterDetailsSerializer
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView


def index(request):
    return render(request, 'index.html', context={}, status=200)


class ClusterDetailsView(viewsets.ModelViewSet):
    queryset = ClusterDetails.objects.all()
    serializer_class = ClusterDetailsSerializer


class ClustersView(GenericAPIView):
    http_method_names = ('post', 'create')

    def post(self, request, **kwargs):
        print('ClustersView - post')
        post_data = request.data
        post_data.pop('url', None)
        if post_data.get('action') == 'delete':
            selected_ids = post_data.get('selected_ids')
            ClusterDetails.objects.filter(id__in=selected_ids).delete()
        else:
            ClusterDetails.objects.filter(id=post_data.pop('id')).update(**post_data)
        return JsonResponse({'status': 'success'}, safe=False)

    def create(self, request, **kwargs):
        print('ClustersView - create')
        ClusterDetails(
            cluster_name=request.data['cluster_name'],
            nodes_count=request.data['nodes_count']
        ).save()
        return JsonResponse({'status': 'success'}, safe=False)
