from django.urls import path
from selia_managers import views


urlpatterns = [
    path('', views.management, name='management'),
    # path('collections', views.collections, name='collections'),
    path(
        'collections',
        views.listManagerCollectionsView.as_view(),
        name='collections'),
    path(
        'collections/detail/<pk>/',
        views.DetailCollectionView.as_view(),
        name='collection_detail'),
    path(
        'collection/create/2/',
        views.listManagerCollectionsView.as_view(),
        name='create_collection'),
]
