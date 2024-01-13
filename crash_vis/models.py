from django.db import models

class Crashes (models.Model):
    Longitude = models.FloatField(("Longitude"))
    Latitude = models.FloatField(("Longitude"))

    def __str__(self):
        return '%s, %s' % (self.Longitude, self.Latitude)


# Creates "Crashes" model, creating a table in the database which was filled with data from an external .csv file
