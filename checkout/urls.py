from django.urls import path
from . import views
from .webhooks import webhook


app_name = 'orders'

urlpatterns = [
    path('create', views.create_checkout, name='create_checkout'),
    path('wh/', webhook, name='webhook'),
]
