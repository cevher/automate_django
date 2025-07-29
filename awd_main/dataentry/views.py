import os
from django.conf import settings
from django.shortcuts import redirect, render

from dataentry.utils import get_all_custom_models
from uploads.models import Upload
from django.core.management import call_command
from django.contrib import messages

# Create your views here.

def import_data(request):
    # Placeholder for import data view logic
    context = {}
    if request.method == 'POST':
        # Handle form submission for importing data
        file_path = request.FILES.get('file_path')
        model_name = request.POST.get('model_name')
        
        # Store this file inside the Upload model
        if file_path and model_name:
            # Logic to save the uploaded file and associate it with the model
            # This is a placeholder; actual implementation will depend on your requirements
            upload = Upload.objects.create(file=file_path, model_name=model_name)
            
            # Construct the full path
            relative_path = str(upload.file.url)
            # print("relative_path==>", relative_path)
            base_url = str(settings.BASE_DIR)
            full_path = base_url + relative_path
            # print("full_path==>", full_path)
            # # trigger the import data command
            try:
                call_command('importdata', full_path, model_name)
                messages.success(request, f'Data imported successfully for model {model_name}!')
            except Exception as e:
                messages.error(request, f'Error importing data: {str(e)}')
                raise e
            
            
            return redirect('import_data')
    else: 
        all_models = get_all_custom_models()
        context = {
            'all_models': all_models,
        }
    
    return render(request, 'dataentry/importdata.html', context=context)