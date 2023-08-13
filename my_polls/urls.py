from django.urls import path

from . import views

app_name = "my_polls"
urlpatterns = [
    # Index - example: /my_polls/
    path("", views.IndexView.as_view(), name="index"),
    # Detail: /my_polls/5
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # Results: my_polls/5/results
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # Vote: my_polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote")
    ]
