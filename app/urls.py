from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
