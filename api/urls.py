from django.urls import path
from api.views import (
    PingPongView,
    CreateUserView,
    ProfileListView,
    ProfileRetrieveView,
    LoginView,
)

urlpatterns = [
    path("ping/", PingPongView.as_view()),
    path("users/", CreateUserView.as_view()),
    path("users/login", LoginView.as_view()),
    path("profiles/", ProfileListView.as_view()),
    path("profiles/<username>", ProfileRetrieveView.as_view()),
]
