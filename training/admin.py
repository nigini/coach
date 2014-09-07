from django.contrib import admin
from training.models import Athlete,Activity

class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 1

class AthleteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [ActivityInline]
    list_display = ('name', 'last_registered_activity_date')
    #list_filter = ['last_registered_activity_date']

class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['athlete']}),
        ('When', {'fields': ['date']}),
        ('What', {'fields': ['sport', 'description']})
    ]

admin.site.register(Athlete, AthleteAdmin)
admin.site.register(Activity, ActivityAdmin)