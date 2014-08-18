from django.contrib import admin

# Register your models here.
from users.models import Disc

class DiscAdmin(admin.ModelAdmin):
    pass

admin.site.register(Disc, DiscAdmin)
