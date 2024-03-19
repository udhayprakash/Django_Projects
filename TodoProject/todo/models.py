from django.db import models

# PRIORITY_CHOICES = (
#     ('Low', 'Low'),
#     ('Medium', 'Medium'),
#     ('High', 'High')
# )
STATUS_CHOICES = (
    ('created', 'created'),
    ('updated', 'updated'),
    ('archived', 'archived')
)


class Tasks(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, default='')
    # priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    action = models.CharField(max_length=8, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    target_date = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']


class AuditHistory(models.Model):
    description = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        model_name = self.__class__.__name__
        fields_str = ", ".join((f"{field.name}={getattr(self, field.name)}" for field in self._meta.fields))
        return f"{model_name}({fields_str})"
