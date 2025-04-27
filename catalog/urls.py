from django.urls import path
from . import views

urlpatterns = [
    path("home_view/", views.home_view, name="home_view"),
    path("contact_view/", views.contact_view, name="contact_view"),
    path(
        "contact/success/<str:name>",
        views.contact_success_view,
        name="contact_success_view",
    ),
]
