from django.contrib import admin
from testapp.models import Beer
# Register your models here.
class BeerAdmin(admin.ModelAdmin):
    list_display=('Bname','Taste','color','price')
admin.site.register(Beer,BeerAdmin)