from django.urls import path
from .views import UserActivationView



urlpatterns = [

	path('users/activation/<str:uid>/<str:token>/', UserActivationView.as_view()),
]