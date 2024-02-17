from django.contrib import admin
from .models import Skateparks


class SkateparksAdmin(admin.ModelAdmin):
    list_display = (
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


# Register model
admin.site.register(Skateparks, SkateparksAdmin)
