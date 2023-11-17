from django.db import models


class Feedback(models.Model):
    nama = models.CharField(max_length=255)
    kontak = models.CharField(max_length=255, blank=True, null=True)
    pesan = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama} | {self.pesan} | {self.timestamp}"
