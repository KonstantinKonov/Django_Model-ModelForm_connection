from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('update/<int:pk>', views.update, name='update'),
]
