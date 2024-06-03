from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import catalog, contacts, product, catalog_products

app_name = CatalogConfig.name
urlpatterns = [

    path('catalog/', catalog, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('', product, name='product'),
    path('product/<int:pk>/', catalog_products, name='catalog_products'),
]