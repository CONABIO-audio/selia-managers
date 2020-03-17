from django.urls import path
from selia_managers import views
from selia_managers.views.create_views import collection

urlpatterns = [
    path('', views.management, name='management'),
    path(
        'collections',
        views.listManagerCollectionsView.as_view(),
        name='collections'),
    path(
        'collections/detail/<pk>/',
        views.DetailCollectionView.as_view(),
        name='collection_detail'),
    path(
        'collection/create/',
        collection.CreateCollectionManager.as_view(),
        name='create_collection'),
    path(
        'collection/create/1/',
        collection.SelectCollectionCollectionView.as_view(),
        name='create_collection_select_collection_type'),
    path(
        'collection/create/2/',
        collection.CreateCollectionView.as_view(),
        name='create_collection_create_form'),
]
