from django.urls import path
from .views import pos_view

urlpatterns = [
    path('pos/', pos_view, name='pos'),
]