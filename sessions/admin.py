from django.contrib import admin
from .models import Session

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('course', 'tutor', 'student', 'date', 'start_time', 'end_time', 'status')
    list_filter = ('status', 'date', 'tutor', 'student')
    search_fields = ('course__title', 'tutor__username', 'student__username')
