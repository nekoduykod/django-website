from django.db import models


# class Location(models.Model):
#     country = models.CharField()
#     iso_code = models.CharField(max_length=3)
# TODO normalization


class Projects(models.Model):
    project_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    sector = models.TextField()
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.title