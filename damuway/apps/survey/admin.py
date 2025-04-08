from django.contrib import admin
from .models import Question, AnswerOption, UserResponse

class AnswerOptionInline(admin.TabularInline):
    model = AnswerOption
    extra = 4
    fields = ('text', 'feedback')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'order']
    inlines = [AnswerOptionInline]

@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'session_key']