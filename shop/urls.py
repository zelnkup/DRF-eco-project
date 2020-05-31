from django.urls import path
from . import views

app_name = 'shop'

urlpatterns= [
    path('', views.ProductListView.as_view()),
    path('<int:id>/<slug:slug>', views.ProductDetailView.as_view()),
]