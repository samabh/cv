from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    url = models.URLField(max_length=200, default='https://example.com')

    def __str__(self):
        return self.title