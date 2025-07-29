from django.contrib import admin

from uploads.models import Upload

class UploadAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'uploaded_at']
    search_fields = ('model_name',)

# Register your models here.
admin.site.register(Upload, UploadAdmin)