from django.urls import path

from .views import view_news, view_one_news, view_add, view_delete, view_update, load_more


urlpatterns = [
    path('all/', view_news, name='view_news'),
    path('get/<int:news_id>', view_one_news, name='view_one_news'),
    path('create', view_add, name='view_add'),
    path('delete/<int:news_id>', view_delete, name='view_delete'),
    path('update/<int:news_id>', view_update, name='view_update'),
    # Scroll
    path('load_more/', load_more, name='pagination_news'),
]
