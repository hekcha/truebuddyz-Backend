from django.contrib import admin
from .models import *


class ThisOrThatAdmin(admin.ModelAdmin):
    list_display = ('category', 'optionA', 'optionB')
    list_filter = ['category']
    search_fields = ['category', 'optionA', 'optionB']
    actions_on_bottom=True
admin.site.register(ThisOrThat,ThisOrThatAdmin)

class WouldYouRatherAdmin(admin.ModelAdmin):
    list_display = ('category', 'que', 'optionA', 'optionB')
    list_filter = ['category']
    search_fields = ['category', 'que', 'optionA', 'optionB']
    actions_on_bottom=True
admin.site.register(WouldYouRather,WouldYouRatherAdmin)

