from django.shortcuts import render

from .models import NewsStatistic


def index(request):
    """Statistic By News"""
    stats = NewsStatistic.objects.all().order_by('-views')
    print('stats: ', stats)
    return render(request, 'statistic.html', {'stats': stats})
