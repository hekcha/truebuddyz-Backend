from django.contrib import admin
from .models import *


class RfQuestionBankAdmin(admin.ModelAdmin):
    list_display = ('category', 'que')
    list_filter = ['category']
    search_fields = ['category','que']
    actions_on_bottom=True
admin.site.register(RfQuestionBank,RfQuestionBankAdmin)


class RfRoomDetailAdmin(admin.ModelAdmin):
    list_display = ('category', 'roomId', 'playerId', 'playerName')
    list_filter = ['category', 'roomId', 'playerId']
    search_fields = ['category', 'roomId', 'playerId', 'playerName']
    actions_on_bottom=True
admin.site.register(RfRoomDetail,RfRoomDetailAdmin)

