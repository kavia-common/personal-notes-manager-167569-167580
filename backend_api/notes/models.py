from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract base model that provides created_at and updated_at timestamps.
    """
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the record was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="When the record was last updated.")

    class Meta:
        abstract = True


class Note(TimeStampedModel):
    """
    Represents a personal note with title and content.
    """
    title = models.CharField(max_length=255, db_index=True, help_text="Short title of the note.")
    content = models.TextField(blank=True, help_text="Full content of the note.")

    class Meta:
        ordering = ["-updated_at", "-created_at"]
        indexes = [
            models.Index(fields=["updated_at"], name="note_updated_idx"),
            models.Index(fields=["created_at"], name="note_created_idx"),
        ]
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"Note<{self.pk}>: {self.title}"
