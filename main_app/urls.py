from rest_framework import routers

from .views import StudentViewSet

router = routers.SimpleRouter()

router.register(r"students", StudentViewSet, basename="student urls")

urlpatterns = router.urls
