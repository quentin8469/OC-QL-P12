from rest_framework.routers import DefaultRouter
from .views import ContractViewset

router = DefaultRouter()
router.register(r"",ContractViewset, basename='contract')

urlpatterns = router.urls