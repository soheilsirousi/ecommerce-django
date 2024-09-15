from django.urls import path
from store.views import *

urlpatterns = [
    path('health/', health, name='health'),
    path('category/<str:name>/', CategoryDetailView.as_view(), name='category-page'),
]