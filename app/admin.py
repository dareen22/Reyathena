from django.contrib import admin
from app.models import Sport, Athlete, CustomUser

# Register your models here.

admin.site.register(Sport)
admin.site.register(Athlete)
admin.site.register(CustomUser)

