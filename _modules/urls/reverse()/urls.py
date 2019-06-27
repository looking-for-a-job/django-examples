from django.urls import path
from . import views

urlpatterns = [
    path('view-path/', views.my_view, name='view-name'),
]
