from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from taggit.models import Tag

from news.models import News
from .serializers import NewsSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def view_news(request):
    """Get all News"""
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def view_one_news(request, news_id):
    """Get News By ID"""
    news = get_object_or_404(News, pk=news_id)
    serializer = NewsSerializer(instance=news)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def load_more(request):
    """Get News by Pagination"""
    offset = int(request.GET.get('offset', 0))
    limit = int(request.GET.get('limit', 3))

    # Tag
    tag = request.GET.get('tag')
    if tag:
        tag = get_object_or_404(Tag, slug=tag)
        news = News.objects.filter(tags=tag).order_by('id')[offset: offset + limit]
    else:
        news = News.objects.all().order_by('id')[offset: offset + limit]
    data = NewsSerializer(news, many=True)
    return Response(data.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def view_add(request):
    """Add News"""
    data = request.data
    news = NewsSerializer().create({
        'title': data['title'],
        'text': data['text'],
        'image': data['image'],
        'tags': data['tags']
    })
    if news:
        news.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def view_delete(request, news_id):
    """Delete News"""
    news = get_object_or_404(News, pk=news_id)
    news.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def view_update(request, news_id):
    """Update News"""
    data = request.data
    if 'tags' in data:
        data = {
            'tags': data['tags']
        }

    news = get_object_or_404(News, pk=news_id)
    data = NewsSerializer().update(news, data)
    if data:
        data.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
