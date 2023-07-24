from django.contrib import admin
from .models import Resume

# Register your models here.

@admin.register(Resume)
class ResumeModel(admin.ModelAdmin):
    list_display = [
                    'name','DOB','gender','locality','city','state','pin',
                    'mobile','email','job_city','profile_image','my_file'
                    ]