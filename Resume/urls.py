from django.urls import path
from .views import IndexPAge

urlpatterns = [
    path('', IndexPAge.as_view(), name='home_page')
]