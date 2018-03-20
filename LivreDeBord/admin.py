from django.contrib import admin

from .models import Evenement, Histoire, Depense, ReleveEau, ReleveElec

admin.site.register(Evenement)
admin.site.register(Histoire)
admin.site.register(Depense)
admin.site.register(ReleveEau)
admin.site.register(ReleveElec)
