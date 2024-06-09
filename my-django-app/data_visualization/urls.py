from django.urls import path
from . import views

urlpatterns = [
    path('chart/', views.chart_view, name='chart_view'),
    path('add/', views.add_data_point, name='add_data_point'),
]
