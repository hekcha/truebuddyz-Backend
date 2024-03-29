from django.contrib import admin
from .models import *


class HowWellUKnowAdmin(admin.ModelAdmin):
    list_display = ('category', 'que', 'ans')
    list_filter = ['category','ans']
    search_fields = ['category','que','optionA','optionB','optionC','optionD']
    actions_on_bottom=True
admin.site.register(HowWellUKnow,HowWellUKnowAdmin)


class HowWellUKnowScoreAdmin(admin.ModelAdmin):
    list_display = ('category', 'score', 'complement')
    list_filter = ['category', 'score','complement']
    search_fields = ['category','complement','message','score']
    actions_on_bottom=True
admin.site.register(HowWellUKnowScore,HowWellUKnowScoreAdmin)

