from django.contrib import admin

# Register your models here.
from users.models import User, Address, Profile, Table

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Table)
