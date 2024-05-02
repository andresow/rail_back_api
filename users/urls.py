from django.urls import path, include
from rest_framework import routers
from users import views

urlpatterns = [
    path("create/", views.CreateUserView.as_view()),
    path("list/", views.CreateUserView.as_view()),
    path("token/", views.CreateTokenView.as_view()),
    path("user/", views.RetreiveUpdateUserView.as_view()),

]