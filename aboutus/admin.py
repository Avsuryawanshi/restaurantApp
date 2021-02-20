from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import AboutUs,Why_Choose_Us,Chef
# Register your models here.
class ContactAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = '__all__'
    list_display = ['name','title']
    search_fields = ['title']
    list_filter = ['name','title']
admin.site.register(AboutUs)
admin.site.register(Why_Choose_Us)
admin.site.register(Chef,ContactAdmin)