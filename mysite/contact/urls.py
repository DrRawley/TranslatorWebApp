from django.urls import path

from . import views

app_name = "contact"
urlpatterns = [
  path("", views.IndexView.as_view(), name="index"),
  path("send/", views.send, name="send"),
]