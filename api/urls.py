from django.urls import path
from api.views import PingPongView, CreateUserView

urlpatterns = [
    path("ping/", PingPongView.as_view()),
    path("users/", CreateUserView.as_view()),
]
