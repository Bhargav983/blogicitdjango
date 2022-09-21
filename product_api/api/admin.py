from django.contrib import admin

from .models import Product, downloadexcel,reporttoday,agent

# Register your models here.

admin.site.register(Product)

admin.site.register(downloadexcel)

admin.site.register(reporttoday)

admin.site.register(agent)
