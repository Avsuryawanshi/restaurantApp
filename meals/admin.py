from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from meals.models import Meals,Category
# Register your models here.
class MealsAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['name','category','price']
    search_fields = ['name']
    list_filter = ['category']
admin.site.register(Meals,MealsAdmin)
admin.site.register(Category)