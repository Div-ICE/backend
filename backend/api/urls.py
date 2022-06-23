from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .views import (BillViewSet, ClientViewSet, FileUploadView,
                    OrganizationViewSet)

router = DefaultRouter()

router.register(r'client', ClientViewSet, basename='client')
router.register(r'organization', OrganizationViewSet, basename='Organization')
router.register(r'bill', BillViewSet, basename='bill')

urlpatterns = [
    re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
    path('', include(router.urls)),
]
