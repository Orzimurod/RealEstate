from django.contrib import admin
from .models import Listing, Slides, advert, founder, Blog

admin.site.register(Slides)
admin.site.register(advert)
admin.site.register(founder)
admin.site.register(Blog)
admin.site.register(Listing)



