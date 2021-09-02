from django.contrib import admin
from .models import Campaign, Statcampa

class CampaignAdmin(admin.ModelAdmin):
    pass


class StatcampaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Statcampa, StatcampaAdmin)