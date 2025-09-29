from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    PUBLIC_INTERFACE
    A viewset providing CRUD operations for personal notes.

    Endpoints:
    - GET /api/notes/ : List notes
    - POST /api/notes/ : Create note
    - GET /api/notes/{id}/ : Retrieve note
    - PUT /api/notes/{id}/ : Full update note
    - PATCH /api/notes/{id}/ : Partial update note
    - DELETE /api/notes/{id}/ : Delete note
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    @swagger_auto_schema(
        operation_id="list_notes",
        operation_summary="List notes",
        operation_description="Retrieve a list of all personal notes ordered by most recently updated.",
        responses={200: NoteSerializer(many=True)},
        tags=["notes"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="create_note",
        operation_summary="Create note",
        operation_description="Create a new personal note.",
        request_body=NoteSerializer,
        responses={201: NoteSerializer()},
        tags=["notes"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="retrieve_note",
        operation_summary="Retrieve note",
        operation_description="Retrieve a note by its ID.",
        responses={200: NoteSerializer()},
        tags=["notes"],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="update_note",
        operation_summary="Update note",
        operation_description="Replace an existing note with the provided data.",
        request_body=NoteSerializer,
        responses={200: NoteSerializer()},
        tags=["notes"],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="partial_update_note",
        operation_summary="Partial update note",
        operation_description="Partially update an existing note.",
        request_body=NoteSerializer,
        responses={200: NoteSerializer()},
        tags=["notes"],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="delete_note",
        operation_summary="Delete note",
        operation_description="Delete a note by its ID.",
        responses={204: "No Content"},
        tags=["notes"],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=["get"], url_path="health", url_name="health")
    @swagger_auto_schema(
        operation_id="notes_health",
        operation_summary="Notes API health",
        operation_description="Simple readiness/health endpoint for the Notes API group.",
        manual_parameters=[],
        responses={200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={"status": openapi.Schema(type=openapi.TYPE_STRING)},
        )},
        tags=["notes"],
    )
    def health(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)
