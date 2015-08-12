from django.contrib import admin

# Register your models here.
from models import StationStatus

def reset_stations(modeladmin, request, queryset):
    queryset.update(station_status='Not Ready')
reset_stations.short_description = "Reset / Not Ready"

def help_stations(modeladmin, request, queryset):
    queryset.update(station_status='Need Help')
help_stations.short_description = "Help"

def ready_stations(modeladmin, request, queryset):
    queryset.update(station_status='Ready')
ready_stations.short_description = "Ready"

class StationAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
                return False
    def status(self, obj):
        if obj.__str__() == 'Not Ready':
            return """<div style="width:100%%; height:100%%;
            background-color:red;">%s</div>""" % obj.__str__()
        if obj.__str__() == 'Need Help':
            return """<div style="width:100%%; height:100%%;
            background-color:orange;">%s</div>""" % obj.__str__()
        if obj.__str__() == 'Ready':
            return """<div style="width:100%%; height:100%%;
            background-color:green;">%s</div>""" % obj.__str__()
        return obj.__str__()
    status.allow_tags = True
    list_display = ['station_number', 'status']
    ordering = ['station_number']
    actions = [reset_stations, help_stations, ready_stations]

admin.site.register(StationStatus, StationAdmin)
