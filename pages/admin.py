from django.contrib import admin

# Register your models here.
from .models import Team
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))
    
    thumbnail.short_description = 'photo'

    list_display = ('id','thumbnail','firstname','designation','created_date')
    list_display_links = ('id','firstname','thumbnail')
    search_fields = ('firstname', 'lastname','designation')
    list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)
