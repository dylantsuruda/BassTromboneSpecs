from django.contrib import admin
from .models import Feedback

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['feedback', 'datetime', 'resolved']
    list_filter = ['resolved']


admin.site.register(Feedback, FeedbackAdmin)
