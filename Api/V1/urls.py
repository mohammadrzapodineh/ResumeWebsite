from django.urls import path
from .views import PortfilloListApiView, portfillo_by_category_list


app_name = 'api-v1'
urlpatterns = [
    path('portfillo/', PortfilloListApiView.as_view(), name='portfillo_list'),
    path('portfillo/get_by_categoty/<int:category_id>/', portfillo_by_category_list, name='portfillo_by_category_list')
]