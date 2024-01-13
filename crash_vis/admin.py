from django.contrib import admin
from .models import *

admin.site.register(Crashes)

# Allows the model containing data to be viewed and edited in the Admin panel
