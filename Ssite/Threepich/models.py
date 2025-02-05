from django.db import models

class Threepich(models.Model):
        title = models.CharField(max_length = 255)
        cost = models.TextField(blank = True)
        weight = models.TextField(blank = True)
        content = models.TextField(blank = True)
        photo = models.ImageField(upload_to="photo/%Y/%m/%d")
        time_create = models.DateTimeField(auto_now_add = True)
        time_update = models.DateTimeField(auto_now = True)
        is_published = models.BooleanField(default=True)
# Create your models here.


        def __str__(self):
                return self.title