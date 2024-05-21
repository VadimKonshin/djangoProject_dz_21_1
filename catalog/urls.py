from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import catalog, contacts


app_name = NewappConfig.name
urlpatterns = [

    path('', catalog, name='home'),
    path('contacts/', contacts, name='contacts')
]
