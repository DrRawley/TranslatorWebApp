from django.urls import path

from . import views

app_name = 'translate'
urlpatterns = [
  path("", views.IndexView.as_view(), name="index"),
  path("translate/", views.translate, name="translate"),
  path("clear", views.clear, name="clear")
]