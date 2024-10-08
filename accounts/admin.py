from django.contrib import admin
from . models import *

# Register your models here.        #these display in the admin console
admin.site.register(Cinema),   
admin.site.register(Movie),
admin.site.register(Shows),