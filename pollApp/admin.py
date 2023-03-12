from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = (
        ('Published Date Information', {
            "fields": (
                ['pub_date']
            ),
        }),
        ('Question Information', {
            "fields": (
                ['question_text']
            ),
        }),
    )
    
    

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)