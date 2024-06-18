from django.contrib import admin
from .models import Ucastnik, Dovolena, Rezervace, Recenze, Flight

admin.site.register(Ucastnik)
admin.site.register(Dovolena)
admin.site.register(Rezervace)
admin.site.register(Recenze)
admin.site.register(Flight)
