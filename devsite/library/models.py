from django.db import models

# Create your models here.
class MusicItem(models.Model):
    inventory_num = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    composer_last = models.CharField(max_length=255)
    composer_first = models.CharField(max_length=255)
    arranger_last = models.CharField(max_length=255)
    arranger_first = models.CharField(max_length=255)
    ensemble = models.CharField(max_length=20)
    style = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=20)
    rating = models.CharField(max_length=20)
    last_performed = models.CharField(max_length=20)
    organized = models.BooleanField()
    notes = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
