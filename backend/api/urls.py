from django.urls import include, path, re_path
from .views import FileUploadView

urlpatterns = [
    re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view())
]