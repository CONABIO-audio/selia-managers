from django.urls import path
from selia_managers import views
from selia_managers.views.create_views import collection
from selia_managers.views.create_views import administrator

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
    path(
        'administrator/create/',
        administrator.CreateAdministratorManager.as_view(),
        name='create_administrator'),
    path(
        'administrator/create/1/',
        administrator.SelectCollectionAdministratorView.as_view(),
        name='create_administrator_select_collection'),
    path(
        'administrator/create/2/',
        administrator.SelectUserAdministratorView.as_view(),
        name='create_administrator_select_user'),
    path(
        'administrator/create/3/',
        administrator.CreateAdministratorView,
        name='create_administrator_create_form'),
    path(
        'administrator/create/save/',
        administrator.SaveAdministrator,
        name='create_administrator_save'),
]
