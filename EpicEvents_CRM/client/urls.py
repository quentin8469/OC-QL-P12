from rest_framework.routers import DefaultRouter
from .views import ClientViewset

router = DefaultRouter()
router.register(r"",ClientViewset, basename='client')

urlpatterns = router.urls