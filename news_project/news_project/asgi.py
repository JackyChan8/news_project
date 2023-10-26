import os
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from news.consumers import NewsConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path('ws/news/<int:news_id>/', NewsConsumer.as_asgi()),
    ])
})
