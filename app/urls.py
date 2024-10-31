from django.urls import path
from .views import TokenPairsDetail

urlpatterns = [
    path('pool-events', TokenPairsDetail.as_view(), name='pool-events-list'),
]