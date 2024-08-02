from django.urls import path

from . import views

urlpatterns = [
    path("solution/", views.SolutionView.as_view(), name="solution"),
]
