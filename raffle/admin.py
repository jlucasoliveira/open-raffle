from django.contrib import admin

from . import models


class RaffleItemInline(admin.TabularInline):
    model = models.RaffleItem
    extra = 0


@admin.register(models.Raffle)
class RaffleAdmini(admin.ModelAdmin):
    inlines = (RaffleItemInline,)
