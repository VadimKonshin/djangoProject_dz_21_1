from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import catalog


app_name = NewappConfig.name
urlpatterns = [

    path('', catalog, name='home')
]
