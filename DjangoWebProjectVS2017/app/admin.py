
from django.contrib import admin
from app.models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Topic',               {'fields': ['topic']}),

    ]
    list_display = ('question_text', 'pub_date','topic')
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)