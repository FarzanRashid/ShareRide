from django.contrib import admin
from .models import Requests


class RequestsModelAdmin(admin.ModelAdmin):
    list_display = ['pickup', 'destination', 'formatted_time', 'user_id']

    def formatted_time(self, obj):
        return obj.time.strftime('%H:%M')

    formatted_time.short_description = 'Time'


admin.site.register(Requests, RequestsModelAdmin)
