from django.contrib import admin
# #
from mailing_service.models import Mssg
#
admin.site.register(Mssg)
# #
# #
class Mssg(admin.ModelAdmin):
    list_display = ['topic', 'text']
