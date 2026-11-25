# from django.urls import path
# from . import views
# 
# urlpatterns = [
#     path("", views.index, name="index"),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("delete/<int:id>/", views.delete_student, name="delete_student"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]