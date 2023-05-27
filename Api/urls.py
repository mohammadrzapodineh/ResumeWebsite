from django.urls import path, include

app_name = 'Api'
urlpatterns = [
    path('v1/', include('Api.V1.urls'))
]