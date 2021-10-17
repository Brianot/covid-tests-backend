from django.contrib import admin

# Register your models here.
from .models.user import User
from .models.test import Test
from .models.country import Country

admin.site.register(User)
admin.site.register(Test)
admin.site.register(Country)
