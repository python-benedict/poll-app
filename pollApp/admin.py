from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = (
        ('Published Date Information', {
            "fields": (
                ['pub_date']
            ), 'classes':['collapse']
        }),
        ('Question Information', {
            "fields": (
                ['question_text']
            ), 'classes':['collapse']
        }),
    )
    
    inlines = [ChoiceInline]
    

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)