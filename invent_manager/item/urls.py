from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    path("", views.list, name = "list"),
    path("register/", views.register, name="register"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("detail/<int:pk>/delete", views.delete, name="delete"),
    #path("update/<int:pk>/", views.update, name="update"),
]