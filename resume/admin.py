from django.contrib import admin
from .models import  *

class DetailAdmin(admin.ModelAdmin):
    list_display = "personal_detail skills phone_number".split()

class AcomplishmentAdmin(admin.ModelAdmin):
    list_display = 'work_completed years_of_exper total_client'.split()

class ProjectAdmin(admin.ModelAdmin):
    list_display = 'name topic proj_url project_created client'.split()

admin.site.register(Detail, DetailAdmin)
admin.site.register(Acomplishment, AcomplishmentAdmin)
admin.site.register(Project, ProjectAdmin)
