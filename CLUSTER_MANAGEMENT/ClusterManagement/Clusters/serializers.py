from Clusters.models import ClusterDetails
from rest_framework import serializers


class ClusterDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClusterDetails
        fields = ('id', 'url', 'cluster_name', 'nodes_count')
