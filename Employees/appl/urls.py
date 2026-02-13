from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path("task/", views.task),   # ← comma needed here
    path("showEmployee/", views.Show_employee),
]