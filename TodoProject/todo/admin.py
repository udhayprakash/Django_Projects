from django.contrib import admin
from todo.models import Tasks, AuditHistory


class TasksAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'target_date', 'action', 'created_at', 'updated_at']
    list_filter = ['action']
    readonly_fields = ['created_at', 'updated_at']

    class Meta:
        models = Tasks


class AuditHistoryAdmin(admin.ModelAdmin):
    list_display = ['description', 'created_at']
    readonly_fields = ['description', 'created_at']

    class Meta:
        models = AuditHistory


admin.site.register(Tasks, TasksAdmin)
admin.site.register(AuditHistory, AuditHistoryAdmin)
