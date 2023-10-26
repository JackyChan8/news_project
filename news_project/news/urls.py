from django.urls import path, re_path

from .views import index, tagged, news

urlpatterns = [
    path('', index, name='home'),
    path('news/<int:news_id>', news, name='news'),
    re_path(r'^tag/(?P<slug>[-\w]*)/$', tagged, name="tagged"),
]
