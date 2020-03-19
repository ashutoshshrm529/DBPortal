from django.contrib import admin
from .models import User, Staff, DBer, City, State

admin.site.register(User)
admin.site.register(Staff)
admin.site.register(DBer)
admin.site.register(City)
admin.site.register(State)
