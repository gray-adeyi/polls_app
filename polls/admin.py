from django.contrib import admin
from . import models

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

# Register your models here.
admin.site.register(models.Question, QuestionAdmin)
