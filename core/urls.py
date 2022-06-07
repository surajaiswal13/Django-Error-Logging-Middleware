from core.viewsets import ErrorLogViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'error-logs', ErrorLogViewSet, basename='error-logs')
urlpatterns = router.urls