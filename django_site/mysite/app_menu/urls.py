from django.urls import path

from app_menu.views import HomeView

app_name = 'app_menu'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
