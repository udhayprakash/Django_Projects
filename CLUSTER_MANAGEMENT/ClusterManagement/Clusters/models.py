from django.db import models


# Create your models here.
class ClusterDetails(models.Model):
    cluster_name = models.CharField(max_length=50, unique=True)
    nodes_count = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cluster_name

    class Meta:
        ordering = ['cluster_name']
