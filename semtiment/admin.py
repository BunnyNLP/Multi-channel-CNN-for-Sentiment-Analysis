from django.contrib import admin
from semtiment.models import ResultsModel
# Register your models here.
class ResultsModelAdmin(admin.ModelAdmin):
    search_fields=('semtiment','view',)
    list_filter=('semtiment',)
    list_display=('semtiment','view','sentence')

admin.site.register(ResultsModel,ResultsModelAdmin)
