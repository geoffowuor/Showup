from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('event/<str:event_name>/', views.event_detail, name='event_detail'),
    path('search/', views.search, name='search'),
]
