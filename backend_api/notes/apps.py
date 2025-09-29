from django.apps import AppConfig


class NotesConfig(AppConfig):
    """Django AppConfig for the Notes application."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "notes"
    verbose_name = "Notes"
