from django.conf.urls import url
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(
        r'^managers/',
        include(('selia_managers.urls', 'selia_managers'))),
    url(
        r'^registration/',
        include('selia_registration.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
