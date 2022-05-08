from django.urls import path
from . import views
app_name = "resume"

urlpatterns = [
    path("",views.index, name="resume-list"),
    path("login/", views.sign_account, name='resume-login'),
    path("logout/", views.sign_out_account, name='resume-logout'),
    path("dashboard/", views.dashboard, name='resume-dashboard'),
    path("project/<int:detail_pk>/", views.project, name="resume-detail"),

]