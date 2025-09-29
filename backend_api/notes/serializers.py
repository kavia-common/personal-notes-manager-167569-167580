from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    # PUBLIC_INTERFACE
    class Meta:
        """Serializer for Note objects."""
        model = Note
        fields = ("id", "title", "content", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")
