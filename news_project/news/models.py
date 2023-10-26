from django.db import models
from taggit.managers import TaggableManager


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    text = models.TextField(verbose_name='Text')
    image = models.FileField(upload_to='static/images/')
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Images(models.Model):
    news = models.ForeignKey(News, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='static/images/')

    def __str__(self):
        return self.news.title


# Like / Dislike
class Like(models.Model):
    news = models.OneToOneField(News, related_name='likes', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.count)


class DisLike(models.Model):
    news = models.OneToOneField(News, related_name='dis_likes', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.count)
