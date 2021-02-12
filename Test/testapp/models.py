from django.db import models

# Create your models here.
class Period(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    objects = models.Manager()


class User(models.Model):
    id = models.CharField(max_length=10, primary_key=True, blank=False)
    real_name = models.CharField(max_length=20, blank=False)
    tz = models.CharField(max_length=30, blank=False)
    period = models.ManyToManyField(Period)
    objects = models.Manager()

    def __str__(self):
        return self.real_name
