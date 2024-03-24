from django.db import models


# class Project_id(models.Model):
#     project_id_ = models.CharField(max_length=255)


# class Title(models.Model):
#     title_name = models.CharField(max_length=255)


# class Date(models.Model):
#     date_ = models.DateTimeField()


# class Amount(models.Model):
#     amount_ = models.DecimalField(max_digits=20, decimal_places=2)


# class Status(models.Model):
#     status_name = models.CharField(max_length=255)


# class Location(models.Model):
#     country = models.CharField()
#     iso_code = models.CharField(max_length=3)


# class Sector(models.Model):
#     sector_name = models.CharField(max_length=255)

# class Type(models.Model):
#     type_name = models.CharField(max_length=255)

# TODO normalization
class Projects(models.Model):
    project_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    # location = models.ForeignKey(Location, on_delete=models.SET_NULL)
    sector = models.TextField()
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.title


''' OK to have multiple tables in Postgresql ? Perhaps, logic for repetetive values can be done (see next) '''
    # project_id = models.ForeignKey(Project_id, on_delete=models.SET_NULL)
    # title = models.ForeignKey(Title, on_delete=models.SET_NULL)
    # date = models.ForeignKey(Date, on_delete=models.SET_NULL)
    # amount = models.ForeignKey(Amount, on_delete=models.SET_NULL)
    # status = models.ForeignKey(Status, on_delete=models.SET_NULL)
    # location = models.ForeignKey(Location, on_delete=models.SET_NULL)  # Assuming Location model exists
    # sector = models.ForeignKey(Sector, on_delete=models.SET_NULL)
    # type = models.ForeignKey(Type, on_delete=models.SET_NULL)


''' TODO Repetetive values alike this? As i`ve understood, it is a common practice, that helps 
    to reduce the load on the database and optimize the performance of the Django application '''

# class Projects(models.Model):
#     # Define choices for status field
#     STATUS_CHOICES = [
#         ('active', 'Active'),
#         ('closed', 'Closed'),
#     ]

#     project_id = models.CharField(max_length=255)
#     ...
#     status = models.CharField(max_length=255, choices=STATUS_CHOICES)  <====
#     location = models.CharField(max_length=255)
#     ...
