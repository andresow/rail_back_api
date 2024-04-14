from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from scale import views

router = routers.DefaultRouter()
router.register(r'scale', views.ScaleView, 'scale')

urlpatterns = [
    path("api/v1/",include(router.urls)),

]