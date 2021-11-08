from django.db import models

class About(models.Model):
    body = models.TextField()

    def __str__(self):
        return self.body