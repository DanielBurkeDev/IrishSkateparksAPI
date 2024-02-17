from django.db import models


class Skateparks(models.Model):
    SURFACE_TYPE = [
        ("CONCRETE", "Concrete"),
        ("WOOD", "Wood"),
        ("UNKNOWN", "Unknown"),
    ]

    INDOOR_OUTDOOR = [
        ("INDOOR", "Indoor"),
        ("OUTDOOR", "Outdoor"),
        ("Un", "Unknown"),
    ]

    YES_NO = [
        ("Yes", "Yes"),
        ("No", "No"),
        ("Unknown", "Unknown"),
    ]

    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    image = models.CharField(max_length=500, blank=True)
    latitude = models.CharField(max_length=500)
    longitude = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    county = models.CharField(max_length=500, blank=True)
    phone = models.CharField(max_length=500, blank=True)
    email = models.CharField(max_length=500)
    website = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    rating = models.IntegerField()
    comment = models.CharField(max_length=500)
    lights = models.CharField(max_length=10, choices=YES_NO)
    openinghours = models.CharField(max_length=500)
    helmets = models.CharField(max_length=10, choices=YES_NO)
    surface = models.CharField(max_length=20, choices=SURFACE_TYPE)
    indooroutdoor = models.CharField(max_length=20, choices=INDOOR_OUTDOOR)
    fee = models.CharField(max_length=100)
    pros = models.CharField(max_length=1000, blank=True)
    cons = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self().name
