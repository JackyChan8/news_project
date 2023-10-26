from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rest Framework
    path('api-auth/', include('rest_framework.urls')),
    # News
    path('', include('news.urls')),
    # Statistics
    path('statistics/', include('statistic.urls')),
    # Rest API
    path('api/news/', include('api.urls')),
]
