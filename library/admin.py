from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Kitob, Muallif

@admin.register(Kitob)
class TodoAdmin(ModelAdmin):
    search_fields = ["id", "nom", "sahifa"]
    list_filter = ["tur"]
    list_display = ["id", "nom", "tur"]
@admin.register(Muallif)
class TodoAdmin(ModelAdmin):
    search_fields = ["ism", "yosh"]
    list_filter = ["jins"]
    list_display = ["id", "ism", "yosh"]
