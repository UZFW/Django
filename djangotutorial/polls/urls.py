from django.urls import path
from . import views


app_name = "polls"


urlpatterns = [
    # Bosh sahifa
    path(
        "",
        views.IndexView.as_view(),
        name="index",
    ),

    # Savol tafsilotlari
    path(
        "<int:pk>/",
        views.DetailView.as_view(),
        name="detail",
    ),

    # Natijalar
    path(
        "<int:pk>/results/",
        views.ResultsView.as_view(),
        name="results",
    ),

    # Ovoz berish
    path(
        "<int:question_id>/vote/",
        views.vote,
        name="vote",
    ),
]