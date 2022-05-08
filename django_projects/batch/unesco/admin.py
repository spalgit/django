from django.contrib import admin

# Register your models here.

from unesco.models import Site, Category, Region, Iso, States

admin.site.register(Site)
admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Iso)
admin.site.register(States)
