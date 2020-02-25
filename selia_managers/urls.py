from django.urls import path
from selia_managers import views


urlpatterns = [
    path('', views.management, name='management'),
    # path('collections', views.collections, name='collections'),
    path(
        'collections',
        views.listManagerCollectionsView.as_view(),
        name='collections'),
]
