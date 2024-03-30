from django.contrib import admin

from Mission.models import Mission

# Register your models here.
class MissionAdmin(admin.ModelAdmin):
    model = Mission
    list_display = ['name', 'mission']

admin.site.register(Mission, MissionAdmin)
