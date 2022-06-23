from django.urls import include, path, re_path
from .views import FileUploadView, ClientViewSet, OrganizationViewSet, BillViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'client', ClientViewSet, basename='client')
router.register(r'organization', OrganizationViewSet, basename='Organization')
router.register(r'bill', BillViewSet, basename='bill')

urlpatterns = [
    re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
    #re_path(r'^client/(?P<filename>[^/]+)$', ClientApiView.as_view()),
    path('', include(router.urls)),
]