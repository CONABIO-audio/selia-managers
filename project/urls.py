from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [
    url(
        r'^managers/',
        include(('selia_managers.urls', 'selia_managers')))
]
