from django.contrib import admin
from .models import Users


class UsersModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'get_date_created']

    def get_date_created(self, obj):
        return obj.date

    get_date_created.short_description = 'Date Created'


admin.site.register(Users, UsersModelAdmin)
