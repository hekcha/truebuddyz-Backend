from django.contrib import admin
from .models import *


class YouLookLikeAdmin(admin.ModelAdmin):
    list_display = ('category','que')
    list_filter = ['category']
    search_fields = ['category','que','optionA','optionB','optionC','optionD']
    actions_on_bottom=True
admin.site.register(YouLookLike,YouLookLikeAdmin)



class YouLookLikeResultAdmin(admin.ModelAdmin):
    list_display = ('category', 'name')
    list_filter = ['category']
    search_fields = ['category', 'name', 'text']
    actions_on_bottom=True
admin.site.register(YouLookLikeResult,YouLookLikeResultAdmin)
