from django.db import models

from django.db import models

class Repository(models.Model):
    name = models.CharField(max_length=100)
    github_username = models.CharField(max_length=100)
    github_external_id = models.IntegerField(unique=True)
    url = models.URLField()
    stars = models.IntegerField()

    def __str__(self):
        return self.name
