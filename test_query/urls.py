from django.urls import path

from test_query import views

urlpatterns = [
    path('', views.index),

]
