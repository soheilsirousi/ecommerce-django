from django.urls import path
from store.views import *

urlpatterns = [
    path('health/', health, name='health'),
]