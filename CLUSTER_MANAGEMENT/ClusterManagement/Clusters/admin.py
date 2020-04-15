from Clusters.models import ClusterDetails
from django.contrib import admin


class ClusterDetailsAdmin(admin.ModelAdmin):
    list_display = ['cluster_name', 'nodes_count', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

    class Meta:
        models = ClusterDetails


admin.site.register(ClusterDetails, ClusterDetailsAdmin)
