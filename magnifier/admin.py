from django.contrib import admin
from .models import Search

# Register your models here.
admin.site.register(Search)
admin.site.index_title = 'Welcom to the admin dashboard'
admin.site.site_header = 'Magnifier Admin'
admin.site.site_title

