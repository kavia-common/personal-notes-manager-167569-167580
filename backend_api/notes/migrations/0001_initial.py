# Generated initial migration for Notes app
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='When the record was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='When the record was last updated.')),
                ('title', models.CharField(db_index=True, help_text='Short title of the note.', max_length=255)),
                ('content', models.TextField(blank=True, help_text='Full content of the note.')),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
                'ordering': ['-updated_at', '-created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='note',
            index=models.Index(fields=['updated_at'], name='note_updated_idx'),
        ),
        migrations.AddIndex(
            model_name='note',
            index=models.Index(fields=['created_at'], name='note_created_idx'),
        ),
    ]
