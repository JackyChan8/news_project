from django.db import models

from news.models import News


class NewsStatistic(models.Model):
    news = models.ForeignKey(News, default=None, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.news.title
