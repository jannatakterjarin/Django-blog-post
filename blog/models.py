import uuid
from django.db import models


class BlogPost(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
