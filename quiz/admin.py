from django.contrib import admin
from .models import *

class QuizQuestionBankAdmin(admin.ModelAdmin):
    list_display = ('category', 'part1', 'part2')
    list_filter = ['category']
    search_fields = ['category','part1','part2']
    actions_on_bottom=True
admin.site.register(QuizQuestionBank,QuizQuestionBankAdmin)


class QuizAdmin(admin.ModelAdmin):
    list_display = ('category', 'is_active', 'name', 'user', 'code')
    list_filter = ['category', 'is_active']
    search_fields = ['category', 'is_active', 'name', 'user']
    actions_on_bottom=True
admin.site.register(Quiz,QuizAdmin)


class QuizResponseAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'quizcode', 'respcode')
    list_filter = ['quizcode']
    search_fields = ['name', 'quizcode', 'respcode']
    actions_on_bottom=True
    def category(self, obj):
        return Quiz.objects.get(code=obj.quizcode).category
admin.site.register(QuizResponse,QuizResponseAdmin)

