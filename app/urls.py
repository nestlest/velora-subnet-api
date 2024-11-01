from django.urls import path
from .views import PoolEventsDownload, index

urlpatterns = [
    path('pool-events', PoolEventsDownload.as_view(), name='pool-events-download'),
    path('', index, name='index'),  # Add this line for the index view
]