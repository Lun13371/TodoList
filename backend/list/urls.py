from django.urls import path

from backend.list import views

urlpatterns = [
    path('api/items/', views.get_items),
]