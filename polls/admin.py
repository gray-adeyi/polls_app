from django.contrib import admin
from . import models

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields':['pub_date']}),
    ]

# Register your models here.
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice)
