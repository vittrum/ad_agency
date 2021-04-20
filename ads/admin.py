from django.contrib import admin

from .models import Contract, Bill, TVAd, InternetAd, OutdoorAd

# Register your models here.

admin.site.register(Contract)
admin.site.register(Bill)
admin.site.register(TVAd)
admin.site.register(InternetAd)
admin.site.register(OutdoorAd)
