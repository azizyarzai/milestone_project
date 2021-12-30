

from django.urls import path, include

from .views import say_hi, SayHiApiView, list_products, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("products", ProductViewSet, "test")

app_name = 'api'

urlpatterns = [
    path("say-hi/", say_hi),
    path("products-view/", list_products),
    path("", include(router.urls)),

    # path("say-hi/", SayHiApiView.as_view())
]
