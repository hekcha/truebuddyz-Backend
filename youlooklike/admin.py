from django.contrib import admin
from .models import *


class YouLookLikeAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ['category']
    actions_on_bottom=True
admin.site.register(YouLookLike,YouLookLikeAdmin)


class YouLookLikeScoreAdmin(admin.ModelAdmin):
    list_display = ('category','code')
    list_filter = ['category','code']
    search_fields = ['category','code']
    actions_on_bottom=True
admin.site.register(YouLookLikeScore,YouLookLikeScoreAdmin)
