from django.db import models
from django.utils import timezone

# Create your models here.

class Person(models.Model):
    title = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    grade = models.TextField(max_length=100)
    hometown = models.CharField(max_length=100)
    text = models.TextField(max_length=100, default = '')
    created_data = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
