from django.contrib import admin
from .models import *


class RfQuestionBankAdmin(admin.ModelAdmin):
    list_display = ('category', 'que')
    list_filter = ['category']
    search_fields = ['category','que']
    actions_on_bottom=True
admin.site.register(RfQuestionBank,RfQuestionBankAdmin)

