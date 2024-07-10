from django.contrib import admin
from .models import Plade, Runde, Category, Kant, Anmeld, Kugle, Model

# Register your models here.
admin.site.register(Plade)
admin.site.register(Runde)
admin.site.register(Category)
admin.site.register(Kant)
admin.site.register(Anmeld)
admin.site.register(Kugle)
admin.site.register(Model)