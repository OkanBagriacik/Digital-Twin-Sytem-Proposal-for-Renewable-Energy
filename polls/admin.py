from django.contrib import admin
from .models import Energy

admin.site.site_header = 'Decision Support System Dashboard'

admin.site.register(Energy)

