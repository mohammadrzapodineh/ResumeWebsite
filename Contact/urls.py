from django.urls import path
from .views import contact_me

app_name = 'Contact'
urlpatterns = [
    path('contact-me/', contact_me, name='contact_me')
]