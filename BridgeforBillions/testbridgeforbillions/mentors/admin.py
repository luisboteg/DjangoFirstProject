from django.contrib import admin
from testbridgeforbillions.mentors.models import Mentor
from import_export.admin import ExportActionMixin

@admin.register(Mentor)
class MentorAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ('name','email','gender')
    ordering = ('name','email','gender')
    search_fields = ('name','email','gender')
