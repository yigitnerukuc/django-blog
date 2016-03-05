from django.db import models
from django.utils import timezone


# Create your models here.

class Yazi(models.Model):
    yazar = models.ForeignKey('auth.User')
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    olusturulma_tarihi = models.DateTimeField(
        default=timezone.now
    )
    yayinlanma_tarihi = models.DateTimeField(
        blank=True, null=True
    )

    def yayinla(self):
        self.yayinlanma_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik
