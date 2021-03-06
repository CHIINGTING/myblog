from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    # 繼承models.Model class
    title = models.CharField(max_length=200)  # max 200 bit
    slug = models.CharField(max_length=200)
    body = models.TextField()  # unlimit size
    pub_date = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ('-pub_date'),
        db_table = 'articels'

    def __str__(self):
       return self.body
