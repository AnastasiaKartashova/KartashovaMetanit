from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    genre = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Movies'
        verbose_name_plural = 'Movies'