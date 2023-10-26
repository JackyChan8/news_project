import json
from django.db.models import F
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import News, Like, DisLike


class NewsConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.news_id = None
        self.news_group_id = None
        self.news = None

    def connect(self):
        self.news_id = self.scope['url_route']['kwargs']['news_id']
        self.news_group_id = f'chat_{self.news_id}'
        self.news = News.objects.get(pk=self.news_id)

        # connection has to be accepted
        self.accept()

        # join the room group
        async_to_sync(self.channel_layer.group_add)(
            self.news_group_id,
            self.channel_name,
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.news_group_id,
            self.channel_name,
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['type']

        if message == 'like':
            like = Like.objects.get(news__pk=self.news_id)
            like.count = F('count') + 1
            like.save()
        elif message == 'dislike':
            dis_like = DisLike.objects.get(news__pk=self.news_id)
            dis_like.count = F("count") + 1
            dis_like.save()

        # send chat message event to the room
        async_to_sync(self.channel_layer.group_send)(
            self.news_group_id,
            {
                'type': 'news_events',
                'message': message,
            }
        )

    def news_events(self, event):
        self.send(text_data=json.dumps(event))
