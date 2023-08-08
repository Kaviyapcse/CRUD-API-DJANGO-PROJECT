from django.contrib import admin
from .models import Label

# Register your models here.
@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    data=['name','color','description']