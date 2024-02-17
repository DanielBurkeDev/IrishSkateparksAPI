from rest_framework import serializers
from .models import Skateparks


class SkateparkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skateparks
        fields = (
            "id",
            "name",
            "image",
            "latitude",
            "longitude",
            "address",
            "county",
            "phone",
            "email",
            "website",
            "description",
            "rating",
            "comment",
            "lights",
            "openinghours",
            "helmets",
            "surface",
            "indooroutdoor",
            "fee",
            "pros",
            "cons",
        )
