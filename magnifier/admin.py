from django.contrib import admin
from .models import Search

# Register your models here.
admin.site.register(Search)
admin.site.site_title('Magnifier:Administrator')
admin.site.site_header('Magnifier Admin')

