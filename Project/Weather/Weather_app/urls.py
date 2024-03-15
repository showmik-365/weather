from django.urls import path
from Weather_app import views

app_name = 'Weather_app'

urlpatterns = [
    path('',views.index),
]