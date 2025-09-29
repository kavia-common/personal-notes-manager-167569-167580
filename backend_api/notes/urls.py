from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NoteViewSet

router = DefaultRouter()
router.register(r"notes", NoteViewSet, basename="note")

urlpatterns = [
    # PUBLIC_INTERFACE
    # /api/notes/ endpoints via router
    path("", include(router.urls)),
]
