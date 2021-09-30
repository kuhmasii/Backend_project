from django.urls import path
from . import views
app_name = "resume"

urlpatterns = [
    path("",views.index, name="index"),
    path("project/<int:detail_pk>/", views.project, name="project"),
    path("login/", views.sign_account, name='sign_account'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("logout/", views.sign_out_account, name='sign_out_account'),
]