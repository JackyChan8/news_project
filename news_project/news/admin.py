from django.contrib import admin

from .models import News, Images


class ImageAdmin(admin.StackedInline):
    model = Images


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'tags')
    list_filter = ('title', 'tags')
    inlines = (ImageAdmin,)


admin.site.register(News, NewsAdmin)
