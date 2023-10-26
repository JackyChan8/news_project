from django.shortcuts import render, get_object_or_404
from taggit.models import Tag

from statistic.models import NewsStatistic
from .models import News, Images, Like, DisLike


def index(request):
    """Get All News"""
    news = News.objects.all().order_by('id')[0:6]
    tags = News.tags.most_common()
    return render(request, 'home.html', {'news': news, 'tags': tags})


def tagged(request, slug):
    """Get News by Tag"""
    tag = get_object_or_404(Tag, slug=slug)
    print(tag)
    news = News.objects.filter(tags=tag)[0:6]
    print(news)
    tags = News.tags.most_common()
    return render(request, 'home.html', {'news': news, 'tag': tag, 'tags': tags})


def news(request, news_id):
    """Get News by ID"""
    news = get_object_or_404(News, id=news_id)
    photos = Images.objects.filter(news=news)
    # Add Statistic Views
    stat, created = NewsStatistic.objects.get_or_create(
        news=news
    )
    # Get Likes / Dislikes
    likes, created = Like.objects.get_or_create(news=news)
    dislikes, created = DisLike.objects.get_or_create(news=news)
    stat.views += 1
    stat.save(update_fields=['views'])
    return render(
        request, 'news.html',
        {
            'news': news,
            'photos': photos,
            'views': stat.views,
            'likes': likes,
            'dislikes': dislikes,
        })
