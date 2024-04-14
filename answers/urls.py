from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from answers import views

router = routers.DefaultRouter()
router.register(r'answers', views.AnswersView, 'answers')

urlpatterns = [
    path("api/v1/",include(router.urls)),
    path('docs/', include_docs_urls(title="Answers API"))
]