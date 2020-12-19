from django.contrib import admin
from .models import User, Class, Race, Character
        
admin.site.register(Class)
admin.site.register(Race)
admin.site.register(User)
admin.site.register(Character)
