from django.urls import path
from .views import MyView

urlpatterns = [
    path('mine/', MyView.as_view(), name='my-view'),
]
