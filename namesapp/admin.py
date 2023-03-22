from django.contrib import admin
from .models import CatName


# Register your models here.
class CatNameAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(CatName, CatNameAdmin)