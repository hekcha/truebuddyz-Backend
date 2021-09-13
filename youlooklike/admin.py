from django.contrib import admin
from .models import *


class YouLookLikeAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ['category']
    actions_on_bottom=True
admin.site.register(YouLookLike,YouLookLikeAdmin)


class YouLookLikeRandomAdmin(admin.ModelAdmin):
    list_display = ('category','que')
    list_filter = ['category']
    search_fields = ['category','que','optionA','optionB','optionC','optionD']
    actions_on_bottom=True
admin.site.register(YouLookLikeRandom,YouLookLikeRandomAdmin)


class YouLookLikeScoreAdmin(admin.ModelAdmin):
    list_display = ('category','code','name')
    list_filter = ['category','code','name']
    search_fields = ['category','code','name']
    actions_on_bottom=True
admin.site.register(YouLookLikeScore,YouLookLikeScoreAdmin)
