from django.contrib import admin
from .models import itemModel 

# Register your models here.
class itemAdmin(admin.ModelAdmin):
    list_display = ('item','featured','price',)

admin.site.register(itemModel, itemAdmin)
