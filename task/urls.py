from django.urls import path
from .views import create_task, home_page

urlpatterns = [
    path("", home_page, name="home_page"),
    path("task/create/", create_task, name="create_task"),
]
