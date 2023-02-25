from django.urls import path
from problems import views

app_name = "problems"

urlpatterns = [
    # path("", views.ProblemsView.as_view(), name="problems_home"),
    path("", views.ProblemListView.as_view(), name="problem_list"),
    path("problem/<int:pk>", views.ProblemDetailView.as_view(), name="problem_detail"),
    path("problem/new", views.ProblemCreateView.as_view(), name="problem_new"),
    path("drafts/", views.DraftListView.as_view(), name="problem_draft_list"),
    path("problem/<int:pk>/publish/", views.problem_publish, name="problem_publish"),
    path("problem/<int:pk>/edit", views.ProblemUpdateView.as_view(), name="problem_edit"),
    path("problem/<int:pk>/remove", views.ProblemDeleteView.as_view(), name="problem_remove"),

    path("problem/<int:pk>/solution/", views.add_solution, name="add_solution"),
    path("solution/<int:pk>/approve", views.solution_approve, name="solution_approve"),
    path("solution/<int:pk>/remove", views.solution_remove, name="solution_remove"),
    path("solution/<int:pk>/reject", views.solution_reject, name="solution_reject"),
    path("solution/", views.SolutionListView.as_view(), name="solution_list"),
    # path("solution/<int:pk>", views.SolutionDetailView.as_view(), name="solution_detail"),
]
