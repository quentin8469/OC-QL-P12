from rest_framework.routers import DefaultRouter
from .views import EventViewset

router = DefaultRouter()
router.register(r"",EventViewset, basename='event')

urlpatterns = router.urls