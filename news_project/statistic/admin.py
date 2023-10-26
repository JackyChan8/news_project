from django.contrib import admin

from .models import NewsStatistic


class NewsStatisticAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'views')
    list_filter = ('views',)


admin.site.register(NewsStatistic, NewsStatisticAdmin)
