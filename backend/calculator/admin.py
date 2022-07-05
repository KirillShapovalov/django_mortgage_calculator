from django.contrib import admin
from .models import MortgageOffer


class MortgageOfferAdmin(admin.ModelAdmin):
    pass


admin.site.register(MortgageOffer, MortgageOfferAdmin)
