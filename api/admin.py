from django.contrib import admin
from .models.quiz import *
from .models.entertainment import *
from .models.howwelluknow import *
from .models.other import *


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


class QuizQuestionBankAdmin(admin.ModelAdmin):
    list_display = ('category', 'part1', 'part2')
    list_filter = ['category']
    search_fields = ['category','part1','part2']
    actions_on_bottom=True
admin.site.register(QuizQuestionBank,QuizQuestionBankAdmin)


class QuizAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'user')
    list_filter = ['category']
    search_fields = ['category','name', 'user']
    actions_on_bottom=True
admin.site.register(Quiz,QuizAdmin)


class QuizResponseAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'quizcode', 'respcode')
    list_filter = ['respcode']
    search_fields = ['name', 'quizcode', 'respcode']
    actions_on_bottom=True
    def category(self, obj):
        return Quiz.objects.get(code=obj.quizcode).category
admin.site.register(QuizResponse,QuizResponseAdmin)


class RfQuestionBankAdmin(admin.ModelAdmin):
    list_display = ('category', 'que')
    list_filter = ['category']
    search_fields = ['category','que']
    actions_on_bottom=True
admin.site.register(RfQuestionBank,RfQuestionBankAdmin)


class EntertainmentAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ['category']
    actions_on_bottom=True
admin.site.register(Entertainment,EntertainmentAdmin)


class EntertainmentResultAdmin(admin.ModelAdmin):
    list_display = ('category','code')
    list_filter = ['category','code']
    search_fields = ['category','code']
    actions_on_bottom=True
admin.site.register(EntertainmentResult,EntertainmentResultAdmin)


class HowWellUKnowAdmin(admin.ModelAdmin):
    list_display = ('category', 'que', 'ans')
    list_filter = ['category','ans']
    search_fields = ['category','que','optionA','optionB','optionC','optionD']
    actions_on_bottom=True
admin.site.register(HowWellUKnow,HowWellUKnowAdmin)


class HowWellUKnowScoreAdmin(admin.ModelAdmin):
    list_display = ('category', 'score', 'message')
    list_filter = ['category', 'score']
    search_fields = ['category','message','score']
    actions_on_bottom=True
admin.site.register(HowWellUKnowScore,HowWellUKnowScoreAdmin)


class TrendingAdmin(admin.ModelAdmin):
    ordering = ['rank','-is_active']
    list_display = ('text', 'rank', 'is_active')
    list_filter = ['is_active', 'rank']
    search_fields = ['rank', 'is_active', 'text', 'link']
    actions_on_bottom=True
admin.site.register(Trending,TrendingAdmin)

