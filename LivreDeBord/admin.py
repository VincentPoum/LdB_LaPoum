from django.contrib import admin

from .models import Evenement, Histoire, Depense, ReleveEau, ReleveElec

class EvenementAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_event'
    ordering = ['-date_event']
    list_display = ('date_event','libelle')
admin.site.register(Evenement, EvenementAdmin)

class HistoireAdmin(admin.ModelAdmin):
    date_hierarchy = 'lien_event__date_event'
    ordering = ['-lien_event__date_event']
admin.site.register(Histoire, HistoireAdmin)

class DepenseAdmin(admin.ModelAdmin):
    date_hierarchy = 'lien_event__date_event'
    ordering = ['-lien_event__date_event']
admin.site.register(Depense, DepenseAdmin)

class ReleveEauAdmin(admin.ModelAdmin):
    date_hierarchy = 'lien_event__date_event'
    ordering = ['-lien_event__date_event']
admin.site.register(ReleveEau, ReleveEauAdmin)

class ReleveElecAdmin(admin.ModelAdmin):
    date_hierarchy = 'lien_event__date_event'
    ordering = ['-lien_event__date_event']
admin.site.register(ReleveElec, ReleveElecAdmin)
