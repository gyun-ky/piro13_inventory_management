from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    path("", views.list, name = "list"),
    path("register/", views.register, name="register"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("detail/<int:pk>/delete/", views.delete, name="delete"),
    path("update/<int:pk>/", views.update, name="update"),
]

urlpatterns += [
    path('account/register/', views.a_register, name="a_register"),
    path('account/list/', views.a_list, name='a_list'),
    path('account/detail/<int:pk>/', views.a_detail, name='a_detail'),
    path('account/detail/<int:pk>/delete/', views.a_delete, name='a_delete'),
    path('account/update/<int:pk>/', views.a_update, name='a_update'),
]