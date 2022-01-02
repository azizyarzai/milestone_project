

from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import say_hi, SayHiApiView, list_products, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("products", ProductViewSet, "test")

app_name = 'api'

urlpatterns = [
    path("say-hi/", say_hi),
    path("products-view/", list_products),
    path("index/", TemplateView.as_view(template_name="api.html")),
    path("", include(router.urls)),

    # path("say-hi/", SayHiApiView.as_view())
]
