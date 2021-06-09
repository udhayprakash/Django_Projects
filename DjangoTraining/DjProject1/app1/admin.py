from django.contrib import admin

# Register your models here.
from app1.models import Choice, Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ( 'pub_date', )
    list_per_page = 5 

admin.site.register(Question , QuestionAdmin)


admin.site.register(Choice)
# admin.site.register(Question)

admin.site.site_header = 'My Admin'
admin.site.site_title = 'My Admin Portal'
admin.site.index_title = 'Welcome to Mysite Portal'