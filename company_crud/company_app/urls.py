from .views import CompanyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('company', CompanyViewSet, basename='company')
urlpatterns = router.urls