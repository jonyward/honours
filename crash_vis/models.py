from django.db import models

class Crashes (models.Model):

    Longitude = models.FloatField(("Longitude"))
    Latitude = models.FloatField(("Longitude"))

# Creates "Crashes" model, creating a table in the database which was filled with data from an external .csv file
