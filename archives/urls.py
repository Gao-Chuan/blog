from django.urls import path

from . import views

app_name = 'archives'

urlpatterns = [
    path('', views.list, name="list"),
    path('paper/<slug:name>', views.archives, name="paper"),
]
