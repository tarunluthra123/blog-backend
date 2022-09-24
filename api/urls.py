from django.urls import path
from api.views import (
    PingPongView,
    CreateUserView,
    ProfileListView,
    ProfileRetrieveView,
    LoginView,
    ArticleCreateListView,
    ArticleRetrieveUpdate,
    CommentListCreateView,
)

urlpatterns = [
    path("ping/", PingPongView.as_view()),
    path("users/", CreateUserView.as_view()),
    path("users/login", LoginView.as_view()),
    path("profiles/", ProfileListView.as_view()),
    path("profiles/<username>", ProfileRetrieveView.as_view()),
    path("articles/", ArticleCreateListView.as_view()),
    path("articles/<slug>", ArticleRetrieveUpdate.as_view()),
    path("articles/<slug>/comments/", CommentListCreateView.as_view()),
]
