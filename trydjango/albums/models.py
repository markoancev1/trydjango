from django.db import models
from datetime import datetime
# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=25, blank=False)
    singer = models.ForeignKey("singers.Singer", on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    released = models.BooleanField(default=False)

    def __str__(self):
        return self.singer


