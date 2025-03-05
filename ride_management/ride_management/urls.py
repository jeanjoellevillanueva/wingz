from django.urls import include
from django.urls import path


urlpatterns = [
    path(
        'api/',
        include('core.urls'),
    ),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    path(
        '__debug__/',
        include('debug_toolbar.urls')
    ),
]
