from django.urls import path
from django.conf import settings
from .views import Index
from django.views import View
from django.conf.urls.static import static

urlpatterns = [
  path('', Index.as_view(), name='index'),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)