from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Add any other fields here

    def __str__(self):
        return self.title
