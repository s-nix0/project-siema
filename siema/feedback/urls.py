from django.urls import path
from .views import feedback_view

urlpatterns = [
    path('', feedback_view, name='feedback_form'),
    # path('sukses/', feedback_success, name='feedback_success'),
]
