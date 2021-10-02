from django.contrib import admin
from .models import *


class RatingAdmin(admin.ModelAdmin):
    list_display = ('value', 'user')
    list_filter = ['value']
    actions_on_bottom=True
admin.site.register(Rating,RatingAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('rating','user','text')
    list_filter = ['rating']
    search_fields = ['rating','user','text']
    actions_on_bottom=True
admin.site.register(Feedback,FeedbackAdmin)


class ContributionAdmin(admin.ModelAdmin):
    list_display = ('user','name','game','message')
    list_filter = ['user']
    search_fields = ['user','name','email','game','message']
    actions_on_bottom=True
admin.site.register(Contribution,ContributionAdmin)


class TrendingAdmin(admin.ModelAdmin):
    ordering = ['rank','-is_active']
    list_display = ('text', 'rank', 'is_active')
    list_filter = ['is_active', 'rank']
    search_fields = ['rank', 'is_active', 'text', 'link']
    actions_on_bottom=True
admin.site.register(Trending,TrendingAdmin)


class NewGamesAdmin(admin.ModelAdmin):
    ordering = ['rank','-is_active']
    list_display = ('text', 'rank', 'is_active')
    list_filter = ['is_active', 'rank']
    search_fields = ['rank', 'is_active', 'text', 'link']
    actions_on_bottom=True
admin.site.register(NewGames,NewGamesAdmin)


class GamesDataAdmin(admin.ModelAdmin):
    ordering = ['-date']
    list_display = ('game', 'subGame', 'user', 'text', 'date')
    list_filter = ['game', 'subGame', 'text']
    search_fields = ['game', 'subGame', 'user', 'date', 'text']
    actions_on_bottom=True
admin.site.register(GamesData,GamesDataAdmin)

