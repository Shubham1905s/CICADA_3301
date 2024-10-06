from django.contrib import admin

# Register your models here.
from .models import GamePassword
from .models import ResultTeam

# Register your models here.
admin.site.register(GamePassword)
admin.site.register(ResultTeam)
