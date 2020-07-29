from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('register/', views.register, name="register"),
    path('list/', views.list, name='list'),
    path('detail/<int:pk>/', views.detail, name='detail' ),
    path('detail/<int:pk>/delete/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
]