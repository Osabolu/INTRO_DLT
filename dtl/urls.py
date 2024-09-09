from django.urls import path
from . import views

urlpatterns = [
    path("dtl/", views.bio, name="dtl")
]