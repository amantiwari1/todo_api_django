from django.urls import path
from .views import TaskViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register("task", TaskViewSet)

urlpatterns = router.urls