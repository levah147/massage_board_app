from django.urls import path
from .views import HomePagesview

urlpatterns = [
    path('', HomePagesview.as_view(), name='home'),
]