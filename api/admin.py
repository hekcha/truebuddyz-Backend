from django.contrib import admin
from .models import *

admin.site.register(Rating)

admin.site.register(Quiz)
admin.site.register(QuizQuestionBank)
admin.site.register(QuizResponse)

admin.site.register(RfQuestionBank)

