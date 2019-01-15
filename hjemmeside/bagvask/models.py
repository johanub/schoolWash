from django.db import models
from django.contrib.auth.models import User


class Noter(models.Model):
    note = models.FileField(upload_to='noter/')
    titel = models.CharField(max_length=255)
    beskrivelse = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    usr = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_at
