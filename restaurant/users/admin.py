from django.contrib import admin

# Register your models here.
from users.models import User, Table, TakeAway, Review, Comment

admin.site.register(User)
admin.site.register(Table)
admin.site.register(TakeAway)
admin.site.register(Review)
admin.site.register(Comment)

