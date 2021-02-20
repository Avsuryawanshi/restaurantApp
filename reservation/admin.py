from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Reservation

# Register your models here.
class ReservationAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['name','email','phone','Date','time']
    search_fields = ['name']
    list_filter = ['email','Date']

admin.site.register(Reservation,ReservationAdmin)
